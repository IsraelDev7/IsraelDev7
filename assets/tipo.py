"""
tipo.py — converte texto em contornos SVG usando a fonte real.

Por que vetorizar em vez de embutir a fonte: um SVG referenciado por
<img> no GitHub roda isolado, sem rede. Embutir a TTF em base64
funciona, mas custa ~90 KB por arquivo. Convertendo para `path`, o
texto vira geometria — fidelidade idêntica, alguns kilobytes, e nenhuma
dependência de carregamento.

O espacejamento é aplicado manualmente porque o kerning do GPOS exigiria
um motor de layout completo. Para tipografia de display, com tracking
definido à mão, a diferença não aparece.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen


class Fonte:
    def __init__(self, caminho):
        self.tt = TTFont(caminho)
        self.upm = self.tt["head"].unitsPerEm
        self.cmap = self.tt.getBestCmap()
        self.glifos = self.tt.getGlyphSet()
        self.hmtx = self.tt["hmtx"]

    def largura(self, texto, corpo, tracking=0.0):
        """Largura final da linha, em pixels, já com o tracking."""
        escala = corpo / self.upm
        total = 0.0
        for ch in texto:
            nome = self.cmap.get(ord(ch))
            if nome is None:
                total += corpo * 0.5
                continue
            total += self.hmtx[nome][0] * escala + corpo * tracking
        return total - (corpo * tracking if texto else 0)

    def caminho(self, texto, corpo, x=0.0, y=0.0, tracking=0.0):
        """Devolve um único `d` com todos os glifos posicionados.

        y é a LINHA DE BASE. O eixo do SVG cresce para baixo e o da
        fonte para cima, daí a escala negativa no segundo eixo.
        """
        escala = corpo / self.upm
        partes = []
        cursor = x

        for ch in texto:
            nome = self.cmap.get(ord(ch))
            if nome is None:
                cursor += corpo * 0.5
                continue

            pen = SVGPathPen(self.glifos)
            self.glifos[nome].draw(pen)
            d = pen.getCommands()

            if d:
                # translate + scale aplicados direto nos comandos seria
                # trabalhoso; envolver num grupo é mais simples e o
                # resultado é o mesmo.
                partes.append((d, cursor, y, escala))

            cursor += self.hmtx[nome][0] * escala + corpo * tracking

        return partes

    def grupo(self, texto, corpo, x, y, tracking=0.0, **attrs):
        """Monta o markup pronto: um <g> com um <path> por glifo."""
        extra = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
        saida = [f"<g {extra}>"]
        for d, gx, gy, escala in self.caminho(texto, corpo, x, y, tracking):
            saida.append(
                f'<path transform="translate({gx:.2f},{gy:.2f}) scale({escala:.5f},{-escala:.5f})" d="{d}"/>'
            )
        saida.append("</g>")
        return "".join(saida)

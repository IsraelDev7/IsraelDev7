"""
gerar_obras.py — as obras-primas, como cards.

── por que não usar a seção "Pinned" do GitHub ──
Porque ela não resolve este caso. O GitHub permite fixar repositório
privado, mas só mostra para quem já tem acesso — um recrutador
deslogado vê a fileira vazia. Das sete obras aqui, sete são privadas:
código de cliente não é do desenvolvedor para publicar.

Um card desenhado no README aparece para todo mundo, independe de
visibilidade, e ainda carrega o que a vitrine do GitHub não mostra: o
setor do cliente, o período real de trabalho e o que cada peça prova.

── por que o período vem do primeiro commit, e não da criação do repo ──
Quase todos os repositórios foram versionados em 2 de setembro, num
lote só. A data de criação diria "tudo feito no mesmo dia", o que é
falso e soa pior que não dizer nada. O primeiro commit é o registro
mais honesto que existe no repositório — e onde ele também está
achatado, o card mostra o mês da entrega, não uma faixa inventada.
"""
from tipo import Fonte

SG = Fonte("sg-bold.ttf")
JB = Fonte("jb-mono.ttf")

L, A = 1200, 372
MARGEM, GAP = 40, 16
COLS = 4
CARD = (L - 2 * MARGEM - (COLS - 1) * GAP) // COLS   # 268

TEMAS = {
    "dark":  dict(fundo="#0A0A0A", card="#121110", grade="#1D1C1A", borda="#26241F",
                  texto="#F5F0E8", fraco="#8A8478", solda="#D14D29", ouro="#C9A227"),
    "light": dict(fundo="#F5F0E8", card="#FFFFFF", grade="#DDD6C6", borda="#D8D0BE",
                  texto="#14120F", fraco="#6B655A", solda="#B03D1E", ouro="#8A6B12"),
}

OBRAS = [
    dict(n="01", nome="PORTFÓLIO", sub="SMART LABS",
         setor="OBRA PRÓPRIA", periodo="SET 2026",
         metrica="82", rotulo="COMMITS",
         pilha=["REACT 19", "GSAP", "THREE.JS", "LENIS"],
         prova="O MÉTODO É O PRODUTO"),
    dict(n="02", nome="BRUNO", sub="3 ENTREGAS",
         setor="CONSULTORIA · REINO UNIDO", periodo="MAI — SET 2026",
         metrica="03", rotulo="PROJETOS",
         pilha=["SERVERLESS", "SHEETS API", "WHATSAPP", "CRON"],
         prova="O CLIENTE VOLTOU DUAS VEZES"),
    dict(n="03", nome="DANILA", sub="2 ENTREGAS",
         setor="SAÚDE ESTÉTICA", periodo="JUL — SET 2026",
         metrica="02", rotulo="PROJETOS",
         pilha=["POSTGRES", "PRISMA", "N8N", "EXPRESS"],
         prova="SITE E AUTOMAÇÃO JUNTOS"),
    dict(n="04", nome="TIAGO", sub="TL GARDEN",
         setor="PAISAGISMO · REINO UNIDO", periodo="SET 2026",
         metrica="07", rotulo="PERGUNTAS",
         pilha=["MOTOR DE REGRAS", "FIREBASE", "SEO"],
         prova="O LEAD CHEGA DIAGNOSTICADO"),
]


def card(c, o, i):
    x = MARGEM + i * (CARD + GAP)
    y = 74
    h = 252
    p = []

    p.append(f'<rect x="{x}" y="{y}" width="{CARD}" height="{h}" fill="{c["card"]}" stroke="{c["borda"]}" stroke-width="1"/>')

    # cantoneira superior esquerda — a mesma marca do cabeçalho, em escala menor
    p.append(f'<path d="M{x},{y + 16} L{x},{y} L{x + 16},{y}" fill="none" stroke="{c["solda"]}" stroke-width="2"/>')

    px = x + 18

    # índice e estado
    p.append(JB.grupo(f"//{o['n']}", 10, px, y + 26, tracking=0.16, fill=c["fraco"]))
    p.append(f'<circle cx="{x + CARD - 24}" cy="{y + 22}" r="3.2" fill="{c["solda"]}" class="piscar" style="animation-delay:{i * 0.4:.1f}s"/>')

    # nome
    p.append(SG.grupo(o["nome"], 27, px, y + 62, tracking=-0.03, fill=c["texto"]))
    p.append(JB.grupo(o["sub"], 10, px, y + 80, tracking=0.16, fill=c["solda"]))

    # setor e período
    p.append(f'<line x1="{px}" y1="{y + 94}" x2="{x + CARD - 18}" y2="{y + 94}" stroke="{c["grade"]}" stroke-width="1"/>')
    p.append(JB.grupo(o["setor"], 8.5, px, y + 112, tracking=0.12, fill=c["fraco"]))
    p.append(JB.grupo(o["periodo"], 10, px, y + 130, tracking=0.14, fill=c["ouro"]))

    # métrica
    p.append(SG.grupo(o["metrica"], 34, px, y + 176, tracking=-0.03, fill=c["solda"]))
    larg_m = SG.largura(o["metrica"], 34, -0.03)
    p.append(JB.grupo(o["rotulo"], 8.5, px + larg_m + 9, y + 176, tracking=0.12, fill=c["fraco"]))

    # pilha — chips
    cx_, cy_ = px, y + 196
    for t in o["pilha"]:
        w = JB.largura(t, 7.5, 0.1) + 12
        if cx_ + w > x + CARD - 16:
            cx_, cy_ = px, cy_ + 16
        if cy_ > y + h - 34:
            break
        p.append(f'<rect x="{cx_:.0f}" y="{cy_}" width="{w:.0f}" height="13" fill="none" stroke="{c["borda"]}" stroke-width="1"/>')
        p.append(JB.grupo(t, 7.5, cx_ + 6, cy_ + 9, tracking=0.1, fill=c["fraco"]))
        cx_ += w + 5

    # a prova, no rodapé do card
    p.append(f'<line x1="{px}" y1="{y + h - 26}" x2="{x + CARD - 18}" y2="{y + h - 26}" stroke="{c["grade"]}" stroke-width="1"/>')
    p.append(JB.grupo(o["prova"], 8.5, px, y + h - 11, tracking=0.1, fill=c["texto"]))

    return "".join(p)


def construir(tema):
    c = TEMAS[tema]
    escuro = tema == "dark"
    cards = "".join(card(c, o, i) for i, o in enumerate(OBRAS))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {A}" width="{L}" height="{A}" role="img" aria-label="Obras: Portfólio Smart LABS, Bruno, Danila e Tiago">
<defs>
  <pattern id="g" width="30" height="30" patternUnits="userSpaceOnUse">
    <path d="M30 0H0V30" fill="none" stroke="{c['grade']}" stroke-width="1" opacity="{0.4 if escuro else 0.55}"/>
  </pattern>
  <style>
    .piscar {{ animation:piscar 2.1s steps(1,end) infinite; }}
    @keyframes piscar {{ 0%,62% {{ opacity:1 }} 63%,80% {{ opacity:.18 }} 81% {{ opacity:1 }} }}
    @media (prefers-reduced-motion:reduce) {{ .piscar {{ animation:none; opacity:1 }} }}
  </style>
</defs>
<rect width="{L}" height="{A}" fill="{c['fundo']}"/>
<rect width="{L}" height="{A}" fill="url(#g)" opacity="{0.45 if escuro else 0.5}"/>

{JB.grupo("OBRAS", 11, MARGEM, 38, tracking=0.2, fill=c['solda'])}
<line x1="{MARGEM + 58}" y1="34" x2="{L - MARGEM}" y2="34" stroke="{c['grade']}" stroke-width="1"/>
{JB.grupo("REPOSITÓRIOS PRIVADOS — CÓDIGO DE CLIENTE NÃO É MEU PARA PUBLICAR", 8.5, MARGEM, 56, tracking=0.12, fill=c['fraco'])}

{cards}

{JB.grupo("APRESENTO QUALQUER UMA EM DETALHE NUMA CONVERSA", 9, MARGEM, 352, tracking=0.14, fill=c['fraco'])}
</svg>'''


if __name__ == "__main__":
    import os
    for tema in ("dark", "light"):
        nome = "obras.svg" if tema == "dark" else "obras-light.svg"
        open(nome, "w", encoding="utf-8").write(construir(tema))
        print(f"  {nome}  {os.path.getsize(nome) / 1024:.1f} KB")

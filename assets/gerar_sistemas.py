"""
gerar_sistemas.py — painel de sistemas.

── por que os seis módulos viram MARK I a VI ──
A progressão das armaduras do Stark é numerada e cumulativa: cada marca
herda a anterior e resolve o que faltava. Os seis módulos do portfólio
funcionam igual — Design, Development, Automation, Data, AI e Security
são ordem de construção, não cardápio. A analogia não foi imposta ao
conteúdo: os dois já tinham a mesma forma.

E o MARK VI aparece como EM CONSTRUÇÃO porque ele está. Marcar tudo
como pronto custaria a única coisa que esta página está tentando
comprar, que é confiança.
"""
from tipo import Fonte

SG = Fonte("sg-bold.ttf")
JB = Fonte("jb-mono.ttf")

L, A = 1200, 300

MODULOS = [
    ("01", "DESIGN",      "COMO A PESSOA ENTENDE",      100),
    ("02", "DEVELOPMENT", "O QUE SUSTENTA",             100),
    ("03", "AUTOMATION",  "O QUE TRABALHA SOZINHO",     100),
    ("04", "DATA",        "O QUE O NEGÓCIO APRENDE",     85),
    ("05", "AI",          "O QUE DECIDE JUNTO",          70),
    ("06", "SECURITY",    "O QUE PODE SER CONFIADO",     35),
]

TEMAS = {
    "dark":  dict(fundo="#0A0A0A", grade="#1D1C1A", texto="#F5F0E8",
                  fraco="#8A8478", solda="#D14D29", ouro="#C9A227", trilho="#221F1C"),
    "light": dict(fundo="#F5F0E8", grade="#DDD6C6", texto="#14120F",
                  fraco="#6B655A", solda="#B03D1E", ouro="#8A6B12", trilho="#E4DCCE"),
}


def construir(tema):
    c = TEMAS[tema]
    escuro = tema == "dark"
    col = (L - 80) / 6
    corpo = []

    for i, (cod, nome, papel, nivel) in enumerate(MODULOS):
        x = 40 + i * col
        pronto = nivel >= 100
        cor = c["solda"] if pronto else c["ouro"]

        # separador entre colunas
        if i:
            corpo.append(f'<line x1="{x - 12:.0f}" y1="64" x2="{x - 12:.0f}" y2="248" stroke="{c["grade"]}" stroke-width="1"/>')

        corpo.append(JB.grupo(f"MARK {'I' * (i + 1) if i < 3 else ['IV','V','VI'][i - 3]}", 10, x, 86, tracking=0.18, fill=c["ouro"]))
        corpo.append(JB.grupo(f"MOD —— {cod}", 10, x, 106, tracking=0.16, fill=c["fraco"]))
        corpo.append(SG.grupo(nome, 20, x, 140, tracking=-0.02, fill=c["texto"]))

        # papel, quebrado em duas linhas para caber na coluna
        palavras, linha, linhas = papel.split(), "", []
        for p in palavras:
            teste = (linha + " " + p).strip()
            if JB.largura(teste, 9, 0.1) > col - 26 and linha:
                linhas.append(linha); linha = p
            else:
                linha = teste
        linhas.append(linha)
        for j, ln in enumerate(linhas[:2]):
            corpo.append(JB.grupo(ln, 9, x, 162 + j * 13, tracking=0.1, fill=c["fraco"]))

        # barra de nível — oito degraus, como o símbolo dos Degraus da marca
        for d in range(8):
            aceso = d < round(nivel / 100 * 8)
            corpo.append(
                f'<rect x="{x + d * 14:.0f}" y="200" width="10" height="{6 + d * 2}" '
                f'y2="0" transform="translate(0,{20 - (6 + d * 2)})" '
                f'fill="{cor if aceso else c["trilho"]}" '
                f'{"class=\'degrau\' style=\'animation-delay:%.2fs\'" % (i * 0.18 + d * 0.06) if aceso else ""}/>'
            )

        estado = "OPERACIONAL" if pronto else ("EM CONSTRUÇÃO" if nivel < 50 else "PARCIAL")
        corpo.append(f'<circle cx="{x + 4:.0f}" cy="240" r="3.4" fill="{cor}" '
                     f'{"class=\'piscar\'" if not pronto else ""}/>')
        corpo.append(JB.grupo(estado, 9, x + 14, 243, tracking=0.12, fill=cor))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {A}" width="{L}" height="{A}" role="img" aria-label="Seis módulos: Design, Development, Automation, Data, AI e Security">
<defs>
  <pattern id="g" width="30" height="30" patternUnits="userSpaceOnUse">
    <path d="M30 0H0V30" fill="none" stroke="{c['grade']}" stroke-width="1" opacity="{0.45 if escuro else 0.6}"/>
  </pattern>
  <style>
    .degrau {{ transform-origin:center bottom; animation:acender 3s ease-in-out infinite; }}
    .piscar {{ animation:piscar 1.7s steps(1,end) infinite; }}
    @keyframes acender {{ 0%,100% {{ opacity:.45 }} 50% {{ opacity:1 }} }}
    @keyframes piscar  {{ 0%,60% {{ opacity:1 }} 61%,80% {{ opacity:.2 }} 81% {{ opacity:1 }} }}
    @media (prefers-reduced-motion:reduce) {{ .degrau,.piscar {{ animation:none; opacity:1 }} }}
  </style>
</defs>
<rect width="{L}" height="{A}" fill="{c['fundo']}"/>
<rect width="{L}" height="{A}" fill="url(#g)" opacity="{0.45 if escuro else 0.55}"/>

{JB.grupo("PAINEL DE SISTEMAS", 11, 40, 40, tracking=0.2, fill=c['solda'])}
<line x1="40" y1="52" x2="{L - 40}" y2="52" stroke="{c['grade']}" stroke-width="1"/>

{"".join(corpo)}

<line x1="40" y1="264" x2="{L - 40}" y2="264" stroke="{c['grade']}" stroke-width="1"/>
{JB.grupo("ORDEM DE CONSTRUÇÃO, NÃO CARDÁPIO — CADA UM SUSTENTA O SEGUINTE", 10, 40, 282, tracking=0.14, fill=c['fraco'])}
</svg>'''


if __name__ == "__main__":
    import os
    for tema in ("dark", "light"):
        nome = "sistemas.svg" if tema == "dark" else "sistemas-light.svg"
        open(nome, "w", encoding="utf-8").write(construir(tema))
        print(f"  {nome}  {os.path.getsize(nome) / 1024:.1f} KB")

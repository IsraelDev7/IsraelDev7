"""
gerar_banner.py — o cabeçalho do perfil.

── a ponte entre o Homem de Ferro e a marca ──
Ela já existia e não precisou ser forçada. O Solda (#D14D29) da Smart
LABS é laranja-metal quente: é exatamente a cor do reator. O Aço
(#0A0A0A) é a chapa escura da armadura. O que faltava era o ouro, que
entra só nos suportes do HUD — acento, nunca protagonista.

E o vocabulário de HUD (retículas, cantoneiras, telemetria em
monoespaçada) não é fantasia nova: o portfólio já rotula as seções como
`MOD —— 01` e `//001`. O visor do Stark é a continuação natural desse
sistema, não uma roupa emprestada.

── por que animação em CSS dentro do SVG ──
O GitHub serve o SVG como imagem, num contexto isolado: não há rede,
não há script. Sobram `@keyframes` e SMIL, que rodam normalmente. É o
que permite um cabeçalho vivo sem depender de serviço de terceiro que
quebra sozinho daqui a um ano.
"""
import math
from tipo import Fonte

SG = Fonte("sg-bold.ttf")
JB = Fonte("jb-mono.ttf")

L, A = 1200, 340          # largura e altura
CX, CY = 176, 170         # centro do reator

TEMAS = {
    "dark": dict(
        fundo="#0A0A0A", chapa="#141414", grade="#1D1C1A",
        texto="#F5F0E8", fraco="#8A8478",
        solda="#D14D29", ouro="#C9A227", brilho="#FF7A4D",
    ),
    "light": dict(
        fundo="#F5F0E8", chapa="#EAE4D8", grade="#DDD6C6",
        texto="#14120F", fraco="#6B655A",
        solda="#B03D1E", ouro="#8A6B12", brilho="#D14D29",
    ),
}


def reator(c):
    """O reator: três anéis em rotações opostas e um núcleo que pulsa."""
    p = []

    # halo — o que dá a sensação de luz, e não de desenho
    p.append(f'<circle cx="{CX}" cy="{CY}" r="104" fill="url(#halo)"/>')

    # anel externo tracejado, girando devagar no sentido horário
    p.append(
        f'<g class="gira-h"><circle cx="{CX}" cy="{CY}" r="92" fill="none" '
        f'stroke="{c["ouro"]}" stroke-width="1.5" stroke-dasharray="3 9" opacity="0.75"/></g>'
    )

    # anel de segmentos, girando ao contrário — o contraste de sentidos
    # é o que faz o conjunto parecer mecanismo, e não enfeite
    seg = []
    for i in range(24):
        ang = i * 15
        r1, r2 = 74, (86 if i % 3 == 0 else 81)
        x1 = CX + r1 * math.cos(math.radians(ang))
        y1 = CY + r1 * math.sin(math.radians(ang))
        x2 = CX + r2 * math.cos(math.radians(ang))
        y2 = CY + r2 * math.sin(math.radians(ang))
        op = "0.9" if i % 3 == 0 else "0.4"
        seg.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{c["ouro"]}" stroke-width="2" opacity="{op}"/>'
        )
    p.append(f'<g class="gira-ah">{"".join(seg)}</g>')

    # anel de contenção
    p.append(
        f'<circle cx="{CX}" cy="{CY}" r="64" fill="none" stroke="{c["solda"]}" '
        f'stroke-width="2.5" opacity="0.85"/>'
    )

    # as dez bobinas: o desenho que identifica o reator de imediato
    bob = []
    for i in range(10):
        ang = i * 36 - 90
        x = CX + 44 * math.cos(math.radians(ang))
        y = CY + 44 * math.sin(math.radians(ang))
        bob.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="none" '
            f'stroke="{c["solda"]}" stroke-width="2"/>'
        )
        bob.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{c["brilho"]}" '
            f'class="bobina" style="animation-delay:{i * 0.12:.2f}s"/>'
        )
    p.append("".join(bob))

    # triângulo interno — a assinatura do reator do Mark II em diante
    t = []
    for i in range(3):
        ang = i * 120 - 90
        t.append(f"{CX + 26 * math.cos(math.radians(ang)):.1f},{CY + 26 * math.sin(math.radians(ang)):.1f}")
    p.append(
        f'<polygon points="{" ".join(t)}" fill="none" stroke="{c["ouro"]}" '
        f'stroke-width="2" opacity="0.9" class="respira"/>'
    )

    # núcleo
    p.append(f'<circle cx="{CX}" cy="{CY}" r="17" fill="url(#nucleo)" class="pulso"/>')
    p.append(f'<circle cx="{CX}" cy="{CY}" r="8" fill="{c["texto"]}" opacity="0.95" class="pulso"/>')

    return "".join(p)


def ondas(c):
    """As mesmas barras da seção Cisão do portfólio, geradas pelo mesmo
    LCG determinístico. Com `random`, o desenho mudaria a cada build e
    o cabeçalho cintilaria entre commits; com semente fixa, a peça tem
    identidade estável — e é a mesma decisão tomada lá."""
    s = 1337
    def rnd():
        nonlocal s
        s = (s * 1664525 + 1013904223) % 4294967296
        return s / 4294967296

    n = 40
    bruto = [rnd() for _ in range(n)]
    # média móvel de três: é ela que dá CONTINUIDADE ao contorno. Sem
    # isso cada barra ignora a vizinha e vira chuvisco.
    suave = [(bruto[(i - 1) % n] + bruto[i] * 2 + bruto[(i + 1) % n]) / 4 for i in range(n)]

    # 40 barras a partir de 880: termina em 1158, com 24px de folga
    # até a cantoneira direita (1182). Barra encostando em moldura
    # lê como erro de corte, não como desenho.
    x0, base, larg, altmax = 880, 268, 5, 108
    out = []
    for i in range(n):
        t = i / n
        env = 0.24 + 0.12 * math.sin(t * math.pi * 4.3) + 0.09 * math.sin(t * math.pi * 9.7 + 1.7)
        sorte = rnd()
        pico = 0.3 + rnd() * 0.3 if sorte > 0.86 else 0
        vale = -0.26 if sorte < 0.18 else 0
        h = max(0.05, min(1, env + suave[i] * 0.72 + pico + vale)) * altmax
        x = x0 + i * (larg + 2)
        op = 0.22 + 0.5 * (h / altmax)
        out.append(
            f'<rect x="{x}" y="{base - h:.1f}" width="{larg}" height="{h:.1f}" '
            f'fill="{c["solda"]}" opacity="{op:.2f}" class="barra" '
            f'style="animation-delay:{i * 0.045:.2f}s"/>'
        )
    out.append(f'<line x1="{x0}" y1="{base}" x2="{x0 + n * (larg + 2) - 2}" y2="{base}" stroke="{c["grade"]}" stroke-width="1"/>')
    return "".join(out)


def reticula(c):
    """Retícula de visor no canto superior direito — o enquadramento
    que o HUD do capacete faz antes de travar o alvo."""
    cx, cy, r = 1012, 104, 44
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["ouro"]}" stroke-width="1.2" opacity="0.5"/>']
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 13}" fill="none" stroke="{c["ouro"]}" stroke-width="1" stroke-dasharray="2 6" opacity="0.6" class="gira-retic"/>')
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        out.append(
            f'<line x1="{cx + dx * (r - 8)}" y1="{cy + dy * (r - 8)}" '
            f'x2="{cx + dx * (r + 9)}" y2="{cy + dy * (r + 9)}" '
            f'stroke="{c["ouro"]}" stroke-width="1.6" opacity="0.8"/>'
        )
    out.append(f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{c["solda"]}" class="pulso-retic"/>')
    return "".join(out)


def cantoneiras(c):
    """Cantoneiras de visor. Enquadram sem fechar — moldura completa
    viraria borda de cartão, e a leitura de HUD se perde."""
    b, m = 26, 18   # braço e margem
    out = []
    for sx, sy, ox, oy in ((1, 1, m, m), (-1, 1, L - m, m), (1, -1, m, A - m), (-1, -1, L - m, A - m)):
        out.append(
            f'<path d="M{ox},{oy + sy * b} L{ox},{oy} L{ox + sx * b},{oy}" fill="none" '
            f'stroke="{c["ouro"]}" stroke-width="2" opacity="0.85"/>'
        )
    return "".join(out)


def telemetria(c, y):
    """A linha de dados. Cada número aqui é verificável — inventar
    métrica num cabeçalho é a forma mais rápida de perder a confiança
    que o resto do perfil está tentando construir."""
    itens = [("CLIENTES", "03"), ("ENTREGAS", "06"), ("RETORNOS", "02"), ("PAÍSES", "02")]
    out, x = [], 470
    for i, (rot, val) in enumerate(itens):
        out.append(JB.grupo(rot, 11, x, y, tracking=0.12, fill=c["fraco"]))
        out.append(SG.grupo(val, 26, x, y + 30, tracking=-0.02, fill=c["solda"]))
        largura = max(JB.largura(rot, 11, 0.12), 40)
        if i < len(itens) - 1:
            xs = x + largura + 26
            out.append(f'<line x1="{xs}" y1="{y - 12}" x2="{xs}" y2="{y + 36}" stroke="{c["grade"]}" stroke-width="1"/>')
        x += largura + 52
    return "".join(out)


def construir(tema):
    c = TEMAS[tema]
    escuro = tema == "dark"

    # grade de fundo: dá profundidade sem competir com o texto
    grade = (
        f'<pattern id="g" width="34" height="34" patternUnits="userSpaceOnUse">'
        f'<path d="M34 0H0V34" fill="none" stroke="{c["grade"]}" stroke-width="1" opacity="{0.55 if escuro else 0.75}"/>'
        f"</pattern>"
    )

    # fios verticais — a mesma peça da seção Cisão do portfólio
    fios = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="{A}" stroke="{c["grade"]}" stroke-width="1" opacity="0.6"/>'
        for x in range(430, L, 96)
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {A}" width="{L}" height="{A}" role="img" aria-label="Israel Passos — engenharia de sistemas de aquisição">
<defs>
  {grade}
  <radialGradient id="halo">
    <stop offset="0%" stop-color="{c['solda']}" stop-opacity="{0.34 if escuro else 0.20}"/>
    <stop offset="55%" stop-color="{c['solda']}" stop-opacity="0.09"/>
    <stop offset="100%" stop-color="{c['solda']}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="nucleo">
    <stop offset="0%" stop-color="#FFFFFF"/>
    <stop offset="45%" stop-color="{c['brilho']}"/>
    <stop offset="100%" stop-color="{c['solda']}"/>
  </radialGradient>
  <linearGradient id="varredura" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{c['solda']}" stop-opacity="0"/>
    <stop offset="50%" stop-color="{c['solda']}" stop-opacity="{0.5 if escuro else 0.3}"/>
    <stop offset="100%" stop-color="{c['solda']}" stop-opacity="0"/>
  </linearGradient>
  <style>
    .gira-h  {{ transform-origin:{CX}px {CY}px; animation:girar 22s linear infinite; }}
    .gira-ah {{ transform-origin:{CX}px {CY}px; animation:girar 30s linear infinite reverse; }}
    .pulso   {{ transform-origin:{CX}px {CY}px; animation:pulsar 2.6s ease-in-out infinite; }}
    .respira {{ transform-origin:{CX}px {CY}px; animation:respirar 4s ease-in-out infinite; }}
    .bobina  {{ animation:acender 2.6s ease-in-out infinite; }}
    .scan    {{ animation:varrer 7s cubic-bezier(.4,0,.6,1) infinite; }}
    .piscar  {{ animation:piscar 1.9s steps(1,end) infinite; }}
    .barra   {{ transform-origin:center bottom; animation:subir 3.4s ease-in-out infinite; }}
    .gira-retic {{ transform-origin:1012px 104px; animation:girar 14s linear infinite; }}
    .pulso-retic {{ transform-origin:1012px 104px; animation:pulsar 2.2s ease-in-out infinite; }}
    @keyframes girar   {{ to {{ transform:rotate(360deg); }} }}
    @keyframes pulsar  {{ 0%,100% {{ transform:scale(1); opacity:.92 }} 50% {{ transform:scale(1.13); opacity:1 }} }}
    @keyframes respirar{{ 0%,100% {{ transform:rotate(0deg); opacity:.55 }} 50% {{ transform:rotate(120deg); opacity:1 }} }}
    @keyframes acender {{ 0%,100% {{ opacity:.35 }} 50% {{ opacity:1 }} }}
    @keyframes varrer  {{ 0% {{ transform:translateY(-20px); opacity:0 }} 12% {{ opacity:1 }} 88% {{ opacity:1 }} 100% {{ transform:translateY({A}px); opacity:0 }} }}
    @keyframes piscar  {{ 0%,62% {{ opacity:1 }} 63%,78% {{ opacity:.15 }} 79% {{ opacity:1 }} }}
    @keyframes subir   {{ 0%,100% {{ transform:scaleY(.72) }} 50% {{ transform:scaleY(1) }} }}
    /* Quem pediu menos movimento recebe o cabeçalho parado — e ele
       continua legível, porque nada aqui depende de animar. */
    @media (prefers-reduced-motion:reduce) {{
      .gira-h,.gira-ah,.pulso,.respira,.bobina,.scan,.piscar,.barra,.gira-retic,.pulso-retic {{ animation:none; }}
      .scan {{ opacity:0; }}
    }}
  </style>
</defs>

<rect width="{L}" height="{A}" fill="{c['fundo']}"/>
<rect width="{L}" height="{A}" fill="url(#g)" opacity="{0.5 if escuro else 0.6}"/>
{fios}
<rect x="0" y="0" width="{L}" height="2" fill="url(#varredura)" class="scan"/>

{reator(c)}
{ondas(c)}
{reticula(c)}
{cantoneiras(c)}

<!-- sobrescrito -->
{JB.grupo("SMART LABS", 12, 430, 96, tracking=0.2, fill=c['solda'])}
<line x1="{430 + JB.largura('SMART LABS', 12, 0.2) + 12}" y1="92" x2="{430 + JB.largura('SMART LABS', 12, 0.2) + 42}" y2="92" stroke="{c['solda']}" stroke-width="1.5"/>
{JB.grupo("UNIDADE 01", 12, 430 + JB.largura('SMART LABS', 12, 0.2) + 52, 96, tracking=0.2, fill=c['fraco'])}

<!-- nome -->
{SG.grupo("ISRAEL PASSOS", 68, 428, 164, tracking=-0.028, fill=c['texto'])}

<!-- função -->
{JB.grupo("ENGENHARIA DE SISTEMAS DE AQUISIÇÃO", 14, 430, 198, tracking=0.13, fill=c['fraco'])}

<!-- estado -->
<circle cx="436" cy="228" r="5" fill="{c['solda']}" class="piscar"/>
{JB.grupo("REATOR ATIVO", 11, 450, 232, tracking=0.16, fill=c['solda'])}

{telemetria(c, 286)}
</svg>'''
    return svg


for tema in ("dark", "light"):
    nome = "banner.svg" if tema == "dark" else "banner-light.svg"
    with open(nome, "w", encoding="utf-8") as fh:
        fh.write(construir(tema))
    import os
    print(f"  {nome}  {os.path.getsize(nome) / 1024:.1f} KB")

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./banner.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./banner-light.svg?v=1">
  <img src="./banner.svg?v=1" alt="Israel Passos — engenharia de sistemas de aquisição" width="100%"/>
</picture>

</div>

<br/>

<div align="center">

**Construo páginas que continuam trabalhando depois que carregam.**

A maior parte do mercado entrega uma peça bonita e estática.
Eu entrego a peça bonita **e a máquina que a atende**.

<sub>Smart LABS · Goiânia, Brasil · atendendo Brasil e Reino Unido</sub>

</div>

<br/>

---

## `//` MODO DE OPERAÇÃO

Instrumentação por seção. Resposta automática ao lead em segundos. Registro
próprio dos dados do cliente. E um relatório que chega até ele **sem que
precise abrir painel nenhum** — porque painel que o cliente não abre não
existe.

<table>
<tr>
<td width="33%" valign="top">

**MEDIR**
<br/><sub>Cada clique guarda seção, rótulo e origem. Dá para cruzar *qual bloco gerou interesse* com *qual lead entrou* — e cortar criativo que traz clique sem contato.</sub>

</td>
<td width="33%" valign="top">

**RESPONDER**
<br/><sub>E-mail e WhatsApp ao lead em segundos. Velocidade de primeira resposta é o fator isolado que mais move conversão.</sub>

</td>
<td width="33%" valign="top">

**REPORTAR**
<br/><sub>Resumo do dia no WhatsApp do dono, às 23h, gerado sozinho. Zero curva de aprendizado — e é por isso que ele continua usando.</sub>

</td>
</tr>
</table>

<br/>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./sistemas.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./sistemas-light.svg?v=1">
  <img src="./sistemas.svg?v=1" alt="Seis módulos: Design, Development, Automation, Data, AI e Security" width="100%"/>
</picture>

<sub>O MARK VI aparece incompleto porque está. Marcar tudo como pronto custaria a única coisa que esta página tenta comprar.</sub>

</div>

<br/>

---

## `//` ARSENAL

<div align="center">

![React](https://img.shields.io/badge/React-0A0A0A?style=flat-square&logo=react&logoColor=D14D29)
![Next.js](https://img.shields.io/badge/Next.js-0A0A0A?style=flat-square&logo=nextdotjs&logoColor=F5F0E8)
![TypeScript](https://img.shields.io/badge/TypeScript-0A0A0A?style=flat-square&logo=typescript&logoColor=D14D29)
![Vite](https://img.shields.io/badge/Vite-0A0A0A?style=flat-square&logo=vite&logoColor=C9A227)
![GSAP](https://img.shields.io/badge/GSAP-0A0A0A?style=flat-square&logo=greensock&logoColor=C9A227)
![Three.js](https://img.shields.io/badge/Three.js-0A0A0A?style=flat-square&logo=threedotjs&logoColor=F5F0E8)

![Node.js](https://img.shields.io/badge/Node.js-0A0A0A?style=flat-square&logo=nodedotjs&logoColor=D14D29)
![Express](https://img.shields.io/badge/Express-0A0A0A?style=flat-square&logo=express&logoColor=F5F0E8)
![Prisma](https://img.shields.io/badge/Prisma-0A0A0A?style=flat-square&logo=prisma&logoColor=C9A227)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0A0A0A?style=flat-square&logo=postgresql&logoColor=D14D29)
![Supabase](https://img.shields.io/badge/Supabase-0A0A0A?style=flat-square&logo=supabase&logoColor=C9A227)

![Stripe](https://img.shields.io/badge/Stripe-0A0A0A?style=flat-square&logo=stripe&logoColor=D14D29)
![n8n](https://img.shields.io/badge/n8n-0A0A0A?style=flat-square&logo=n8n&logoColor=C9A227)
![OpenAI](https://img.shields.io/badge/OpenAI-0A0A0A?style=flat-square&logo=openai&logoColor=F5F0E8)
![Vercel](https://img.shields.io/badge/Vercel-0A0A0A?style=flat-square&logo=vercel&logoColor=F5F0E8)
![Docker](https://img.shields.io/badge/Docker-0A0A0A?style=flat-square&logo=docker&logoColor=D14D29)

</div>

<br/>

---

## `//` OBRAS

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./obras.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./obras-light.svg?v=1">
  <img src="./obras.svg?v=1" alt="Obras: Portfólio Smart LABS, Bruno, Danila e Tiago" width="100%"/>
</picture>

</div>

<br/>

### O que dá para abrir agora

| | Repositório | O que demonstra |
|:---:|:---|:---|
| `05` | [**DevBurger**](https://github.com/IsraelDev7/Dev_buger_final) · <sub>MAI 2026</sub> | E-commerce full-stack: JWT + bcrypt, validação com Yup, upload, Stripe do carrinho ao webhook, painel administrativo |
| `06` | [**SmartFit AI Platform**](https://github.com/IsraelDev7/Smart-fitAI) · <sub>MAR 2026</sub> | Monorepo com mobile e web dividindo o mesmo contrato de tipos, Supabase com RLS, cobrança por webhook e CI |

<br/>

---

## `//` PROTOCOLOS

<details open>
<summary><b>01 · Medir, não olhar</b></summary>

<br/>

Screenshot mostra que *parece* certo. Medição mostra que *está* certo. Três
defeitos que nenhuma inspeção visual pegaria:

- **Um item flex inflando de 746 para 1002px.** `flex: 0 0 52%` fixa a
  **base**, não o **mínimo** — todo item flex nasce com `min-width: auto`, e um
  texto em `nowrap` entrou no `min-content`. A saída foi tirar o elemento do
  fluxo, não `min-width: 0`.
- **Uma media query perdendo para uma regra base escrita depois.** Media query
  não soma especificidade; o desempate é a ordem no arquivo. A correção foi
  reescrever como `min-width`, não `!important` — regra que não existe no
  telefone não vaza para o telefone.
- **Duas animações disputando as mesmas propriedades** porque foram *criadas*
  na ordem errada: um `fromTo` sob ScrollTrigger grava o estado inicial no ato
  da criação, não quando dispara.

</details>

<details>
<summary><b>02 · Saber quando <i>não</i> usar IA</b></summary>

<br/>

O diagnóstico do site de paisagismo podia ser uma chamada de LLM. Não é — é um
motor de regras com pontuação ponderada, definida junto com o especialista.

Determinístico (as mesmas respostas dão sempre o mesmo laudo), auditável linha
a linha por quem entende do assunto, instantâneo e de custo zero. Um modelo de
linguagem seria pior em tudo que importa nesse caso — e poderia alucinar uma
recomendação técnica para alguém que vai contratar um serviço.

Quando IA entra, entra no lugar certo: **a régua calcula, o modelo redige.**
Decisão determinística, linguagem natural só na apresentação.

</details>

<details>
<summary><b>03 · Não deixar o sistema falhar calado</b></summary>

<br/>

O padrão mais caro que encontro — inclusive em código meu — é o sucesso
presumido: a tela diz "enviado" e nada foi. Já corrigi quatro variações:

| Variação | Por que ela engana |
|:---|:---|
| `fire and forget` depois de responder | Em serverless, o container pode ser congelado antes das promessas terminarem |
| `mode: 'no-cors'` | A resposta é opaca — o código **não consegue** saber se funcionou |
| `catch` marcando sucesso como reserva | O erro vira confirmação |
| `console.log` no lugar de banco | Log expira, não se consulta, não se agrupa |

Hoje toda entrega que eu escrevo espera confirmação antes de responder, e o
erro aparece na tela de quem está do outro lado.

</details>

<details>
<summary><b>04 · Segredo nenhum no código</b></summary>

<br/>

Zero credenciais versionadas em 16 repositórios — verificado por varredura.
Chave de reserva no código não é valor padrão: é a senha publicada. Toda rota
protegida aqui é **fechada por omissão** — sem a variável configurada, ela
recusa atender em vez de abrir.

</details>

<br/>

---

<div align="center">

## `//` CANAL

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A0A0A?style=for-the-badge&logo=linkedin&logoColor=D14D29)](https://www.linkedin.com/in/israel-passos-281374336/)
[![GitHub](https://img.shields.io/badge/GitHub-0A0A0A?style=for-the-badge&logo=github&logoColor=F5F0E8)](https://github.com/IsraelDev7)

<br/>

<sub>

*"Às vezes você tem que correr antes de poder andar."*

</sub>

<br/>

<details>
<summary><sub><b>English summary</b></sub></summary>

<br/>
<div align="left">

**Acquisition systems engineering.** I build pages that keep working after they
load — measuring, responding, recording and reporting on their own.

Most of the market ships a beautiful static page. I ship the page **and the
machine behind it**: per-section instrumentation, automated lead response in
seconds, first-party data storage, and a report that reaches the business owner
without them opening any dashboard.

Three clients, six deliveries, two came back for a second project. Client
repositories are private — someone else's code isn't mine to publish, but I'm
happy to walk through any of them.

What I care about: measuring instead of eyeballing, knowing when *not* to reach
for an LLM, and never letting a system fail silently.

</div>
</details>

</div>

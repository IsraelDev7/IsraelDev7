# Israel Passos

**Engenharia de sistemas de aquisição.** Construo páginas que continuam
trabalhando depois que carregam — medindo, respondendo, registrando e
reportando sozinhas.

Smart LABS · Goiânia, Brasil · atendendo Brasil e Reino Unido

---

## O que eu faço

A maior parte do mercado entrega uma peça bonita e estática. Eu entrego a peça
bonita **e a máquina que a atende**: instrumentação por seção, resposta
automática ao lead em segundos, registro próprio dos dados do cliente e um
relatório que chega até ele sem que precise abrir painel nenhum.

Três clientes, seis entregas, dois voltaram para um segundo projeto.

---

## O que o meu código prova

| Projeto | O que ele demonstra |
|---|---|
| **Landing page com relatório diário** <br><sub>consultoria · Reino Unido</sub> | Três funções serverless, OAuth com a API do Google, e-mail + WhatsApp ao lead, e um resumo agendado que chega no WhatsApp do dono às 23h |
| **Site com motor de diagnóstico** <br><sub>paisagismo · Reino Unido</sub> | Sistema especialista determinístico: sete perguntas com peso, nota de 0 a 100 e laudo específico. O lead chega qualificado e a ligação muda de natureza |
| **Link na bio com analytics próprio** <br><sub>saúde estética</sub> | Postgres com migrações versionadas, rota de relatório autenticada, proteção contra *tabnabbing* e limite de taxa por rota |
| [**DevBurger**](https://github.com/IsraelDev7/Dev_buger_final) | E-commerce full-stack: JWT + bcrypt, validação com Yup, upload, Stripe do carrinho ao webhook, painel administrativo |
| [**SmartFit AI Platform**](https://github.com/IsraelDev7/Smart-fitAI) | Monorepo com mobile e web dividindo o mesmo contrato de tipos, Supabase com RLS, cobrança por webhook e CI |
| **Portfólio Smart LABS** | 82 commits com o raciocínio de cada decisão escrito dentro. O método é o produto |

> Os projetos de cliente são privados: código de terceiro não é meu para
> publicar. Posso apresentar qualquer um deles em detalhe numa conversa.

---

## Como eu trabalho

### Medir, não olhar

Screenshot mostra que *parece* certo. Medição mostra que *está* certo. Três
defeitos que só apareceram porque eu medi, e que nenhuma inspeção visual
pegaria:

- Um item flex inflando de 746 para 1002px. `flex: 0 0 52%` fixa a **base**,
  não o **mínimo** — todo item flex nasce com `min-width: auto`, e um texto em
  `nowrap` entrou no `min-content`. A saída foi tirar o elemento do fluxo, não
  `min-width: 0`.
- Uma media query perdendo para uma regra base escrita depois no arquivo.
  Media query não soma especificidade; o desempate é a ordem. A correção foi
  reescrever como `min-width`, não `!important` — regra que não existe no
  telefone não vaza para o telefone.
- Duas animações disputando as mesmas propriedades porque foram **criadas** na
  ordem errada: um `fromTo` sob ScrollTrigger grava o estado inicial no ato da
  criação, não quando dispara.

### Saber quando *não* usar IA

O diagnóstico do site de paisagismo podia ser uma chamada de LLM. Não é — é um
motor de regras com pontuação ponderada, definida junto com o especialista.

Determinístico (a mesma resposta dá sempre o mesmo laudo), auditável linha a
linha por quem entende do assunto, instantâneo e de custo zero. Um modelo de
linguagem seria pior em tudo que importa nesse caso — e poderia alucinar uma
recomendação técnica para alguém que vai contratar um serviço.

Quando IA entra, entra no lugar certo: a régua calcula, o modelo redige.
Decisão determinística, linguagem natural só na apresentação.

### Não deixar o sistema falhar calado

O padrão mais caro que encontro — inclusive em código meu — é o sucesso
presumido: a tela diz "enviado" e nada foi. Já corrigi quatro variações disso:

- `fire and forget` depois de responder, em ambiente serverless, onde o
  container pode ser congelado antes das promessas terminarem
- `mode: 'no-cors'`, que torna a resposta opaca — o código *não consegue*
  saber se funcionou
- `catch` marcando sucesso como reserva
- `console.log` fazendo as vezes de banco de dados

Hoje toda entrega que eu escrevo espera confirmação antes de responder, e o
erro aparece na tela de quem está do outro lado.

### Segredo nenhum no código

Zero credenciais versionadas em 16 repositórios — verificado por varredura.
Chave de reserva no código não é valor padrão: é a senha publicada. Toda rota
protegida aqui é **fechada por omissão** — sem a variável configurada, ela
recusa atender em vez de abrir.

---

## Stack

**Frente** React · Next.js · Vite · TypeScript · Tailwind · GSAP · Three.js / R3F
**Trás** Node · Express · Prisma · Postgres · Supabase · funções serverless
**Integração** Stripe · Google Sheets API · n8n · WhatsApp · OpenAI
**Operação** Vercel · Docker · GitHub Actions · VPS

---

## Contato

[LinkedIn](https://www.linkedin.com/in/israel-passos) · Goiânia, GO

---

<details>
<summary><b>English summary</b></summary>

<br>

**Acquisition systems engineering.** I build pages that keep working after
they load — measuring, responding, recording and reporting on their own.

Most of the market ships a beautiful static page. I ship the page **and the
machine behind it**: per-section instrumentation, automated lead response in
seconds, first-party data storage, and a report that reaches the business
owner without them opening any dashboard.

Three clients, six deliveries, two came back for a second project. Client
repositories are private — someone else's code isn't mine to publish, but I'm
happy to walk through any of them.

What I care about: measuring instead of eyeballing, knowing when *not* to
reach for an LLM, and never letting a system fail silently.

</details>

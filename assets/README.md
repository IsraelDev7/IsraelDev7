# assets — como os SVG do perfil sao gerados

Os visuais do README nao sao imagens exportadas de um editor: sao SVG
gerados por estes tres scripts. Versionar o gerador, e nao so o
resultado, e o que permite mudar um numero da telemetria ou um tom da
paleta sem redesenhar nada.

## Os arquivos

| | |
|---|---|
| `tipo.py` | converte texto em contornos SVG usando a fonte real |
| `gerar_banner.py` | o cabecalho: reator, reticula, ondas e telemetria |
| `gerar_sistemas.py` | o painel dos seis modulos |

## Rodar

```bash
pip install fonttools
# baixe as duas fontes para esta pasta:
#   sg-bold.ttf  -> Space Grotesk 700
#   jb-mono.ttf  -> JetBrains Mono 500
python gerar_banner.py
python gerar_sistemas.py
```

Os `.ttf` ficam fora do versionamento: sao redistribuiveis, mas nao ha
motivo para carregar 180 KB de binario num repositorio de perfil.

## Duas decisoes que valem explicacao

**Texto vira contorno, a fonte nao e embutida.** Um SVG referenciado
por `<img>` no GitHub roda isolado — sem rede, sem script. Embutir a
TTF em base64 funciona e custa ~90 KB por arquivo; converter para
`path` custa alguns kilobytes e tem a mesma fidelidade.

**Animacao em CSS dentro do SVG, nao servico de terceiro.** O GitHub
serve o SVG como imagem e `@keyframes` roda normalmente. Widget
hospedado por outra pessoa quebra sozinho, muda de visual sem aviso e
envelhece mal — e um README de perfil deveria durar mais que isso.
Tudo que anima aqui tambem respeita `prefers-reduced-motion`.

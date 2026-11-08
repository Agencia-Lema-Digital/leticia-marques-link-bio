# Link da bio · Letícia Marques

Página de link da bio do Instagram da Letícia Marques, sócia da Agência Lema Digital.

No ar: https://agencia-lema-digital.github.io/leticia-marques-link-bio/

## Como está organizado

- `index.html`: a página publicada. É um arquivo único, com fotos e fontes embutidas, servido pelo GitHub Pages a partir da branch `main`.
- `fonte/gerar.py`: gera o `index.html`. Textos, links do WhatsApp, cores e estilos ficam todos aqui.
- `fonte/fotos/`: fotos da capa, das polaroides, da faixa de café e os prints dos depoimentos (quadrados de 800 px).
- `fonte/fontes/`: Noto Serif Devanagari Condensed (Light e ExtraLight), Noto Serif Condensed Italic (Light e ExtraLight) e Inter (SemiBold e Bold), todas com licença SIL Open Font License.

## Como editar

1. Altere o texto ou o estilo em `fonte/gerar.py`, ou troque uma foto em `fonte/fotos/` mantendo o mesmo nome.
2. Gere a página de novo:

   ```bash
   python3 fonte/gerar.py
   ```

3. Faça commit e push do `index.html`. O GitHub Pages publica em cerca de um minuto.

Todos os botões levam ao WhatsApp (85) 99220-1110, cada um com uma mensagem pronta diferente.

import base64
import pathlib

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "fontes"
FOTOS = HERE / "fotos"


def b64(path):
    return base64.b64encode(path.read_bytes()).decode("ascii")


def jpg(name):
    return "data:image/jpeg;base64," + b64(FOTOS / name)


FONTES = {
    "F_SERIF": b64(FONTS / "NotoSerifDevanagariCondensed-Light.woff2"),
    "F_FINA": b64(FONTS / "NotoSerifDevaCond-ExtraLight.woff2"),
    "F_IT_FINA": b64(FONTS / "NotoSerifCond-ExtraLightItalic.woff2"),
    "F_IT": b64(FONTS / "NotoSerifCond-LightItalic.woff2"),
    "F_SB": b64(FONTS / "Inter-SemiBold.woff2"),
    "F_B": b64(FONTS / "Inter-Bold.woff2"),
}

WA = "https://wa.me/5585992201110?text="
WA_GERAL = WA + "Ol%C3%A1%2C%20Let%C3%ADcia%21%20Vim%20pelo%20seu%20link%20da%20bio%20e%20quero%20saber%20mais."
WA_AG = WA + "Ol%C3%A1%21%20Vim%20pelo%20link%20da%20bio%20e%20quero%20uma%20proposta%20da%20Ag%C3%AAncia%20Lema%20Digital."
WA_CONS = WA + "Ol%C3%A1%21%20Vim%20pelo%20link%20da%20bio%20e%20quero%20agendar%20uma%20consultoria%20estrat%C3%A9gica."

SETA = '<span class="seta" aria-hidden="true"><svg width="12" height="10" viewBox="0 0 12 10" fill="none"><path d="M0 5h10.5M6.5 1l4 4-4 4" stroke="currentColor" stroke-width="1.3"/></svg></span>'
BRILHO = '<svg class="brilho" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0A12 12 0 0 0 24 12A12 12 0 0 0 12 24A12 12 0 0 0 0 12A12 12 0 0 0 12 0Z"/></svg>'
ZAP = '<svg class="zap" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>'
EMOJIS = '<span class="emo e1" aria-hidden="true">✨</span><span class="emo e2" aria-hidden="true">🌟</span>'
CLIPE = '<svg class="clipe" viewBox="0 0 16 46" aria-hidden="true"><path d="M11 12v22a5 5 0 0 1-10 0V7a4 4 0 0 1 8 0v24a2 2 0 0 1-4 0V12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'

STYLE = """
  @font-face{font-family:'Serif Leve';font-weight:300;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,F_SERIF) format('woff2');}
  @font-face{font-family:'Serif Leve';font-weight:200;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,F_FINA) format('woff2');}
  @font-face{font-family:'Serif Leve';font-weight:200;font-style:italic;font-display:swap;src:url(data:font/woff2;base64,F_IT_FINA) format('woff2');}
  @font-face{font-family:'Serif Leve';font-weight:300;font-style:italic;font-display:swap;src:url(data:font/woff2;base64,F_IT) format('woff2');}
  @font-face{font-family:'Inter';font-weight:600;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,F_SB) format('woff2');}
  @font-face{font-family:'Inter';font-weight:700;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,F_B) format('woff2');}

  :root{
    --manteiga:#fdeec4; --linho:#efeee9; --cafe:#3f362d; --areia:#b0a086;
    --areia-escura:#6f6252; --espresso:#2a231d; --papel:#fbfaf6;
    --linha-cafe:#5e5246;
    --raio-1:6px;
    --margem:24px;
    --f-serif:'Serif Leve','Noto Serif Devanagari',Georgia,serif;
    --f-sans:Inter,Arial,sans-serif;
  }

  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;}
  body{margin:0;background:var(--linho);color:var(--cafe);font-family:var(--f-sans);font-weight:600;-webkit-font-smoothing:antialiased;}
  img{display:block;max-width:100%;}
  a{color:inherit;text-decoration:none;}
  :focus-visible{outline:2px solid var(--manteiga);outline-offset:3px;}
  h1,h2,h3,p,ul{margin:0;}

  .page{max-width:480px;margin:0 auto;background:var(--linho);overflow:hidden;}
  @media (min-width:520px){.page{border-left:1px solid var(--areia);border-right:1px solid var(--areia);}}

  .cafe{background:var(--cafe);color:var(--linho);}
  .rotulo{font-weight:700;font-size:11px;line-height:16px;letter-spacing:0.14em;text-transform:uppercase;}
  i,em{font-style:italic;}

  /* capa */
  .capa{position:relative;padding-top:132px;background:var(--linho);}
  .capa-foto{position:relative;aspect-ratio:4/5;overflow:hidden;
    -webkit-mask-image:linear-gradient(180deg,transparent 0,#000 16%);mask-image:linear-gradient(180deg,transparent 0,#000 16%);}
  .capa-foto img{width:100%;height:100%;object-fit:cover;object-position:50% 14%;animation:assentar 1.8s cubic-bezier(.2,.7,.2,1) both;}
  .capa-foto::after{content:"";position:absolute;inset:auto 0 0 0;height:34%;background:linear-gradient(0deg,var(--cafe) 0,rgba(63,54,45,0.55) 45%,rgba(63,54,45,0) 100%);}
  .capa-titulo{position:absolute;z-index:1;top:30px;left:0;right:0;text-align:center;font-family:var(--f-serif);font-weight:200;color:var(--cafe);}
  .capa-titulo .prazer{display:block;font-style:italic;font-size:26px;line-height:1;color:var(--areia-escura);animation:subir .9s cubic-bezier(.2,.7,.2,1) .15s both;}
  .capa-titulo .nome{position:relative;display:inline-block;margin-top:6px;font-size:clamp(46px,13.6vw,60px);line-height:1;letter-spacing:-0.01em;animation:subir .9s cubic-bezier(.2,.7,.2,1) .3s both;}
  .emo{position:absolute;font-family:'Apple Color Emoji','Segoe UI Emoji','Noto Color Emoji',sans-serif;font-style:normal;font-weight:400;line-height:1;}
  .capa-titulo .e1{right:-24px;top:-8px;font-size:20px;}
  .capa-titulo .e2{right:-36px;top:18px;font-size:13px;}
  .capa-assinatura{position:absolute;z-index:1;left:0;right:0;bottom:22px;text-align:center;color:var(--manteiga);font-size:10px;letter-spacing:0.22em;animation:subir .9s cubic-bezier(.2,.7,.2,1) .5s both;}

  @keyframes subir{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
  @keyframes assentar{from{transform:scale(1.05);}to{transform:none;}}

  /* moldura dos títulos */
  .secao{padding:56px var(--margem);}
  .moldura-wrap{text-align:center;margin-bottom:28px;}
  .moldura{position:relative;display:inline-block;padding:10px 24px 8px;border:1px solid currentColor;font-family:var(--f-serif);font-weight:200;font-size:40px;line-height:1.05;letter-spacing:-0.01em;}
  .cafe .moldura{border-color:var(--areia);}
  .moldura i{font-weight:200;}
  .moldura .e1{right:-13px;top:-13px;font-size:24px;}
  .moldura .e2{left:-9px;bottom:-9px;font-size:16px;}
  .sub{margin-top:10px;font-family:var(--f-serif);font-style:italic;font-weight:300;font-size:19px;line-height:1.2;}

  .texto{font-size:15px;line-height:24px;}
  .texto p + p{margin-top:14px;}
  .cafe .texto{color:#e4e0d6;}
  .cafe .texto b{color:var(--manteiga);font-weight:700;}

  /* sobre */
  .sobre{padding-top:24px;}
  .fatos{margin:24px 0 0;padding:0;list-style:none;border-top:1px solid var(--linha-cafe);}
  .fatos li{padding:14px 0;border-bottom:1px solid var(--linha-cafe);font-size:15px;line-height:22px;color:var(--linho);}
  .fatos .rotulo{display:block;margin-bottom:4px;color:var(--areia);}
  .fe{margin-top:28px;text-align:center;font-family:var(--f-serif);font-style:italic;font-weight:300;font-size:26px;line-height:1.2;color:var(--manteiga);}
  .tira{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:36px;}
  .tira img{width:100%;aspect-ratio:3/4;object-fit:cover;border:4px solid var(--linho);}

  /* barra (botão) */
  .barra{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:50px;padding:0 10px 0 20px;border-radius:var(--raio-1);font-weight:700;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;transition:background-color .2s ease,color .2s ease;}
  .seta{flex-shrink:0;width:30px;height:30px;display:grid;place-items:center;border:1px solid currentColor;border-radius:999px;transition:transform .2s ease;}
  .barra:hover .seta{transform:translateX(3px);}
  .barra-linho{background:var(--linho);color:var(--cafe);}
  .barra-linho:hover{background:var(--manteiga);}
  .barra-cafe{background:var(--cafe);color:var(--linho);}
  .barra-cafe:hover{background:var(--espresso);}
  .sobre .barra{margin-top:28px;}
  .barra-zap{justify-content:center;gap:10px;padding:0 20px;min-height:54px;background:var(--manteiga);color:var(--cafe);border:1px solid var(--cafe);font-size:13px;}
  .barra-zap:hover{background:#fbe4a6;}
  .zap{width:20px;height:20px;fill:currentColor;flex-shrink:0;}

  /* missão */
  .linho{background:var(--linho);color:var(--cafe);}
  .citacao{text-align:center;font-family:var(--f-serif);font-weight:300;font-size:32px;line-height:1.12;}
  .citacao i{font-weight:300;}
  .missao .texto{margin-top:20px;text-align:center;color:var(--areia-escura);}

  /* serviços: cartões de selo */
  .cartoes{display:grid;gap:44px;margin-top:8px;}
  .selo{--r:5px;--s:14px;position:relative;background:var(--papel);color:var(--cafe);padding:30px 22px 24px;
    --m:
      radial-gradient(circle var(--r) at 50% 0,#0000 98%,#000) 0 0/var(--s) 100% round no-repeat,
      radial-gradient(circle var(--r) at 50% 100%,#0000 98%,#000) 0 0/var(--s) 100% round no-repeat,
      radial-gradient(circle var(--r) at 0 50%,#0000 98%,#000) 0 0/100% var(--s) no-repeat round,
      radial-gradient(circle var(--r) at 100% 50%,#0000 98%,#000) 0 0/100% var(--s) no-repeat round;
    -webkit-mask:var(--m);-webkit-mask-composite:source-in;
    mask:var(--m);mask-composite:intersect;}
  .selo-borda{position:absolute;inset:9px;border:1px dashed var(--areia);pointer-events:none;}
  .selo h3{position:relative;max-width:calc(100% - 118px);font-family:var(--f-serif);font-weight:300;font-size:32px;line-height:1;letter-spacing:-0.01em;}
  .selo h3 i{display:block;font-weight:300;}
  .selo .rotulo{position:relative;margin-top:12px;color:var(--areia-escura);max-width:calc(100% - 118px);}
  .selo .texto{position:relative;margin-top:16px;font-size:14px;line-height:22px;color:var(--areia-escura);}
  .selo .barra{position:relative;margin-top:20px;}
  .polaroide{position:absolute;z-index:2;top:-18px;right:6px;width:116px;padding:6px 6px 22px;background:var(--papel);border:1px solid #ddd8cc;transform:rotate(5deg);}
  .polaroide img{width:100%;aspect-ratio:1/1;object-fit:cover;}
  .alt .polaroide{transform:rotate(-4deg);}
  .clipe{position:absolute;top:-16px;left:50%;width:14px;height:40px;margin-left:-7px;color:var(--areia-escura);}
  .cartao{position:relative;}

  /* resolvo */
  .manteiga{background:var(--manteiga);color:var(--cafe);}
  .resolvo{list-style:none;padding:0;margin:0;}
  .resolvo li{display:grid;grid-template-columns:14px 1fr;gap:14px;padding:15px 0;border-top:1px solid rgba(111,98,82,0.3);}
  .resolvo li:first-child{border-top:0;padding-top:4px;}
  .resolvo .brilho{width:12px;height:12px;margin-top:5px;fill:var(--areia-escura);}
  .resolvo b{display:block;font-weight:700;font-size:15px;line-height:21px;}
  .resolvo span{display:block;margin-top:2px;font-size:14px;line-height:20px;color:var(--areia-escura);}

  /* depoimentos: carrossel de ovais em movimento */
  .depoimentos{padding-left:0;padding-right:0;}
  .depoimentos .moldura{max-width:300px;}
  .trilho{overflow-x:auto;scrollbar-width:none;}
  .trilho::-webkit-scrollbar{display:none;}
  .faixa{display:flex;gap:16px;width:max-content;padding:16px 24px 8px;}
  .trilho.anda{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);}
  .anda .faixa{padding-left:0;padding-right:0;animation:deslizar 40s linear infinite;}
  .anda:hover .faixa,.anda:active .faixa{animation-play-state:paused;}
  @keyframes deslizar{from{transform:translateX(0);}to{transform:translateX(calc(-50% - 8px));}}
  .print{flex-shrink:0;width:272px;height:272px;padding:0;border:1px solid var(--areia);border-radius:32px;overflow:hidden;background:var(--papel);cursor:zoom-in;}
  .print img{width:100%;height:100%;object-fit:cover;}
  .dica{margin-top:14px;text-align:center;font-family:var(--f-serif);font-style:italic;font-weight:300;font-size:16px;color:var(--areia-escura);}
  .zoom{width:min(92vw,560px);max-width:none;padding:0;border:0;border-radius:32px;overflow:hidden;background:var(--papel);}
  .zoom::backdrop{background:rgba(42,35,29,0.82);}
  .zoom img{width:100%;}
  .zoom button{position:absolute;top:12px;right:12px;width:36px;height:36px;border:0;border-radius:999px;background:var(--cafe);color:var(--linho);font:700 18px/1 var(--f-sans);cursor:pointer;}

  /* contato */
  .contato .moldura-wrap{margin-bottom:24px;}
  .contatos{display:grid;gap:10px;}

  /* rodapé */
  .rodape{padding:36px var(--margem) 40px;text-align:center;}
  .rodape .rotulo{color:var(--areia);font-size:10px;letter-spacing:0.22em;}
  .rodape .rotulo b{color:var(--linho);}
  .rodape .fe{margin-top:12px;font-size:20px;}
  .rodape small{display:block;margin-top:14px;font-size:11px;line-height:16px;color:var(--areia);}

  @media (max-width:360px){
    .moldura{font-size:34px;padding:8px 16px 6px;}
    .polaroide{width:100px;}
    .selo h3,.selo .rotulo{max-width:calc(100% - 100px);}
  }
  @media (prefers-reduced-motion:reduce){
    html{scroll-behavior:auto;}
    *,*::before,*::after{animation:none !important;transition:none !important;}
  }
"""
for k, v in FONTES.items():
    STYLE = STYLE.replace(k, v)


def moldura(a, b, sub=""):
    s = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<div class="moldura-wrap"><h2 class="moldura">{a} <i>{b}</i>{EMOJIS}</h2>{s}</div>'


DEPOIMENTOS = [
    ("d1.jpg", "Print de depoimento de cliente: Saí total da zona de conforto. Obrigada pelas orientações e apoio. Vocês são excelentes!"),
    ("d2.jpg", "Prints de depoimento de cliente: Lema é de fato uma empresa em plena expansão, com excelentes profissionais."),
    ("d3.jpg", "Print de depoimento de cliente: Estou muito feliz e honrado de poder ter uma equipe extraordinária como essa."),
    ("d4.jpg", "Print de depoimento do cliente Luciano: Estou encantado com tudo que estou vendo, e o site ficou sensacional."),
]
PRINTS = {f: jpg(f) for f, _ in DEPOIMENTOS}


def prints():
    return "".join(
        f'<button type="button" class="print"><img src="{PRINTS[f]}" alt="{alt}"></button>'
        for f, alt in DEPOIMENTOS
    )


SCRIPT = """
<script>
(function(){
  var trilho=document.querySelector('.trilho'), faixa=trilho&&trilho.querySelector('.faixa');
  if(faixa&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
    Array.prototype.slice.call(faixa.children).forEach(function(b){
      var c=b.cloneNode(true); c.setAttribute('aria-hidden','true'); c.tabIndex=-1; c.querySelector('img').alt=''; faixa.appendChild(c);
    });
    trilho.classList.add('anda');
  }
  var d=document.getElementById('zoom'); if(!d||!d.showModal) return;
  var img=d.querySelector('img');
  document.querySelectorAll('.print').forEach(function(b){
    b.addEventListener('click',function(){var i=b.querySelector('img');img.src=i.src;img.alt=i.alt||'Print de depoimento';d.showModal();});
  });
  d.addEventListener('click',function(e){if(e.target===d||e.target.tagName==='BUTTON')d.close();});
})();
</script>
"""


def cartao(foto, alt, titulo, italico, rotulo, texto, cta, link, classe=""):
    return f"""
    <article class="cartao {classe}">
      <figure class="polaroide" style="margin:0">{CLIPE}<img src="{jpg(foto)}" alt="{alt}" loading="lazy"></figure>
      <div class="selo">
        <span class="selo-borda" aria-hidden="true"></span>
        <h3>{titulo} <i>{italico}</i></h3>
        <p class="rotulo">{rotulo}</p>
        <p class="texto">{texto}</p>
        <a class="barra barra-cafe" href="{link}" target="_blank" rel="noopener">{cta}{SETA}</a>
      </div>
    </article>"""


BODY = f"""
<div class="page">

<header class="capa">
  <h1 class="capa-titulo">
    <span class="prazer">Prazer,</span>
    <span class="nome">Letícia Marques{EMOJIS}</span>
  </h1>
  <div class="capa-foto">
    <img src="{jpg('capa.jpg')}" alt="Letícia Marques sorrindo em um corredor claro, segurando um notebook">
  </div>
</header>

<section class="secao cafe sobre">
  {moldura("Sobre", "mim")}
  <div class="texto">
    <p>Sou jornalista de formação e atuo no marketing desde 2019. Comecei no marketing de influência em 2020 e, ainda no mesmo ano, passei a atuar também com marketing de conteúdo.</p>
    <p>Hoje sou sócia da <b>Agência Lema Digital</b> ao lado do meu esposo, parceiro de negócio há 4 anos.</p>
  </div>
  <ul class="fatos">
    <li><span class="rotulo">Antes da agência, trabalhei em</span>Cegás, Companhia Docas do Ceará (Porto do Mucuripe) e CREF5</li>
    <li><span class="rotulo">Vendas geradas no digital</span>Mais de R$ 3 milhões</li>
    <li><span class="rotulo">Empresas atendidas pela agência</span>Mais de 50, no Brasil, nos Estados Unidos e em Portugal</li>
  </ul>
  <p class="fe">Tudo o que construímos é para a glória de Deus.</p>
  <a class="barra barra-zap" href="{WA_GERAL}" target="_blank" rel="noopener">{ZAP}Fale comigo aqui</a>
  <div class="tira" aria-hidden="true">
    <img src="{jpg('s_pampas.jpg')}" alt="" loading="lazy">
    <img src="{jpg('s_livro.jpg')}" alt="" loading="lazy">
    <img src="{jpg('s_pires.jpg')}" alt="" loading="lazy">
  </div>
</section>

<section class="secao linho missao">
  {moldura("Minha", "missão")}
  <p class="citacao">Fazer um marketing de verdade, com estratégia e excelência, <i>para a glória de Deus.</i></p>
  <p class="texto">Resultado e propósito andam juntos. Cada projeto que assinamos carrega esse compromisso: entregar o melhor, com ética e excelência.</p>
</section>

<section class="secao cafe">
  {moldura("Meus", "serviços")}
  <div class="cartoes">
    {cartao("p_notebook.jpg", "Detalhe de Letícia segurando um notebook", "Agência", "Lema Digital", "Para empresas · Sob proposta",
            "Redes sociais, tráfego pago, funis e estruturação comercial para o seu negócio crescer com estratégia.",
            "Quero uma proposta", WA_AG)}
    {cartao("p_latte.jpg", "Xícara de café com leite vista de cima", "Consultoria", "estratégica", "Individual · Sob medida",
            "Diagnóstico, planejamento e estratégia de posicionamento, conteúdo e crescimento para o seu momento.",
            "Quero agendar", WA_CONS, "alt")}
  </div>
</section>

<section class="secao linho depoimentos">
  {moldura("Feedbacks de", "clientes")}
  <div class="trilho">
    <div class="faixa">{prints()}</div>
  </div>
  <p class="dica">toque no print para ampliar</p>
  <dialog class="zoom" id="zoom"><button type="button" aria-label="Fechar">×</button><img src="" alt=""></dialog>
</section>

<section class="secao manteiga">
  {moldura("O que eu", "resolvo")}
  <ul class="resolvo">
    <li>{BRILHO}<p><b>Falta de clareza e posicionamento</b><span>Você sai da confusão para um posicionamento claro.</span></p></li>
    <li>{BRILHO}<p><b>Conteúdo bonito que não vende</b><span>Cada publicação passa a ter um papel no seu negócio.</span></p></li>
    <li>{BRILHO}<p><b>Comercial sem processo</b><span>CRM, scripts e atendimento que transformam contato em venda.</span></p></li>
    <li>{BRILHO}<p><b>Sobrecarga fazendo tudo sozinha</b><span>Uma equipe dedicada executa com você.</span></p></li>
  </ul>
</section>

<section class="secao linho contato">
  {moldura("Entre em", "contato", "é só me chamar no WhatsApp")}
  <div class="contatos">
    <a class="barra barra-zap" href="{WA_GERAL}" target="_blank" rel="noopener">{ZAP}Fale comigo aqui</a>
  </div>
</section>

<footer class="rodape cafe">
  <p class="rotulo"><b>Letícia</b> Marques // Agência Lema Digital</p>
  <p class="fe">Feito para a glória de Deus.</p>
  <small>© 2026 Letícia Marques</small>
</footer>

</div>
""" + SCRIPT

TITLE = "Letícia Marques"
DESC = "Jornalista e sócia da Agência Lema Digital. Marketing com estratégia e excelência, para a glória de Deus."

artifact = f'<meta charset="utf-8">\n<title>{TITLE}</title>\n<style>{STYLE}</style>\n{BODY}'
deploy = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#efeee9">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<style>{STYLE}</style>
</head>
<body>
{BODY}
</body>
</html>
"""

(HERE.parent / "index.html").write_text(deploy, encoding="utf-8")
print("index.html gerado:", len(deploy), "caracteres")

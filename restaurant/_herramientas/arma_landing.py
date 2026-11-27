#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA LANDING DE PIXEL RESTAURANT (2026-11-26, Gonzalo: «haz la landing page así como la de
Pixel Football… porque quiero compartirla»). Una sola plantilla y dos idiomas: escribe
`restaurant/index.html` (español) y `restaurant/en/index.html` (inglés).

La de Pixel Football se viste de transmisión de tele; ésta, de RESTAURANTE: letrero arriba,
la cinta de comandas, el juego en un teléfono y «la carta» con los platillos en pixel art.

    python3 restaurant/_herramientas/arma_landing.py

CUANDO APPLE APRUEBE LA 1.0: poner EN_TIENDA = True (los botones pasan de TestFlight a la
App Store) y volver a correr. La carpeta empieza con «_» para que Jekyll no la publique.
"""
from pathlib import Path

AQUI = Path(__file__).resolve().parent.parent
BASE = "https://gonzoas.github.io/gridiron-legacy-web/restaurant/"
EN_TIENDA = False
APP_STORE = "https://apps.apple.com/app/id6837590282"
TESTFLIGHT = "https://testflight.apple.com/join/qAFP9WFC"
PLATOS = ("quesadilla chilaquiles birria ceviche carbonara bibimbap biryani bourguignon barco_sushi cheeseburger "
          "bao calzone churros_chocolate flan cheesecake banana_split tacos_pastor lomo_saltado pizza_margarita tiramisu").split()

T = {
 "es": dict(
  lang="es", raiz="", otra="en/", titulo="Pixel Restaurant · Tu restaurante, a tu manera",
  desc="Abre tu restaurante, arma el menú con cocinas de todo el mundo y gana las tres estrellas de la Guía Pixel. Sin anuncios ni cuentas. Para iPhone y iPad.",
  abierto="Abierto", estado="Beta abierta en TestFlight" , estado_tienda="Ya en la App Store",
  bajar="Pruébalo", bajar_tienda="Descargar",
  cinta=["Beta abierta en TestFlight", "260 recetas", "10 cocinas del mundo", "Tres estrellas de la Guía Pixel", "100 categorías",
         "Decora mueble por mueble", "Visita a tus amigos", "Sin anuncios · sin cuentas", "Español, inglés y portugués", "Muy pronto en App Store y Google Play"],
  cinta_tienda="Ya en la App Store",
  tag="Sim de restaurante", h1="Tu restaurante,", h1b="a tu manera",
  p="De un localito de barrio a un tres estrellas. Tú pones el nombre, acomodas cada mesa, armas el menú y cuidas a tu equipo.",
  cta="Pruébalo gratis en TestFlight", cta_tienda="Descárgalo gratis", cta2="Míralo por dentro",
  chico="iPhone y iPad · Muy pronto en App Store y Google Play · Sin anuncios ni cuentas",
  chico_tienda="iPhone y iPad · Muy pronto en Google Play · Sin anuncios ni cuentas",
  s1=("El servicio", "Llega la hora pico", "y tu equipo responde",
      "Los clientes llegan, piden y esperan. El chef cocina, el mesero sirve, el garrotero levanta y el lavaplatos lava. Si falta un ingrediente a media hora pico, se nota."),
  v1=[("local", "El local", "Míralo trabajar solo"), ("menu", "El menú", "Doce platillos, cuatro tiempos"), ("almacen", "El almacén", "Surte, siembra y no te quedes sin nada")],
  stats=[("260", "Recetas"), ("10", "Cocinas"), ("100", "Categorías"), ("3", "Estrellas"), ("3", "Idiomas"), ("0", "Anuncios")],
  s2=("Tu local", "Decóralo", "mueble por mueble",
      "Mesas, sillas, barras, estufas, pisos y paredes de diez estilos. Amplía el salón, compra el terreno de al lado y corta el listón cada vez que crece."),
  v2=[("tienda", "La tienda", "Cientos de muebles")],
  lista2=["Ponle nombre, color y logo: el letrero es tuyo", "Contrata chefs, meseros, lavaplatos y garroteros", "Sube cada platillo de nivel y cobra más por él", "Visita los restaurantes de tus amigos con un código"],
  s3=("La Guía Pixel", "Gana tus", "tres estrellas",
      "Atiende rápido, mantén limpio y sube de categoría. Cada estrella llega con su propia escena… y con un rival que no te la quiere dejar. Y cuidado: la Guía también las quita."),
  v3=[("estrella", "La primera", "Tu letrero la presume"), ("rango", "Tu equipo", "La foto de cada rango nuevo")],
  s4=("La carta", "260 recetas", "de 10 cocinas",
      "Mexicana, americana, japonesa, china, italiana, coreana, india, francesa, española y peruana. Todas dibujadas en pixel art."),
  fin="Abre tu restaurante", fin_p="Gratis. Sin anuncios. Sin cuentas ni contraseñas.",
  pie=[("soporte", "Soporte"), ("privacidad", "Privacidad")], pie_txt="Un juego de Gonzalo Álvarez, el de Pixel Football.",
  pf="Pixel Football", alt_video="El restaurante en hora pico"),
 "en": dict(
  lang="en", raiz="../", otra="../", titulo="Pixel Restaurant · Your restaurant, your way",
  desc="Open your restaurant, build a menu from cuisines around the world and earn all three Pixel Guide stars. No ads, no accounts. For iPhone and iPad.",
  abierto="Now serving", estado="Open beta on TestFlight", estado_tienda="Now on the App Store",
  bajar="Try it", bajar_tienda="Download",
  cinta=["Open beta on TestFlight", "260 recipes", "10 world cuisines", "Three Pixel Guide stars", "100 categories",
         "Decorate piece by piece", "Visit your friends", "No ads · no accounts", "English, Spanish and Portuguese", "Coming soon to the App Store and Google Play"],
  cinta_tienda="Now on the App Store",
  tag="Restaurant sim", h1="Your restaurant,", h1b="your way",
  p="From a tiny neighborhood spot to a three-star destination. You name it, place every table, build the menu and look after your crew.",
  cta="Try it free on TestFlight", cta_tienda="Download free", cta2="Take a look inside",
  chico="iPhone and iPad · Coming soon to the App Store and Google Play · No ads, no accounts",
  chico_tienda="iPhone and iPad · Coming soon to Google Play · No ads, no accounts",
  s1=("Service", "Rush hour hits", "and your crew delivers",
      "Customers come in, order and wait. The chef cooks, the waiter serves, the busser clears and the dishwasher washes. Run out of an ingredient mid-rush and you'll feel it."),
  v1=[("local", "The floor", "Watch it run itself"), ("menu", "The menu", "Twelve dishes, four courses"), ("almacen", "The pantry", "Stock up, grow your own, never run dry")],
  stats=[("260", "Recipes"), ("10", "Cuisines"), ("100", "Categories"), ("3", "Stars"), ("3", "Languages"), ("0", "Ads")],
  s2=("Your place", "Decorate it", "piece by piece",
      "Tables, chairs, counters, stoves, floors and walls in ten styles. Expand the dining room, buy the lot next door and cut the ribbon every time it grows."),
  v2=[("tienda", "The shop", "Hundreds of pieces")],
  lista2=["Name, color and logo: the sign is yours", "Hire chefs, waiters, dishwashers and bussers", "Level up each dish and charge more for it", "Visit your friends' restaurants with a code"],
  s3=("The Pixel Guide", "Earn your", "three stars",
      "Serve fast, keep it clean and move up in category. Each star comes with its own scene… and a rival who doesn't want you to have it. Careful: the Guide takes them away, too."),
  v3=[("estrella", "The first one", "Your sign shows it off"), ("rango", "Your crew", "A photo for every new rank")],
  s4=("The menu", "260 recipes", "from 10 cuisines",
      "Mexican, American, Japanese, Chinese, Italian, Korean, Indian, French, Spanish and Peruvian. All drawn in pixel art."),
  fin="Open your restaurant", fin_p="Free. No ads. No accounts or passwords.",
  pie=[("soporte", "Support"), ("privacy", "Privacy")], pie_txt="A game by Gonzalo Álvarez, maker of Pixel Football.",
  pf="Pixel Football", alt_video="The restaurant at rush hour"),
}

CSS = r"""
@font-face{font-family:"Fredoka";src:url("%(r)sassets/Fredoka.ttf");font-weight:300 700;font-display:swap}
:root{--crema:#fdf0c8;--crema2:#f6dc8e;--papel:#fffaf0;--oro:#e8b23a;--oro2:#a8741c;--tinta:#0b1020;--dim:#5d6477;--rojo:#d6332d;--verde:#2f8a55;--borde:#ead9a8}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--crema);scroll-behavior:smooth}
body{font-family:"Fredoka",system-ui,sans-serif;font-weight:500;color:var(--tinta);background:var(--crema);line-height:1.5;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}
img,video{display:block;max-width:100%%}
.pixel{image-rendering:pixelated;image-rendering:crisp-edges}

/* EL LETRERO: la cabecera fija, como la barra de arriba del juego. */
.letrero{position:fixed;top:0;left:0;right:0;z-index:30;height:56px;display:flex;align-items:center;gap:10px;padding:0 12px;background:var(--tinta);border-bottom:4px solid var(--oro);color:#fff}
.letrero .marca{display:flex;align-items:center;gap:10px;font-weight:700;font-size:18px;text-decoration:none;white-space:nowrap}
.letrero .marca img{width:34px;height:34px;border-radius:9px}
.letrero .pastilla{display:flex;align-items:center;gap:8px;padding:5px 12px;border-radius:999px;background:#ffffff1a;font-size:13px;font-weight:600;white-space:nowrap}
.letrero .pastilla i{width:9px;height:9px;border-radius:50%%;background:#5fd08a;box-shadow:0 0 0 4px #5fd08a33}
.letrero .idioma{margin-left:auto;display:flex;border-radius:999px;overflow:hidden;background:#ffffff1a;font-size:13px;font-weight:700}
.letrero .idioma a{padding:7px 12px;text-decoration:none;color:#ffffffb0}
.letrero .idioma a.activo{background:#fff;color:var(--tinta)}
.letrero .get{padding:9px 18px;border-radius:999px;background:var(--oro);color:var(--tinta);font-weight:700;text-decoration:none;box-shadow:0 3px 0 var(--oro2);white-space:nowrap}
/* LA CINTA DE COMANDAS: corre bajo el letrero. */
.cinta{position:fixed;top:56px;left:0;right:0;z-index:29;height:32px;overflow:hidden;background:var(--papel);border-bottom:2px dashed var(--borde);display:flex;align-items:center}
.cinta .corre{display:flex;gap:40px;white-space:nowrap;animation:corre 46s linear infinite;padding-left:40px;font-weight:600;font-size:13px;color:var(--dim)}
.cinta .corre span::before{content:"★";color:var(--rojo);margin-right:10px;font-size:11px}
@keyframes corre{to{transform:translateX(-50%%)}}
@media (prefers-reduced-motion:reduce){.cinta .corre,.carta .fila{animation:none}}

.boton{display:inline-flex;align-items:center;justify-content:center;min-height:58px;padding:14px 28px;border-radius:18px;font-weight:700;font-size:18px;text-decoration:none;transition:transform .12s ease}
.boton:active{transform:translateY(3px)}
.boton.primario{background:var(--oro);color:var(--tinta);box-shadow:0 5px 0 var(--oro2),0 14px 30px #e8b23a55}
.boton.secundario{background:#fff;color:var(--tinta);border:3px solid var(--borde);box-shadow:0 5px 0 var(--borde)}

/* EL HÉROE: el título a la izquierda y el juego corriendo en un teléfono. */
.heroe{position:relative;padding:calc(88px + clamp(28px,6vw,70px)) 20px clamp(40px,7vw,80px);background:radial-gradient(1200px 600px at 80%% 10%%,#ffe08a 0,#ffd866 30%%,transparent 70%%),linear-gradient(#fdf0c8,#f6dc8e)}
.heroe .dentro{max-width:1080px;margin:0 auto;display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(24px,5vw,60px);align-items:center}
.tag{display:inline-block;padding:6px 14px;border-radius:999px;background:var(--tinta);color:#fff;font-size:13px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
h1{font-size:clamp(44px,8.4vw,92px);line-height:.98;font-weight:700;margin:16px 0 18px;letter-spacing:-.01em}
h1 span{display:block;color:var(--rojo)}
.heroe p{font-size:clamp(18px,2.2vw,22px);color:#2a2f40;max-width:30em}
.ctas{display:flex;flex-wrap:wrap;gap:14px;margin:26px 0 16px}
.heroe small{display:block;color:var(--dim);font-size:14px;font-weight:500}
.tel{justify-self:center;width:min(300px,72vw);padding:9px;border-radius:38px;background:var(--tinta);box-shadow:0 30px 60px #0b102055,0 0 0 2px #ffffff40 inset;transform:rotate(2.5deg)}
.tel video,.tel img{width:100%%;aspect-ratio:6/13;object-fit:cover;border-radius:30px;background:#cfe9b5}

.secc{max-width:1080px;margin:0 auto;padding:clamp(54px,8vw,96px) 20px}
.etq{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--oro2)}
.etq::before{content:"";width:22px;height:4px;border-radius:2px;background:var(--oro)}
h2{font-size:clamp(34px,5.6vw,60px);line-height:1.02;font-weight:700;margin:10px 0 14px}
h2 span{display:block;color:var(--rojo)}
.sub{font-size:clamp(17px,2vw,20px);color:#2a2f40;max-width:34em}
.pantallas{display:grid;grid-template-columns:repeat(3,minmax(0,264px));justify-content:space-between;gap:clamp(14px,3vw,28px);margin-top:36px}
.pantalla{background:#fff;border:3px solid var(--borde);border-radius:26px;padding:10px 10px 14px;box-shadow:0 8px 0 var(--borde)}
.pantalla img{width:100%%;aspect-ratio:6/13;object-fit:cover;object-position:top;border-radius:18px}
.pantalla b{display:block;margin-top:12px;font-size:19px;font-weight:700}
.pantalla span{display:block;color:var(--dim);font-size:15px;line-height:1.3}
.stats{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:40px}
.stats div{background:var(--tinta);color:#fff;border-radius:18px;padding:16px 8px;text-align:center}
.stats b{display:block;font-size:clamp(26px,4vw,40px);line-height:1;color:var(--oro)}
.stats span{font-size:13px;font-weight:600;color:#ffffffb8}
.blanca{background:var(--papel);border-top:2px dashed var(--borde);border-bottom:2px dashed var(--borde)}
.dos{display:grid;grid-template-columns:1fr minmax(0,300px);gap:clamp(24px,5vw,64px);align-items:center}
.dos ul{list-style:none;margin-top:22px;display:grid;gap:10px}
.dos li{display:flex;gap:12px;align-items:flex-start;font-size:18px;font-weight:600}
.dos li::before{content:"✓";flex:none;width:28px;height:28px;border-radius:9px;background:var(--verde);color:#fff;display:grid;place-items:center;font-size:16px}
/* LA GUÍA: la sección de noche, con las estrellas rojas. */
.guia{background:var(--tinta);color:#fff}
.guia .sub{color:#ffffffc8}.guia .etq{color:var(--oro)}
.guia h2 span{color:#ff5a52}
.estrellas{font-size:clamp(44px,8vw,84px);line-height:1;color:#ff3b33;letter-spacing:.08em;text-shadow:0 0 30px #ff3b3366}
.guia .pantallas{grid-template-columns:repeat(2,minmax(0,264px));justify-content:start}
.guia .pantalla{background:#161d33;border-color:#2a3550;box-shadow:0 8px 0 #060912}
.guia .pantalla span{color:#ffffff9c}
/* LA CARTA: los platillos en pixel art, corriendo en dos filas. */
.carta{overflow:hidden;padding:26px 0 0}
.carta .fila{display:flex;gap:22px;width:max-content;animation:corre 60s linear infinite;margin-bottom:22px}
.carta .fila.b{animation-direction:reverse;animation-duration:70s}
.carta .plato{width:96px;height:96px;flex:none;border-radius:50%%;background:#fff;border:3px solid var(--borde);box-shadow:0 5px 0 var(--borde);display:grid;place-items:center}
.carta .plato img{width:64px;height:64px}
.fin{text-align:center;padding:clamp(60px,9vw,110px) 20px;background:linear-gradient(#f6dc8e,#f2a93b)}
.fin img{width:112px;height:112px;border-radius:26px;margin:0 auto 22px;box-shadow:0 12px 30px #0b102040}
.fin h2{margin-bottom:8px}.fin p{font-size:19px;margin-bottom:26px;color:#2a2f40}
footer{background:var(--tinta);color:#ffffffa8;text-align:center;padding:34px 20px 44px;font-size:14px}
footer nav{display:flex;flex-wrap:wrap;gap:8px 22px;justify-content:center;margin-bottom:14px}
footer a{color:#fff;font-weight:600;text-decoration:none}
footer a:hover{color:var(--oro)}
.aparece{opacity:0;transform:translateY(18px);transition:opacity .5s ease,transform .5s ease}
.aparece.visto{opacity:1;transform:none}
@media (max-width:820px){
  .heroe .dentro{grid-template-columns:1fr;text-align:center}
  .heroe p{margin:0 auto}.ctas{justify-content:center}
  .tel{transform:none;margin-top:10px}
  .pantallas{grid-template-columns:repeat(3,58vw);justify-content:start;overflow-x:auto;scroll-snap-type:x mandatory;margin:30px -20px 0;padding:0 20px 14px;-webkit-overflow-scrolling:touch}
  .pantalla{scroll-snap-align:center}
  .guia .pantallas{grid-template-columns:repeat(2,58vw)}
  .stats{grid-template-columns:repeat(3,1fr)}
  .dos{grid-template-columns:1fr}.dos .pantalla{max-width:300px;margin:0 auto}
  .letrero .pastilla{display:none}
}
@media (max-width:420px){.letrero .marca span{display:none}.boton{width:100%%}}
"""


def pantalla(t, clave, nombre, pie):
    return ('<div class="pantalla aparece"><img src="%sassets/%s/%s.jpg" alt="%s" loading="lazy" width="540" height="1170">'
            '<b>%s</b><span>%s</span></div>') % (t["raiz"], t["lang"], clave, nombre, nombre, pie)


def seccion(s):
    return '<span class="etq aparece">%s</span><h2 class="aparece">%s<span>%s</span></h2><p class="sub aparece">%s</p>' % s


def pagina(t):
    r = t["raiz"]
    url = BASE + ("" if t["lang"] == "es" else "en/")
    cta_url = APP_STORE if EN_TIENDA else TESTFLIGHT
    cinta = list(t["cinta"])
    if EN_TIENDA:
        cinta[0] = t["cinta_tienda"]
        cinta = cinta[:-1]
    spans = "".join("<span>%s</span>" % c for c in cinta)
    fila_a = "".join('<div class="plato"><img class="pixel" src="%sassets/platos/%s.png" alt="" loading="lazy" width="64" height="64"></div>' % (r, p) for p in PLATOS)
    fila_b = "".join('<div class="plato"><img class="pixel" src="%sassets/platos/%s.png" alt="" loading="lazy" width="64" height="64"></div>' % (r, p) for p in reversed(PLATOS))
    es_activa, en_activa = (' class="activo" aria-current="page"', "") if t["lang"] == "es" else ("", ' class="activo" aria-current="page"')
    liga_es, liga_en = ("./", "en/") if t["lang"] == "es" else ("../", "./")
    pie = "".join('<a href="%s%s">%s</a>' % (r, a, b) for a, b in t["pie"])
    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{desc}">
{meta_app}<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}assets/og.jpg">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1020">
<link rel="icon" href="{r}assets/icono.png">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="preload" href="{r}assets/Fredoka.ttf" as="font" type="font/ttf" crossorigin>
<link rel="alternate" hreflang="es" href="{base}">
<link rel="alternate" hreflang="en" href="{base}en/">
<link rel="alternate" hreflang="x-default" href="{base}">
<style>{css}</style>
</head>
<body>
<header class="letrero">
 <a class="marca" href="./"><img src="{r}assets/icono.png" alt=""><span>Pixel Restaurant</span></a>
 <div class="pastilla"><i></i>{abierto} · {estado}</div>
 <nav class="idioma" aria-label="Idioma / Language"><a href="{liga_es}"{es_activa} hreflang="es" lang="es">ES</a><a href="{liga_en}"{en_activa} hreflang="en" lang="en">EN</a></nav>
 <a class="get" href="{cta_url}">{bajar}</a>
</header>
<div class="cinta" aria-hidden="true"><div class="corre">{spans}{spans}</div></div>

<section class="heroe"><div class="dentro">
 <div>
  <span class="tag">{tag}</span>
  <h1>{h1}<span>{h1b}</span></h1>
  <p>{p}</p>
  <div class="ctas"><a class="boton primario" href="{cta_url}">{cta}</a><a class="boton secundario" href="#servicio">{cta2}</a></div>
  <small>{chico}</small>
 </div>
 <div class="tel"><video autoplay muted loop playsinline preload="metadata" poster="{r}assets/local_poster.jpg" aria-label="{alt_video}"><source src="{r}assets/local.mp4" type="video/mp4"></video></div>
</div></section>

<section class="secc" id="servicio">
 {s1}
 <div class="pantallas">{v1}</div>
 <div class="stats aparece">{stats}</div>
</section>

<div class="blanca"><section class="secc"><div class="dos">
 <div>{s2}<ul class="aparece">{lista2}</ul></div>
 {v2}
</div></section></div>

<div class="guia"><section class="secc">
 <div class="estrellas aparece" aria-hidden="true">★★★</div>
 {s3}
 <div class="pantallas">{v3}</div>
</section></div>

<section class="secc" style="padding-bottom:0">{s4}</section>
<div class="carta" aria-hidden="true"><div class="fila">{fila_a}{fila_a}</div><div class="fila b">{fila_b}{fila_b}</div></div>

<section class="fin">
 <img src="{r}assets/icono.png" alt="Pixel Restaurant" width="112" height="112">
 <h2>{fin}</h2><p>{fin_p}</p>
 <a class="boton primario" style="background:var(--tinta);color:#fff;box-shadow:0 5px 0 #000,0 14px 30px #0b102055" href="{cta_url}">{cta}</a>
</section>

<footer>
 <nav>{pie}<a href="https://gonzoas.github.io/gridiron-legacy-web/{pf_liga}">{pf}</a></nav>
 {pie_txt}
</footer>
<script>
// Las secciones entran al llegar a ellas.
(function(){{var els=document.querySelectorAll('.aparece');
 if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('visto')}});return}}
 var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('visto');io.unobserve(e.target)}}}})}},{{threshold:.1}});
 els.forEach(function(e){{io.observe(e)}});}})();
// El video sólo corre cuando se ve.
(function(){{var v=document.querySelector('video');if(!v||!('IntersectionObserver' in window))return;
 new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{var p=v.play();if(p&&p.catch)p.catch(function(){{}})}}else{{v.pause()}}}})}},{{threshold:.2}}).observe(v);}})();
</script>
</body>
</html>
""".format(lang=t["lang"], titulo=t["titulo"], desc=t["desc"], base=BASE, url=url, r=r, css=CSS % {"r": r},
           meta_app='<meta name="apple-itunes-app" content="app-id=6837590282">\n' if EN_TIENDA else "",
           abierto=t["abierto"], estado=t["estado_tienda"] if EN_TIENDA else t["estado"],
           liga_es=liga_es, liga_en=liga_en, es_activa=es_activa, en_activa=en_activa, cta_url=cta_url,
           bajar=t["bajar_tienda"] if EN_TIENDA else t["bajar"], spans=spans, tag=t["tag"], h1=t["h1"], h1b=t["h1b"], p=t["p"],
           cta=t["cta_tienda"] if EN_TIENDA else t["cta"], cta2=t["cta2"], chico=t["chico_tienda"] if EN_TIENDA else t["chico"],
           alt_video=t["alt_video"], s1=seccion(t["s1"]), v1="".join(pantalla(t, *v) for v in t["v1"]),
           stats="".join("<div><b>%s</b><span>%s</span></div>" % s for s in t["stats"]),
           s2=seccion(t["s2"]), lista2="".join("<li>%s</li>" % x for x in t["lista2"]), v2="".join(pantalla(t, *v) for v in t["v2"]),
           s3=seccion(t["s3"]), v3="".join(pantalla(t, *v) for v in t["v3"]), s4=seccion(t["s4"]),
           fila_a=fila_a, fila_b=fila_b, fin=t["fin"], fin_p=t["fin_p"], pie=pie, pie_txt=t["pie_txt"], pf=t["pf"],
           pf_liga="" if t["lang"] == "es" else "en/")


def main():
    (AQUI / "index.html").write_text(pagina(T["es"]), encoding="utf-8")
    (AQUI / "en").mkdir(exist_ok=True)
    (AQUI / "en" / "index.html").write_text(pagina(T["en"]), encoding="utf-8")
    print("restaurant/index.html y restaurant/en/index.html")


if __name__ == "__main__":
    main()

"""Génère la carte de partage (assets/og-banner.jpg, 1200 × 630) et l'icône pour téléphone
(assets/apple-touch-icon.png, 180 × 180).

Usage : python3 outils/carte.py   (depuis la racine du dépôt). Nécessite Node et Playwright.
La carte est l'image affichée quand on partage le lien du site (LinkedIn, WhatsApp, e-mail).
Textes : nom, TITRE_CV et adresse du site, repris de outils/generer.py. Image : l'œuvre Signum Cruci.
"""
import base64
import html
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generer as g  # noqa: E402

RACINE = g.RACINE
e = html.escape


def donnees(chemin, mime):
    with open(os.path.join(RACINE, chemin), "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


POLICE = donnees("assets/fonts/schibsted-grotesk-latin.woff2", "font/woff2")
CSS = (f'@font-face{{font-family:"S";src:url("{POLICE}") format("woff2");font-weight:400 900}}'
       '*{box-sizing:border-box;margin:0;padding:0}body{font-family:"S",sans-serif;background:#0b1320;color:#fff}')

CARTE = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><style>{CSS}
body{{width:1200px;height:630px;display:grid;grid-template-columns:1fr 470px}}
.t{{padding:64px 56px 56px 72px;display:flex;flex-direction:column}}
.barre{{width:64px;height:6px;background:#5fc9c4;margin-bottom:34px}}
h1{{font-size:118px;font-weight:900;line-height:.92;letter-spacing:-.04em}}
.p{{margin-top:30px;font-size:34px;font-weight:800;color:#5fc9c4}}
.d{{margin-top:12px;font-size:28px;line-height:1.3;color:#d5dae2;max-width:17em}}
.u{{margin-top:auto;font-size:24px;color:#aab1bd}}
.i{{background:url("{donnees('assets/oeuvres/signum-cruci-1.webp', 'image/webp')}") center/cover}}
</style></head><body>
<div class="t"><div class="barre"></div><h1>Léa<br>Rybak</h1><p class="p">Portfolio</p>
<p class="d">{e(g.TITRE_CV)}</p><p class="u">{e(g.URL.replace("https://", "").rstrip("/"))}</p></div>
<div class="i"></div></body></html>"""

ICONE = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}
body{{width:180px;height:180px;display:grid;place-items:center}}
b{{font-size:84px;font-weight:900;letter-spacing:-.04em}}i{{display:inline-block;width:14px;height:14px;border-radius:50%;background:#5fc9c4;margin-left:5px}}
</style></head><body><b>LR<i></i></b></body></html>"""

SCRIPT = """const {chromium}=require('playwright');(async()=>{const [h,o,w,ht,t]=process.argv.slice(1);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+ht}});
await p.goto('file://'+h);await p.evaluate(()=>document.fonts.ready);
await p.screenshot(t==='jpeg'?{path:o,type:'jpeg',quality:88}:{path:o});await b.close()})();"""


def capturer(contenu, sortie, largeur, hauteur, genre):
    with tempfile.TemporaryDirectory() as dossier:
        source = os.path.join(dossier, "page.html")
        with open(source, "w", encoding="utf-8") as f:
            f.write(contenu)
        subprocess.run(["node", "-e", SCRIPT, source, os.path.join(RACINE, sortie), str(largeur), str(hauteur), genre], check=True)
    print("écrit", sortie)


if __name__ == "__main__":
    capturer(CARTE, "assets/og-banner.jpg", 1200, 630, "jpeg")
    capturer(ICONE, "assets/apple-touch-icon.png", 180, 180, "png")

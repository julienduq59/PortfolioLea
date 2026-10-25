"""Génère le CV PDF d'une page (A4) de Léa Rybak, avec le QR code du portfolio.

Usage : python3 outils/cv.py   (depuis la racine du dépôt)
Nécessite segno (pip install segno), Node et Playwright.

- assets/cv-lea-rybak.pdf : version publique, liée depuis le site. Coordonnées : e-mail et
  portfolio seulement, sans téléphone ni adresse.
- prive/cv-lea-rybak-avec-telephone.pdf : version pour les candidatures, avec le numéro lu dans
  prive/telephone.txt. Le dossier prive/ n'est pas versionné : rien de ce qu'il contient n'est publié.

Les données (formation, expériences…) viennent de outils/generer.py : le site et le CV disent
toujours la même chose. Ne rien inventer.
"""
import base64
import html
import os
import subprocess
import sys
import tempfile

import segno

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generer as g  # noqa: E402

RACINE = g.RACINE
e = html.escape


def police(nom):
    with open(os.path.join(RACINE, "assets/fonts", nom), "rb") as f:
        return "data:font/woff2;base64," + base64.b64encode(f.read()).decode()


def qr_svg():
    return segno.make(g.URL, error="m").svg_inline(scale=1, border=0, dark="#0b1320", omitsize=True)


def bloc(date, titre, detail):
    det = f'<span class="det">{e(detail)}</span>' if detail else ""
    return f'<li><span class="date">{e(date)}</span><span><b>{e(titre)}</b>{det}</span></li>'


def cv_html(telephone=""):
    url_courte = g.URL.replace("https://", "").rstrip("/")
    coord = [f'<a href="mailto:{g.MAIL}">{g.MAIL}</a>']
    if telephone:
        coord.append(e(telephone))
    coord.append(f'<a href="{g.URL}">{url_courte}</a>')
    coord.append("Permis B")

    culture = []
    if all(c["roles"] == g.CULTURE[0]["roles"] for c in g.CULTURE):
        # Mêmes missions pour chaque édition : on les écrit une seule fois.
        editions = "".join(
            f'<li><span class="date">{e(c["date"])}</span><span><b>{e(c["titre"])}</b>'
            f'<span class="det">{e(c["lieu"])} · œuvre exposée : <i>{e(c["oeuvre"])}</i></span></span></li>'
            for c in g.CULTURE)
        roles = "".join(f"<li>{e(r)}</li>" for r in g.CULTURE[0]["roles"])
        culture.append(f"""<ul class="liste">{editions}</ul>
        <div class="poste"><h3>Missions sur chaque édition</h3><ul>{roles}</ul></div>""")
    else:
        for c in g.CULTURE:
            roles = "".join(f"<li>{e(r)}</li>" for r in c["roles"])
            culture.append(f"""<div class="poste">
        <p class="date">{e(c["date"])}</p>
        <h3>{e(c["titre"])} <span class="lieu">· {e(c["lieu"])}</span></h3>
        <ul>{roles}</ul>
        <p class="oeuvre">Œuvre exposée : <i>{e(c["oeuvre"])}</i></p>
      </div>""")

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV · Léa Rybak</title>
<meta name="author" content="Léa Rybak">
<style>
@font-face{{font-family:"Schibsted Grotesk";src:url("{police("schibsted-grotesk-latin.woff2")}") format("woff2");font-weight:400 900;font-style:normal}}
@font-face{{font-family:"Schibsted Grotesk";src:url("{police("schibsted-grotesk-italic-latin.woff2")}") format("woff2");font-weight:400 900;font-style:italic}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:210mm;height:297mm}}
body{{font-family:"Schibsted Grotesk",Arial,sans-serif;font-size:9pt;line-height:1.4;color:#17202e;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
a{{color:inherit;text-decoration:none}}
.page{{width:210mm;height:297mm;overflow:hidden;display:grid;grid-template-rows:auto minmax(0,1fr)}}
.entete{{background:#0b1320;color:#fff;padding:9mm 13mm 8mm;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8mm;align-items:center}}
h1{{font-size:30pt;font-weight:900;letter-spacing:-.03em;line-height:1}}
.cible{{display:inline-block;margin-top:3mm;border:1px solid #fff;border-radius:2.5mm;padding:1.3mm 3.2mm;font-weight:700;font-size:10.5pt}}
.titre{{margin-top:2.5mm;font-size:10pt;color:#d6dbe4}}
.coord{{margin-top:3mm;display:flex;flex-wrap:wrap;gap:1mm 6mm;font-size:9pt;font-weight:500}}
.qr{{background:#fff;color:#0b1320;padding:3.5mm;border-radius:2mm;display:grid;grid-template-columns:27mm 25mm;gap:3.5mm;align-items:center}}
.qr svg{{display:block;width:27mm;height:27mm}}
.qr p{{font-size:9pt;line-height:1.3;font-weight:800}}
.qr p span{{display:block;font-weight:400;color:#4b5468;font-size:8pt;margin-top:1mm}}
.corps{{display:grid;grid-template-columns:minmax(0,1.62fr) minmax(0,1fr);gap:9mm;padding:7mm 13mm 8mm;min-height:0}}
.colonne{{display:flex;flex-direction:column;justify-content:space-between;gap:5mm;min-height:0;overflow:hidden}}
h2{{font-size:11.5pt;font-weight:800;color:#0b1320;border-bottom:1.4pt solid #0b1320;padding-bottom:1.2mm;margin-bottom:3mm;letter-spacing:-.005em}}
.note{{color:#4b5468;font-size:8.6pt;margin:-1mm 0 3mm}}
.profil p{{font-size:9.4pt}}
.poste+.poste{{margin-top:3.5mm}}
.liste+.poste{{margin-top:3mm}}
.poste .date{{font-size:8.4pt;color:#4b5468}}
.poste h3{{font-size:10.6pt;font-weight:800;line-height:1.3}}
.poste h3 .lieu{{font-weight:500;color:#4b5468}}
.poste ul{{margin:1.2mm 0 0 4.2mm}}
.poste ul li+li{{margin-top:.6mm}}
.poste .oeuvre{{margin-top:1.2mm;color:#4b5468;font-size:8.6pt}}
.liste{{list-style:none;display:flex;flex-direction:column;gap:1.9mm}}
.liste li{{display:grid;grid-template-columns:19mm minmax(0,1fr);gap:3mm}}
.colonne-cote .liste li{{grid-template-columns:minmax(0,1fr);gap:.2mm}}
.liste .date{{color:#4b5468;font-size:8.4pt;padding-top:.35mm;font-variant-numeric:tabular-nums}}
.liste b{{font-weight:700;display:block;line-height:1.3}}
.liste .det{{display:block;color:#4b5468;font-size:8.6pt}}
</style>
</head>
<body>
<div class="page">
  <header class="entete">
    <div>
      <h1>Léa Rybak</h1>
      <p class="cible">À la recherche d'un poste dans le secteur culturel</p>
      <p class="titre">Master exposition-production des œuvres d'art contemporain, Université de Lille</p>
      <p class="coord">{"".join(f"<span>{c}</span>" for c in coord)}</p>
    </div>
    <div class="qr">{qr_svg()}<p>Mon portfolio<span>Scannez pour voir mes œuvres, expositions et parcours</span></p></div>
  </header>
  <div class="corps">
    <div class="colonne">
      <section class="profil">
        <h2>Profil</h2>
        <p>Expérience de la conception, de la communication, du montage et de la médiation d'expositions, et de l'accueil des publics. Pratique artistique : installation, sculpture, performance, photographie.</p>
      </section>
      <section>
        <h2>Expériences dans le secteur culturel</h2>
        <p class="note">STARTER : l'exposition des étudiantes et étudiants en licence d'arts plastiques de l'Université de Lille.</p>
        {"".join(culture)}
      </section>
      <section>
        <h2>Accueil, animation, spectacle et vente</h2>
        <ul class="liste">{"".join(bloc(a, t, d) for a, t, d in g.EXPERIENCES)}</ul>
      </section>
    </div>
    <div class="colonne colonne-cote">
      <section>
        <h2>Formation</h2>
        <ul class="liste">{"".join(bloc(a, t, d) for a, t, d in g.FORMATIONS)}</ul>
      </section>
      <section>
        <h2>Compétences</h2>
        <ul class="liste">{"".join(bloc(a, t, d) for a, t, d in g.COMPETENCES)}</ul>
      </section>
      <section>
        <h2>Pratiques</h2>
        <ul class="liste">{"".join(bloc(a, t, d) for a, t, d in g.PRATIQUES)}</ul>
      </section>
    </div>
  </div>
</div>
</body>
</html>
"""


def imprimer(contenu, sortie):
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    with tempfile.TemporaryDirectory() as dossier:
        source = os.path.join(dossier, "cv.html")
        with open(source, "w", encoding="utf-8") as f:
            f.write(contenu)
        subprocess.run(["node", os.path.join(RACINE, "outils/imprimer_cv.js"), source, sortie], check=True)
    print("écrit", os.path.relpath(sortie, RACINE))


if __name__ == "__main__":
    imprimer(cv_html(), os.path.join(RACINE, g.CV))
    fichier_tel = os.path.join(RACINE, "prive/telephone.txt")
    if os.path.exists(fichier_tel):
        with open(fichier_tel, encoding="utf-8") as f:
            tel = f.read().strip()
        imprimer(cv_html(tel), os.path.join(RACINE, "prive/cv-lea-rybak-avec-telephone.pdf"))

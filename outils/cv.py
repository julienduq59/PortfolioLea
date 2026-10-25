"""Génère le CV PDF d'une page (A4) de Léa Rybak, avec le QR code du portfolio.

Usage : python3 outils/cv.py   (depuis la racine du dépôt)
Nécessite segno (pip install segno), Node et Playwright.

La mise en page reproduit le CV de Léa d'octobre 2026 (Liberation Sans, titres bleus #2e74b5,
photo ronde en haut à droite). Le QR code vers le portfolio est placé dans l'en-tête, à gauche
de la photo. Les données (formation, compétences, expériences…) viennent de outils/generer.py.

Deux versions, toutes deux avec la photo de Léa (outils/photo-lea.jpg) :
- assets/cv-lea-rybak.pdf : la version publique, liée depuis le site, sans téléphone.
- prive/CV-Lea-Rybak.pdf : le CV complet pour les candidatures, avec le téléphone lu dans
  prive/telephone.txt. Le dossier prive/ n'est pas versionné : rien de ce qu'il contient n'est publié.
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
PHOTO = os.path.join(RACINE, "outils/photo-lea.jpg")
POLICES = "/usr/share/fonts/truetype/liberation"
e = html.escape

# Icônes des coordonnées, comme sur le CV de Léa (24 × 24)
ICONES = {
    "tel": "M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57"
           ".55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2"
           " 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z",
    "mail": "M4 5h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z",
    "lieu": "M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5"
            "s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z",
}


def police(fichier, poids, style):
    with open(os.path.join(POLICES, fichier), "rb") as f:
        donnees = base64.b64encode(f.read()).decode()
    return (f'@font-face{{font-family:"CV";src:url("data:font/ttf;base64,{donnees}") format("truetype");'
            f"font-weight:{poids};font-style:{style}}}")


def image_base64(chemin):
    with open(chemin, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def qr_svg():
    return segno.make(g.URL, error="m").svg_inline(scale=1, border=0, dark="#000000", omitsize=True)


def icone(nom):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{ICONES[nom]}"/></svg>'


def ligne(date, titre, lieu, details):
    return (f'<div class="ligne"><div class="date">{e(date)}</div><div class="contenu">'
            f'<div class="titre">{titre}</div><div class="lieu">{e(lieu)}</div>{details}</div></div>')


def formation(f):
    note = f'<div class="note">{e(f["note"])}</div>' if f["note"] else ""
    return ligne(f["date"], f'<b>{e(f["titre"])}</b>', f["lieu"], note)


def experience(x):
    titre = f'<b>{e(x["titre"])}</b>' + (f' – {e(x["precision"])}' if x["precision"] else "")
    missions = '<ul class="puces">' + "".join(f"<li>{e(m)}</li>" for m in x["missions"]) + "</ul>"
    return ligne(x["date"], titre, x["lieu"], missions)


def cv_html(telephone="", photo=""):
    url_courte = g.URL.replace("https://", "").rstrip("/")
    coord = []
    if telephone:
        coord.append(f'<li>{icone("tel")}<span>{e(telephone)}</span></li>')
    coord.append(f'<li>{icone("mail")}<a href="mailto:{g.MAIL}">{g.MAIL}</a></li>')
    coord.append(f'<li>{icone("lieu")}<span>{e(g.VILLE)}</span></li>')
    image = f'<img class="photo" src="{image_base64(photo)}" alt="">' if photo else ""
    competences = "".join(f"<h3>{e(t)}</h3>" for t, _ in g.COMPETENCES) + "".join(
        '<ul class="puces">' + "".join(f"<li>{e(c)}</li>" for c in liste) + "</ul>" for _, liste in g.COMPETENCES)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CV Léa Rybak</title>
<meta name="author" content="Léa Rybak">
<style>
{police("LiberationSans-Regular.ttf", 400, "normal")}
{police("LiberationSans-Bold.ttf", 700, "normal")}
{police("LiberationSans-Italic.ttf", 400, "italic")}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:210mm;height:297mm}}
body{{font-family:"CV",Arial,sans-serif;color:#000;font-size:11px;line-height:1.3;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
a{{color:inherit;text-decoration:none}}
.page{{position:relative;width:210mm;height:297mm;overflow:hidden;padding:26px 40px 0}}
.tete{{position:relative;height:144px}}
h1{{font-size:23px;font-weight:700;line-height:1.15}}
.coord{{list-style:none;margin-top:7px}}
.coord li{{display:flex;align-items:center;font-size:11.5px;line-height:17px}}
.coord svg{{width:12px;height:12px;flex:none;margin-right:10px;fill:#000}}
.photo{{position:absolute;top:0;right:0;width:136px;height:136px;border-radius:50%;object-fit:cover}}
.qr{{position:absolute;top:24px;right:{"154" if photo else "0"}px;display:flex;align-items:center;gap:12px;text-align:right}}
.qr svg{{display:block;width:92px;height:92px}}
.qr p{{font-size:10.5px;line-height:1.4}}
.qr b{{display:block;color:#2e74b5;font-size:11.5px}}
.qr .url{{display:block;font-size:9.5px}}
.accroche{{text-align:right;font-size:13px;font-weight:700;line-height:1.15}}
h2{{font-size:13px;font-weight:400;color:#2e74b5;line-height:1.15;border-bottom:1px solid #2e74b5;padding-bottom:1px;margin:13px 0 7px}}
.ligne{{display:grid;grid-template-columns:84px minmax(0,1fr)}}
.ligne+.ligne{{margin-top:8px}}
.date{{font-size:9px;line-height:1.15;padding-top:3px}}
.titre{{font-size:12.5px;line-height:17px}}
.lieu{{font-style:italic;font-size:11px;line-height:15px}}
.note{{padding-left:22px;font-size:11px;line-height:14px}}
.puces{{list-style:none}}
.puces li::before{{content:"•";display:inline-block;width:13px}}
.contenu .puces{{padding-left:22px}}
.contenu .puces li{{line-height:14.67px}}
.competences{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:14px;padding:1px 0 2px}}
.competences h3{{font-size:11.5px;font-weight:700;line-height:15px}}
.competences .puces{{padding-left:4px}}
.competences .puces li{{font-size:10.5px;line-height:16px}}
.interets{{font-size:11px}}
</style>
</head>
<body>
<div class="page">
  <header class="tete">
    <h1>Léa RYBAK</h1>
    <ul class="coord">{"".join(coord)}</ul>
    <div class="qr"><p><b>Mon portfolio</b>Œuvres, expositions et parcours<a class="url" href="{g.URL}">{url_courte}</a></p>{qr_svg()}</div>
    {image}
  </header>
  <p class="accroche">{e(g.TITRE_CV)}</p>
  <section>
    <h2>Formation</h2>
    {"".join(formation(f) for f in g.DIPLOMES + g.CERTIFICATS)}
  </section>
  <section>
    <h2>Compétences</h2>
    <div class="competences">{competences}</div>
  </section>
  <section>
    <h2>Expériences professionnelles</h2>
    {"".join(experience(x) for x in g.EXPERIENCES)}
  </section>
  <section>
    <h2>Centres d’intérêt</h2>
    <p class="interets">{e(g.CENTRES_INTERET)}</p>
  </section>
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
    imprimer(cv_html(photo=PHOTO), os.path.join(RACINE, g.CV))
    fichier_tel = os.path.join(RACINE, "prive/telephone.txt")
    if os.path.exists(fichier_tel):
        with open(fichier_tel, encoding="utf-8") as f:
            tel = f.read().strip()
        imprimer(cv_html(tel, PHOTO), os.path.join(RACINE, "prive/CV-Lea-Rybak.pdf"))

"""Génère les pages HTML du portfolio de Léa Rybak à partir des données ci-dessous.

Usage : python3 outils/generer.py   (depuis la racine du dépôt)
Tous les textes viennent du CV et du portfolio V1 de Léa ; ne rien inventer.
"""
import html
import json
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "20261025-3"  # à changer à chaque modification de styles.css ou site.js
MAIL = "lea.rybak@outlook.fr"
URL = "https://julienduq59.github.io/PortfolioLea/"

e = html.escape


def dims(nom):
    with open(os.path.join(RACINE, "assets/oeuvres", nom + ".webp.json"), encoding="utf-8") as f:
        d = json.load(f)
    return d["largeur"], d["hauteur"]


def img(nom, alt, taille="(max-width: 820px) 100vw, 50vw", charge="lazy"):
    w, h = dims(nom)
    attr = 'fetchpriority="high"' if charge == "eager" else 'loading="lazy" decoding="async"'
    return (f'<img src="assets/oeuvres/{nom}-640.webp" srcset="assets/oeuvres/{nom}-640.webp 640w, '
            f'assets/oeuvres/{nom}.webp {w}w" sizes="{taille}" width="{w}" height="{h}" alt="{e(alt)}" {attr}>')


def voir(nom, alt, legende, **kw):
    return (f'<a class="voir" href="assets/oeuvres/{nom}.webp" data-legende="{e(legende)}" '
            f'aria-label="Agrandir : {e(alt)}">{img(nom, alt, **kw)}</a>')


# ---------------------------------------------------------------- Œuvres
# Textes : portfolio V1 de Léa, orthographe corrigée (corrections listées dans VALIDATION.md).
OEUVRES = [
    dict(id="signum-cruci", titre="Signum Cruci", annee="2024", matiere="Bois, objets divers", dim="160 × 140 cm",
         lieu="La Condition Publique, Roubaix · exposition STARTER 10",
         images=[("signum-cruci-1", "Signum Cruci : grande croix murale recouverte d'objets anciens, assiettes, tasses, figurines et bibelots."),
                 ("signum-cruci-2", "Signum Cruci vue de côté, accrochée au mur blanc de l'exposition.")],
         texte=["Évoque la sécularisation de la société contemporaine en réinterprétant des objets religieux tels que la croix, emblème catholique. Cette démarche artistique explore les liens profonds entre l'art et le sacré, soulignant la perte de la sacralité dans notre époque. La croix, chargée d'éléments démodés, sert de support à une forme de souvenir sacré, révélant une histoire personnelle à travers ces artefacts."]),
    dict(id="cliche", titre="Cliché", annee="2023", matiere="Photographie argentique", dim="",
         lieu="La Chaufferie de La Tossée, Tourcoing · exposition STARTER 9",
         images=[("cliche-1", "Cliché : photographie argentique en noir et blanc des quais de Seine, la tour Eiffel au loin."),
                 ("cliche-accrochage", "Cliché encadré, accroché sur un mur de briques à La Chaufferie de La Tossée.")],
         texte=["Véritable cliché parisien, où le bon vivre à la française vient réveiller bien-être et souvenir. Une bulle de plénitude, une pause, un moment d'évasion, on s'accorde le droit de pénétrer le paysage avant de repartir dans le monde réel."]),
    dict(id="corail", titre="Sans titre", annee="2024", matiere="Plâtre", dim="", lieu="",
         images=[("corail-1", "Branches de corail rouge en plâtre dressées au sol d'une salle d'exposition, avec leurs ombres."),
                 ("corail-2", "Gros plan sur une branche de corail rouge en plâtre.")],
         texte=["Méduse décapitée, son sang se fige en corail au contact de la mer.",
                "Créature née d'un viol, le corail rouge s'élève et donne à Méduse la reconnaissance qui lui est due. Victime et non bourreau, la femme au débit du monstre est ainsi mise en évidence."]),
    dict(id="trophees", titre="Mes trophées de chasse", annee="2024", matiere="Bois et plâtre", dim="", lieu="",
         images=[("trophees-1", "Mes trophées de chasse : trois formes en plâtre blanc sur des écussons bleu, rose et orange, accrochées au mur."),
                 ("trophees-2", "Vue de l'accrochage des trophées sur un mur blanc."),
                 ("trophees-3", "Détail des écussons rose et orange.")],
         texte=["Quand le chasseur devient chasseuse, la femme vengeresse expose son butin.",
                "Le corps masculin devient objet et suscite la convoitise malgré la fragilité et le temps qui s'attaque d'ores et déjà à ces restes humains."]),
    dict(id="chevelure", titre="Sans titre", annee="2024", matiere="Laine", dim="", lieu="",
         images=[("laine-1", "Longue chevelure de laine verte suspendue au mur."),
                 ("laine-2", "La chevelure de laine verte vue de loin, sur le mur blanc."),
                 ("laine-3", "Détail des mèches de laine verte.")],
         texte=["Tout le monde la cherche, tout le monde pense l'avoir trouvée.",
                "Exposée tel un artefact dans un cabinet de curiosités, cette chevelure de sirène invoque les croyances et les légendes autour du mythe de la créature, mais aussi les vidéos populaires et les photographies amatrices de cette femme tentatrice."]),
    dict(id="poussiere", titre="Poussière d'étoile", annee="2024", matiere="Poussière accumulée, bois, lumière", dim="", lieu="",
         images=[("poussiere-1", "Poussière d'étoile : cadre posé au sol, rempli de poussière, éclairé par une lampe rasante."),
                 ("poussiere-2", "Vue d'ensemble du cadre de poussière et de sa lampe."),
                 ("poussiere-3", "Gros plan sur la surface de poussière, semblable à un paysage lunaire.")],
         texte=["Dans un parterre formé de poussière et de moutons de poussière, où prolifèrent bactéries et restes humains, se dessine un paysage lunaire."]),
    dict(id="porc", titre="Sans titre", annee="2024", matiere="Plastique, chaîne, crochet", dim="", lieu="",
         images=[("porc-1", "Forme de porc emballée dans du film alimentaire, suspendue à un crochet dans une salle d'exposition.")],
         texte=["Dissimuler pour mieux révéler.",
                "Porc minutieusement emballé dans du film alimentaire, suspendu par un crochet de boucher. Et c'est l'abattoir."]),
    dict(id="plantes", titre="Sans titre", annee="2024", matiere="Préservatifs, eau, plantes", dim="", lieu="",
         images=[("plantes-1", "Une douzaine de préservatifs remplis d'eau et de plantes, accrochés en grille sur un mur.")],
         texte=["Dans un futur proche, les êtres humains ont des rapports sexuels avec les plantes. Une fois la semence expulsée, elle est conservée dans le réservoir afin de faire féconder une nouvelle espèce de plante."]),
    dict(id="marche", titre="Projet collectif, sans titre", annee="2023", matiere="Performance", dim="", lieu="",
         images=[("marche-1", "Performance : des participants vêtus de draps blancs marchent sur une allée."),
                 ("marche-2", "Silhouettes drapées de blanc pendant la marche collective.")],
         texte=["Inspirée des processions religieuses, cette marche collective anonyme est ponctuée d'un son de cloche, et invite qui le souhaite à rejoindre la marche.",
                "Partager la marche, entrer dans le collectif et ne former qu'un."]),
    dict(id="sorciere", titre="Projet collectif, sans titre", annee="2023", matiere="Restitution de performance, vidéo", dim="", lieu="",
         images=[("sorciere-1", "Installation de restitution : un abri de tissus violets surmonté de feuillages, une vidéo projetée à l'intérieur."),
                 ("sorciere-2", "L'abri de tissus bleus et violets de la restitution, vu de face.")],
         texte=["La performance souligne la place marginale de l'artiste en arborant la tenue de la sorcière.",
                "Figure marginalisée ou a contrario idolâtrée, la figure de l'artiste parmi un public désintéressé est mise de côté et repoussée. Tout comme la sorcière, le créatif ou la créative a du mal à trouver sa place et à s'imposer en tant que telle auprès de ses pairs."]),
    dict(id="carreaux", titre="Sans titre", annee="2023", matiere="Carreaux de porcelaine, peinture · restitution de workshop", dim="", lieu="",
         images=[("carreaux-1", "Carreaux de porcelaine peints de motifs colorés inspirés du zellige, posés au sol."),
                 ("carreaux-2", "Vue de l'ensemble des carreaux peints au sol de la salle."),
                 ("carreaux-3", "Détail d'un carreau peint aux motifs géométriques.")],
         texte=["Vernaculaire à Tourcoing.",
                "Inspirés de l'Institut du monde arabe de Tourcoing, ces carreaux blancs viennent évoquer le passé nautique du lieu, et la peinture semblable au zellige marocain rappelle la nouvelle identité du bâtiment. Une odeur de javel enveloppe les carreaux."]),
    dict(id="savon", titre="Sans titre", annee="2023", matiere="Étagère en bois, mousse de savon", dim="", lieu="",
         images=[("savon-1", "Petites étagères en bois fixées au mur, couvertes de mousse de savon blanche."),
                 ("savon-2", "Les étagères et la mousse de savon vues de plus loin.")],
         texte=["Laisser vivre la matière.",
                "Déposée ainsi, cette mousse de savon aussi banale que quotidienne est déplacée au statut d'œuvre d'art. Bien qu'éphémère, le spectateur profite d'un spectacle de douceur, où la mousse coule, crépite et ne laisse derrière elle qu'une flaque d'eau."]),
    dict(id="cendre", titre="Sans titre", annee="2022", matiere="Cendre de bois, sel, clou, fil de fer", dim="", lieu="",
         images=[("cendre-1", "Sculpture organique faite de cendre de bois et de sel, en forme de feuillages entrelacés, accrochée au mur."),
                 ("cendre-2", "Vue d'ensemble de la sculpture en cendre sur le mur blanc.")],
         texte=["Place à la matière.",
                "Le bois est ici transformé en une matière nouvelle. De cette matière naît une sculpture organique et sensible."]),
]
PAR_ID = {o["id"]: o for o in OEUVRES}

# Formation : portfolio V1 et CV de Léa.
FORMATIONS = [("2024-2026", "Master exposition-production des œuvres d'art contemporain", "Université de Lille"),
              ("2021-2024", "Licence arts plastiques et visuels", "Université de Lille, pôle arts plastiques de Tourcoing"),
              ("2021", "Baccalauréat, mention très bien", "Lycée Baudelaire, Roubaix · spécialité humanités, philosophie, littérature et théâtre"),
              ("2021", "BAFA", "Cemea"),
              ("2018", "PSC1", "")]

# Expériences : CV de Léa (février 2024).
EXPERIENCES = [("Depuis 2021", "Animatrice", "Mairie de Croix, MJC de Croix, Planète Aventure… Accueils collectifs de mineurs et colonies de vacances."),
               ("2023", "Hôtesse", "Casino Barrière, Lille · placement des spectateurs et organisation de salle lors d'événements et de spectacles."),
               ("2023", "Comédienne", "Parc Koezio, Villeneuve-d'Ascq · événement d'Halloween, 30 et 31 octobre."),
               ("2023", "Conseillère de vente", "Coupe du monde de rugby, stade Pierre-Mauroy · mise en place de la boutique, caisse, gestion des stocks."),
               ("2023", "Conseillère de vente", "La Fée Maraboutée, Lille · renfort pour la braderie."),
               ("2023", "Service", "Top Action, pour le traiteur Yanka · service, mise en place, gestion du bar.")]

PAGES = [("index.html", "Accueil"), ("parcours.html", "Parcours"), ("oeuvres.html", "Œuvres"),
         ("expositions.html", "Expositions"), ("photographie.html", "Photographie")]

FLECHE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
SOLEIL = '<svg class="soleil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>'
LUNE = '<svg class="lune" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>'


def cartel(o, lien=True):
    lignes = [f'<b class="t">{e(o["titre"])}</b>{o["annee"]}', f'<span>{e(o["matiere"])}</span>']
    if o["dim"]:
        lignes.append(f'<span>{e(o["dim"])}</span>')
    if o["lieu"]:
        lignes.append(f'<span>{e(o["lieu"])}</span>')
    if lien:
        lignes.append(f'<a href="oeuvres.html#{o["id"]}">Lire le texte</a>')
    return '<figcaption class="cartel">' + "".join(lignes) + "</figcaption>"


def legende(o):
    return f'{o["titre"]}, {o["annee"]}. {o["matiere"]}.'


def page(fichier, titre, description, corps):
    nav = []
    for f, nom in PAGES[1:]:
        cur = ' aria-current="page"' if f == fichier else ""
        nav.append(f'<a href="{f}"{cur}>{nom}</a>')
    titre_complet = "Léa Rybak · Arts plastiques et visuels" if fichier == "index.html" else f"{titre} · Léa Rybak"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titre_complet)}</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#0b1320">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Léa Rybak">
<meta property="og:title" content="{e(titre_complet)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{URL}{"" if fichier == "index.html" else fichier}">
<meta property="og:image" content="{URL}assets/og-banner.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{URL}{"" if fichier == "index.html" else fichier}">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="preload" href="assets/fonts/schibsted-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/styles.css?v={VERSION}">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
</head>
<body>
<a class="saut" href="#contenu">Aller au contenu</a>
<header class="entete"><div class="g">
  <a class="signature" href="./"{' aria-current="page"' if fichier == "index.html" else ""}>Léa Rybak</a>
  <nav class="plan" aria-label="Navigation principale">
    {"".join(nav)}
    <button class="theme" type="button" aria-label="Changer de thème">{SOLEIL}{LUNE}</button>
  </nav>
</div></header>
<main id="contenu">
{corps}
</main>
<section class="contact" id="contact" aria-labelledby="titre-contact"><div class="g">
  <h2 id="titre-contact">Me contacter</h2>
  <p class="mail"><a href="mailto:{MAIL}">{MAIL}</a><button class="copier" type="button" data-copier="{MAIL}">Copier</button></p>
</div></section>
<footer class="pied"><div class="g"><span>Léa Rybak · Arts plastiques et visuels</span><span>Portfolio 2026</span></div></footer>
<dialog class="visionneuse" aria-label="Œuvre agrandie">
  <div class="barre"><button class="fermer" type="button">Fermer</button></div>
  <div class="scene"><img alt=""></div>
  <p></p>
</dialog>
<script src="assets/site.js?v={VERSION}" defer></script>
</body>
</html>
"""


def accueil():
    sc = PAR_ID["signum-cruci"]
    selection = ["corail", "trophees", "chevelure", "poussiere"]
    fig = []
    for i in selection:
        o = PAR_ID[i]
        n, alt = o["images"][0]
        fig.append(f'<figure class="oeuvre">{voir(n, alt, legende(o), taille="(max-width: 820px) 100vw, 45vw")}{cartel(o)}</figure>')
    n, alt = sc["images"][0]
    return f"""<section class="entree"><div class="g">
  <div class="texte">
    <h1 class="nom">Léa<br>Rybak</h1>
    <p class="recherche">À la recherche d'un poste dans le secteur culturel</p>
    <p>Détentrice d'une licence arts plastiques et visuels, je travaille avec différents médiums et procédés techniques : installation, sculpture, performance, photographie.</p>
    <p class="doux">Dans une pluralité de médiums, on trouve une pluralité de sujets et de sources d'inspiration. Féminisme, mythologie, religion ou faits de société : autant de situations qui donnent naissance à des œuvres variées.</p>
    <p class="doux">Master exposition-production des œuvres d'art contemporain, Université de Lille (2024-2026).</p>
    <a class="lien-fort" href="parcours.html">Voir mon parcours {FLECHE}</a>
  </div>
  <figure class="oeuvre">{voir(n, alt, legende(sc), taille="(max-width: 820px) 100vw, 45vw", charge="eager")}{cartel(sc)}</figure>
</div></section>

<section class="salle" aria-labelledby="titre-formation"><div class="g">
  <h2 class="titre-salle" id="titre-formation">Parcours</h2>
  <div class="chapeau"><p>Une formation en arts plastiques puis en production d'expositions d'art contemporain.</p></div>
  <ol class="experiences">{"".join(f'<li><span class="an">{a}</span><b>{e(t)}</b><span class="det">{e(d)}</span></li>' for a, t, d in FORMATIONS[:3])}</ol>
</div></section>

<section class="salle" aria-labelledby="titre-experiences"><div class="g">
  <h2 class="titre-salle" id="titre-experiences">Expériences professionnelles</h2>
  <div class="chapeau"><p>Animation, accueil, spectacle et vente : une solide expérience des publics.</p></div>
  <ol class="experiences">{"".join(f'<li><span class="an">{a}</span><b>{e(t)}</b><span class="det">{e(d)}</span></li>' for a, t, d in EXPERIENCES)}</ol>
  <a class="lien-fort" href="parcours.html">Voir tout le parcours {FLECHE}</a>
</div></section>

<section class="salle" aria-labelledby="titre-selection"><div class="g">
  <h2 class="titre-salle" id="titre-selection">Sélection</h2>
  <div class="chapeau"><p>Sculpture, installation et matière : quatre œuvres de 2024.</p></div>
  <div class="accrochage">{"".join(fig)}</div>
  <a class="lien-fort" href="oeuvres.html">Voir les treize œuvres {FLECHE}</a>
</div></section>

<section class="salle" aria-labelledby="titre-expos"><div class="g">
  <h2 class="titre-salle" id="titre-expos">Expositions</h2>
  <div class="chapeau"><p>Conception, communication, montage et médiation de STARTER 10 à La Condition Publique de Roubaix (2024) et de STARTER 9 à La Chaufferie de La Tossée de Tourcoing (2023).</p></div>
  <a class="lien-fort" href="expositions.html">Voir les expositions {FLECHE}</a>
</div></section>
"""


def page_oeuvres():
    plan = []
    fiches = []
    for o in OEUVRES:
        n, alt = o["images"][0]
        w, h = dims(n)
        plan.append(f'<li><a href="#{o["id"]}"><img src="assets/oeuvres/{n}-640.webp" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">'
                    f'<i>{e(o["titre"])}</i><span>{o["annee"]} · {e(o["matiere"])}</span></a></li>')
        planches = "".join(voir(nn, aa, legende(o), taille="(max-width: 820px) 100vw, 55vw" if k == 0 else "(max-width: 820px) 50vw, 28vw")
                           for k, (nn, aa) in enumerate(o["images"]))
        meta = [f'<b>{o["annee"]}</b>', e(o["matiere"])]
        if o["dim"]:
            meta.append(e(o["dim"]))
        if o["lieu"]:
            meta.append(e(o["lieu"]))
        recit = "".join(f'<p{" class=\"accroche\"" if (k == 0 and len(o["texte"]) > 1 and len(t) < 80) else ""}>{e(t)}</p>' for k, t in enumerate(o["texte"]))
        fiches.append(f"""<article class="salle fiche-salle" id="{o["id"]}" aria-labelledby="t-{o["id"]}"><div class="g"><div class="fiche">
  <div class="planches">{planches}</div>
  <div class="texte-oeuvre"><div class="cartel">
    <h2 id="t-{o["id"]}">{e(o["titre"])}</h2>
    <p class="meta">{"<br>".join(meta)}</p>
    <div class="recit">{recit}</div>
  </div></div>
</div></div></article>""")
    return f"""<section class="salle" aria-labelledby="titre-oeuvres"><div class="g">
  <h1 class="titre-salle" id="titre-oeuvres">Œuvres</h1>
  <div class="chapeau"><p>Installation, sculpture, performance et photographie, de 2022 à 2024. Touchez une œuvre pour l'agrandir.</p></div>
  <ol class="plan-salle">{"".join(plan)}</ol>
</div></section>
{"".join(fiches)}
"""


def page_expositions():
    return f"""<section class="salle" aria-labelledby="titre-expositions"><div class="g">
  <h1 class="titre-salle" id="titre-expositions">Expositions</h1>
  <div class="chapeau"><p>Deux éditions de STARTER, l'exposition des étudiantes et étudiants en licence d'arts plastiques de l'Université de Lille. J'en ai assuré la conception, la communication, le montage et la médiation, tout en y exposant une œuvre.</p></div>
  <div class="expos">
    <article class="expo">
      <div>
        <h2>STARTER 10</h2>
        <p class="lieu">2024 · La Condition Publique, Roubaix</p>
        <ul>
          <li>Conception de l'exposition.</li>
          <li>Communication : dossier de presse, communiqué de presse, gestion des réseaux sociaux.</li>
          <li>Montage de l'exposition.</li>
          <li>Médiation : accueil du public et visites.</li>
          <li>Œuvre exposée : <a href="oeuvres.html#signum-cruci"><i>Signum Cruci</i></a>.</li>
        </ul>
      </div>
      <div class="visuels">
        <figure class="large" style="margin:0">{voir("starter10-vue", "Vue de l'exposition STARTER 10 à La Condition Publique : grandes salles blanches, œuvres accrochées aux murs.", "STARTER 10, La Condition Publique, Roubaix, 2024.", taille="(max-width: 820px) 100vw, 55vw")}<figcaption>Vue de l'exposition à La Condition Publique.</figcaption></figure>
      </div>
    </article>
    <article class="expo">
      <div>
        <h2>STARTER 9</h2>
        <p class="lieu">Mars 2023 · La Chaufferie de La Tossée, Tourcoing</p>
        <ul>
          <li>Conception de l'exposition : une trentaine d'exposants et autant d'œuvres, de la photographie à la sculpture, en passant par la peinture et l'installation.</li>
          <li>Communication : dossier de presse, communiqué de presse, gestion des réseaux sociaux.</li>
          <li>Montage de l'exposition.</li>
          <li>Médiation : accueil du public et visites.</li>
          <li>Œuvre exposée : <a href="oeuvres.html#cliche"><i>Cliché</i></a>.</li>
        </ul>
      </div>
      <div class="visuels">
        <figure style="margin:0">{voir("starter9-dossier", "Couverture du dossier de presse de STARTER 9.", "Dossier de presse de STARTER 9, 2023.", taille="(max-width: 820px) 50vw, 27vw")}<figcaption>Dossier de presse.</figcaption></figure>
        <figure style="margin:0">{voir("starter9-plan", "Plan de l'exposition STARTER 9 à La Chaufferie de La Tossée.", "Plan de l'exposition STARTER 9, 2023.", taille="(max-width: 820px) 50vw, 27vw")}<figcaption>Plan de l'exposition.</figcaption></figure>
      </div>
    </article>
  </div>
</div></section>
"""


def page_photographie():
    photos = [("argentique-1", "Photographie argentique en noir et blanc : un objet circulaire vu de près, à la texture usée."),
              ("argentique-2", "Photographie argentique en noir et blanc : pêcheurs sur une plage, sous un ciel gris."),
              ("argentique-3", "Photographie argentique en noir et blanc : façade ornée d'un immeuble ancien vue en contre-plongée."),
              ("argentique-4", "Photographie argentique en noir et blanc : un homme au pied de tours vitrées."),
              ("argentique-5", "Photographie argentique en noir et blanc : la tour Eiffel."),
              ("argentique-6", "Photographie argentique en noir et blanc : une passerelle au-dessus de la Seine."),
              ("argentique-7", "Photographie argentique en noir et blanc : deux chaises longues face au ciel.")]
    figs = "".join(f'<figure>{voir(n, a, "Photographie argentique.", taille="(max-width: 600px) 100vw, 33vw")}</figure>' for n, a in photos)
    return f"""<section class="salle" aria-labelledby="titre-photo"><div class="g">
  <h1 class="titre-salle" id="titre-photo">Photographie</h1>
  <div class="chapeau"><p>Photographie argentique, pratiquée à la MJC de Croix de 2019 à 2022. Voir aussi l'œuvre <a href="oeuvres.html#cliche"><i>Cliché</i></a>, exposée à STARTER 9.</p></div>
  <div class="tirage">{figs}</div>
</div></section>
"""


def page_parcours():
    def liste(items):
        return "".join(f'<li><span class="an">{a}</span><span>{t}{f"<span class=det>{d}</span>" if d else ""}</span></li>' for a, t, d in items)
    pratiques = [("2019-2022", "Photographie argentique", "MJC de Croix"),
                 ("2008-2023", "Danse contemporaine et modern jazz", "MJC de Croix"),
                 ("2019", "Photographe bénévole", "Gala de danse de la MJC de Croix")]
    return f"""<section class="salle" aria-labelledby="titre-parcours"><div class="g">
  <h1 class="titre-salle" id="titre-parcours">Parcours</h1>
  <div class="chapeau"><p>Une formation en arts plastiques et en production d'expositions, et une solide expérience de l'accueil des publics.</p></div>
  <div class="parcours">
    <div><h2>Formation</h2><ol>{liste(FORMATIONS)}</ol></div>
    <div id="experiences"><h2>Expériences professionnelles</h2><ol>{liste(EXPERIENCES)}</ol></div>
    <div><h2>Pratiques</h2><ol>{liste(pratiques)}</ol></div>
    <div><h2>Compétences</h2><ul>
      <li><span class="an">Langue</span><span>Anglais, niveau B1<span class="det">Certification CLES B1</span></span></li>
      <li><span class="an">Permis</span><span>Permis B (2022)</span></li>
      <li><span class="an">Qualités</span><span>Dynamique et responsable, autonome, ponctuelle, bienveillante, à l'écoute, aime le travail en équipe</span></li>
    </ul></div>
  </div>
</div></section>
"""


def page_404():
    return f"""<section class="salle perdu"><div class="g">
  <h1 class="titre-salle">Cette salle n'existe pas</h1>
  <div class="chapeau"><p>La page demandée est introuvable. Elle a peut-être été déplacée.</p></div>
  <a class="lien-fort" href="./">Revenir à l'accueil {FLECHE}</a>
</div></section>
"""


SORTIES = {
    "index.html": ("Accueil", "Portfolio de Léa Rybak, artiste plasticienne : installation, sculpture, performance et photographie. Master exposition-production des œuvres d'art contemporain, Université de Lille.", accueil),
    "oeuvres.html": ("Œuvres", "Les œuvres de Léa Rybak de 2022 à 2024 : Signum Cruci, Cliché, Mes trophées de chasse, Poussière d'étoile et d'autres.", page_oeuvres),
    "expositions.html": ("Expositions", "STARTER 10 à La Condition Publique de Roubaix et STARTER 9 à La Chaufferie de La Tossée de Tourcoing : conception, communication et médiation.", page_expositions),
    "photographie.html": ("Photographie", "Photographies argentiques de Léa Rybak.", page_photographie),
    "parcours.html": ("Parcours", "Formation, expériences et compétences de Léa Rybak.", page_parcours),
    "404.html": ("Page introuvable", "Page introuvable.", page_404),
}

if __name__ == "__main__":
    for fichier, (titre, desc, fn) in SORTIES.items():
        with open(os.path.join(RACINE, fichier), "w", encoding="utf-8") as f:
            f.write(page(fichier, titre, desc, fn()))
        print("écrit", fichier)

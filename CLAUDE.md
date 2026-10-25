# Portfolio de Léa Rybak

Site statique (HTML/CSS/JS) publié avec GitHub Pages depuis la branche `main` du dépôt julienduq59/PortfolioLea (choix de Julien, 25/10/2026) :
https://julienduq59.github.io/PortfolioLea/
Projet mené avec Julien Duquesne (julienduq59@gmail.com). Le site de Julien sert de référence
technique (julienduq59/PortfolioDuquesneJulien), mais ce site a son propre design.
Ne jamais publier ce site dans le dépôt du portfolio de Julien (PortfolioDuquesneJulien).

## Langue

Toujours répondre à Julien en français : messages, questions, réflexion affichée, descriptions
des commandes, commits.

## Règles absolues

- **Ne jamais inventer de données.** Tout le contenu vient du CV de Léa (février 2024) ou de son
  portfolio V1 (PDF Canva, 2026). En cas de doute, poser la question.
- **Léa valide le contenu avant toute mise en ligne.** Voir `VALIDATION.md`.
- Pas de téléphone ni d'adresse postale en ligne : ni sur le site, ni dans le CV public, ni dans le dépôt
  (public). Seul l'e-mail est affiché. Le numéro reste dans `prive/` (non versionné).
- **Pas de statistiques ni de suivi des visites** (choix de Julien, 25/10/2026) : ni GoatCounter,
  ni alertes ntfy, ni liens `?ref=`. Le site de Julien en a, celui de Léa non.
- Aucun document d'identité, aucune donnée sensible.
- Pas de photos d'enfants (gala de danse de la MJC de Croix) sans l'accord des familles.
- Toujours montrer un aperçu avant de publier une modification de design.

## Objectif

Le site sert à trouver un travail (secteur arts et culture). Ordre voulu par Julien
(25/10/2026) : d'abord le parcours (formation), puis les expériences professionnelles,
puis les œuvres, les expositions et le reste.

**Menu fixe, identique sur toutes les pages (demande de Julien) : Parcours, Expériences, Œuvres,
Expositions, Photographie.** Il est défini une seule fois (`PAGES` dans `outils/generer.py`) :
ne jamais changer cet ordre sans demande explicite.

## Fonctionnement

- Les pages HTML sont **générées** par `outils/generer.py` (`python3 outils/generer.py` depuis
  la racine). Modifier les textes et la liste des œuvres dans ce script, pas dans les fichiers HTML.
- Pages, dans l'ordre du menu : `index.html`, `parcours.html`, `experiences.html`, `oeuvres.html`,
  `expositions.html`, `photographie.html`, plus `404.html`.
- Design : direction « L'exposition », choisie par Julien sur aperçu. Une œuvre accrochée en grand
  par salle, un cartel de musée sous chaque œuvre. Couleurs reprises du portfolio V1 : bleu nuit
  `#0b1320` et blanc. Thème sombre par défaut, thème clair selon l'appareil ou via le bouton.
  Police Schibsted Grotesk auto-hébergée (`assets/fonts/`).
- Images : WebP dans `assets/oeuvres/`, en deux tailles (`nom.webp`, jusqu'à 1400 px, et
  `nom-640.webp`), avec leur origine dans `nom.webp.json`.
- Cache : `styles.css` et `site.js` sont chargés avec `?v=AAAAMMJJ`. À chaque modification de
  ces fichiers, changer `VERSION` dans `outils/generer.py`, puis régénérer les pages.
- Visionneuse : tout lien `a.voir` ouvre l'image en grand dans un `<dialog>` (Échap pour fermer).
- Fiche pour Google : données structurées `Person` (JSON-LD) sur l'accueil, dans `FICHE_GOOGLE`.
- **CV PDF** (A4, une page, avec QR code vers le portfolio) : `python3 outils/cv.py` depuis la racine
  (nécessite `pip install segno`, Node et Playwright). Il reprend les données de `outils/generer.py`.
  - `assets/cv-lea-rybak.pdf` : version publique, liée depuis l'accueil et le bloc contact (sans téléphone).
  - `prive/cv-lea-rybak-avec-telephone.pdf` : version pour les candidatures, avec le numéro lu dans
    `prive/telephone.txt`. Jamais versionnée ni publiée.
  - Le script refuse un CV qui dépasse une page. Après toute modification des données, régénérer
    les pages ET le CV.

## Si l'adresse du site change

(transfert du dépôt vers un compte GitHub de Léa, ou nom de domaine) : changer `URL` dans
`outils/generer.py`, régénérer les pages et le CV (le QR code change), puis mettre à jour
`sitemap.xml` et `robots.txt`. Les CV déjà imprimés pointeront vers l'ancienne adresse.

## En attente de Léa

Stages et emplois depuis 2024, master obtenu ou non, compétences métier et logiciels, photo,
LinkedIn ou Instagram. Ne rien ajouter sans ses réponses.

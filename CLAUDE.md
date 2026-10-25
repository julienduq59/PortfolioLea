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
- Pas de téléphone ni d'adresse postale en ligne. Seul l'e-mail est affiché (à confirmer par Léa).
- Aucun document d'identité, aucune donnée sensible.
- Pas de photos d'enfants (gala de danse de la MJC de Croix) sans l'accord des familles.
- Toujours montrer un aperçu avant de publier une modification de design.

## Fonctionnement

- Les pages HTML sont **générées** par `outils/generer.py` (`python3 outils/generer.py` depuis
  la racine). Modifier les textes et la liste des œuvres dans ce script, pas dans les fichiers HTML.
- Pages : `index.html`, `oeuvres.html`, `expositions.html`, `photographie.html`, `parcours.html`, `404.html`.
- Design : direction « L'exposition », choisie par Julien sur aperçu. Une œuvre accrochée en grand
  par salle, un cartel de musée sous chaque œuvre. Couleurs reprises du portfolio V1 : bleu nuit
  `#0b1320` et blanc. Thème sombre par défaut, thème clair selon l'appareil ou via le bouton.
  Police Schibsted Grotesk auto-hébergée (`assets/fonts/`).
- Images : WebP dans `assets/oeuvres/`, en deux tailles (`nom.webp`, jusqu'à 1400 px, et
  `nom-640.webp`), avec leur origine dans `nom.webp.json`.
- Cache : `styles.css` et `site.js` sont chargés avec `?v=AAAAMMJJ`. À chaque modification de
  ces fichiers, changer `VERSION` dans `outils/generer.py`, puis régénérer les pages.
- Visionneuse : tout lien `a.voir` ouvre l'image en grand dans un `<dialog>` (Échap pour fermer).

## À faire

- QR code du CV vers https://julienduq59.github.io/PortfolioLea/
- En option : CV PDF A4 avec QR code, GoatCounter, alertes ntfy (comme sur le site de Julien).

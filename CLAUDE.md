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

- **Ne jamais inventer de données.** Sources : **le CV de Léa d'octobre 2026** (source principale du
  parcours : formation, compétences, expériences, centres d'intérêt), son portfolio V1 (PDF Canva, 2026 :
  œuvres, expositions STARTER, pratiques, baccalauréat) et son CV de février 2024. En cas de doute,
  poser la question.
- **Léa valide le contenu avant toute mise en ligne.** Voir `VALIDATION.md`.
- Téléphone : affiché **uniquement sur la page « Mes infos »**, à la demande de Léa (13/11/2026,
  constante `TELEPHONE`). Il reste absent du CV public et des autres pages. Pas d'adresse postale en ligne.
- **Pas de statistiques ni de suivi des visites** (choix de Julien, 25/10/2026) : ni GoatCounter,
  ni alertes ntfy, ni liens `?ref=`. Le site de Julien en a, celui de Léa non.
- Aucun document d'identité, aucune donnée sensible.
- Photos d'enfants : jamais de visage reconnaissable. Les deux photos d'animation (expérience
  « Animatrice », `assets/oeuvres/animation-*.webp`) et celles de La Piscine (`piscine-*.webp`) ont
  les visages floutés et sans métadonnées. Photos d'animation commerciale : seul le visage de Léa reste
  visible, ceux des collègues sont floutés (choix de Julien, 26/10/2026).
  Pas de photos du gala de danse de la MJC de Croix sans l'accord des familles.
- Toujours montrer un aperçu avant de publier une modification de design.

## Objectif

Le site sert à trouver un travail (secteur arts et culture). Ordre voulu par Julien
(25/10/2026) : d'abord le parcours (formation), puis les expériences professionnelles,
puis les œuvres, les expositions et le reste.

**Menu fixe, identique sur toutes les pages : Mes infos, Parcours, Expériences, Œuvres,
Expositions, Photographie.** (« Mes infos » ajouté en tête à la demande de Léa, 13/11/2026.) Il est défini une seule fois (`PAGES` dans `outils/generer.py`) :
ne jamais changer cet ordre sans demande explicite.

## Fonctionnement

- Les pages HTML sont **générées** par `outils/generer.py` (`python3 outils/generer.py` depuis
  la racine). Modifier les textes et la liste des œuvres dans ce script, pas dans les fichiers HTML.
- Pages, dans l'ordre du menu : `index.html`, `mes-infos.html`, `parcours.html`, `experiences.html`, `oeuvres.html`,
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
- Portrait de Léa : en rond à côté de son nom sur l'accueil (`assets/portrait-lea.webp`, demande et
  validation de Julien sur aperçu, 25/10/2026). Même photo que sur son CV.
- **CV PDF** (A4, une page) : `python3 outils/cv.py` depuis la racine (nécessite `pip install segno`,
  Node et Playwright). Il **reproduit à l'identique le CV de Léa d'octobre 2026** (Liberation Sans,
  titres bleus `#2e74b5`, photo ronde) et ajoute **en bas de page** le lien cliquable et le **QR code
  du portfolio** (demande de Julien, 29/10/2026 ; espacements légèrement resserrés pour tenir sur une page). Les textes viennent des données de `outils/generer.py` (`DIPLOMES`, `CERTIFICATS`,
  `COMPETENCES`, `EXPERIENCES`, `CENTRES_INTERET`, `TITRE_CV`, `VILLE`) : les garder mot pour mot
  identiques au CV de Léa.
  - Photo de Léa sur les deux versions (demande de Julien, 25/10/2026) : `outils/photo-lea.jpg`.
  - `assets/cv-lea-rybak.pdf` : version publique, liée depuis l'accueil et le bloc contact, avec la
    photo, **sans téléphone**.
  - `prive/CV-Lea-Rybak.pdf` : CV complet pour les candidatures, avec le téléphone lu dans
    `prive/telephone.txt`. Jamais versionné ni publié.
  - Le script refuse un CV qui dépasse une page. Après toute modification des données, régénérer
    les pages ET le CV.

## Si l'adresse du site change

(transfert du dépôt vers un compte GitHub de Léa, ou nom de domaine) : changer `URL` dans
`outils/generer.py`, régénérer les pages et le CV (le QR code change), puis mettre à jour
`sitemap.xml` et `robots.txt`. Les CV déjà imprimés pointeront vers l'ancienne adresse.

**Page Parcours : rubrique « Diplômes » sous la Formation**, avec le BAFA et le PSC1 (`CERTIFICATS`). Le PSC1 porte la mention « Renouvelé en octobre 2026 » (clé `renouvellement`, sur le site seulement). Demande de Léa, validée sur aperçu le 13/11/2026.

**Mémoires de M1 et M2** : affichés sous le master sur la page Parcours (clé `memoires` de `DIPLOMES[0]`,
sur le site seulement), donnés par Léa et validés sur aperçu le 13/11/2026. L'introduction de la page Parcours ne
met plus en avant les deux expositions (demande de Léa).

**Expositions STARTER 9 et 10 : projets d'études, rangés dans la Formation** (sous la licence),
pas dans les expériences professionnelles (choix de Julien, 25/10/2026). Données : `EXPOS_LICENCE`.

**Expérience la plus importante (Julien) : guide animatrice au musée de La Piscine (Roubaix).** Elle reste
en tête des expériences, mise en avant sur l'accueil et sur la page Expériences.

Ajouts et retraits demandés par Léa le 13/11/2026 (le CV PDF n'est donc plus identique à celui d'octobre) :
- **CDD à temps partiel à la Villa Cavrois (Croix), nov. 2026 - juin 2027** : agent de billetterie et
  agent de surveillance et de médiation. Il est juste sous La Piscine, **sur le portfolio et dans le CV**.
  Missions données par Léa : gestion de la caisse, vente de billets, organisation de la boutique,
  surveillance, médiation. Pour les faire tenir, les espacements du CV ont encore été un peu resserrés.
  Le CV est maintenant presque plein : avant d'ajouter une ligne, regarder ce qui peut en sortir.
- **Service civique au Crous Lille Nord-Pas-de-Calais (sept. - nov. 2026)** : sous la Villa Cavrois,
  **sur le portfolio seulement**.
- **Stage au Couvent** : retiré du CV PDF, il reste sur le portfolio.
Dans `EXPERIENCES`, la clé `cv=False` exclut une expérience du CV, et la clé `note` affiche une ligne en
italique sous les missions.

## En attente

- Page « Mes infos » (`page_infos()`) : présentation validée par Léa (recherche d'un CDI à temps plein dans le
  secteur culturel), e-mail, téléphone, Instagram @lea_rbk_ et CV. LinkedIn (constante `LINKEDIN`, adresse donnée
  par Léa le 13/11/2026). Pas de bloc « Me contacter » en bas de cette page.
- Téléphone dans le CV public : non, sauf demande de Léa.
- Master obtenu ou non (le CV indique « 2024 - 2026 »).

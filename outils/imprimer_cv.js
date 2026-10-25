/* Imprime le CV HTML en PDF A4 avec Chromium (Playwright), et vérifie qu'il tient sur une page.
   Usage : node outils/imprimer_cv.js <cv.html> <cv.pdf>   (appelé par outils/cv.py) */
const { chromium } = require("playwright");

(async () => {
  const [entree, sortie] = process.argv.slice(2);
  const navigateur = await chromium.launch();
  const page = await navigateur.newPage();
  await page.goto("file://" + entree);
  await page.evaluate(() => document.fonts.ready);
  const debords = await page.evaluate(() =>
    [...document.querySelectorAll(".page, .colonne")]
      .filter((el) => el.scrollHeight > el.clientHeight + 1)
      .map((el) => el.className + " : " + el.scrollHeight + " px pour " + el.clientHeight + " px")
  );
  if (debords.length) {
    console.error("Le CV dépasse une page A4 :\n" + debords.join("\n"));
    process.exitCode = 2;
  }
  await page.pdf({ path: sortie, preferCSSPageSize: true, printBackground: true });
  await navigateur.close();
})();

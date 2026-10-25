/* Portfolio de Léa Rybak : bouton de thème, visionneuse des œuvres, copie de l'adresse e-mail. */
(function () {
  "use strict";
  var racine = document.documentElement;

  /* ---------- Thème clair / sombre ----------
     Sans choix du visiteur, le site suit le réglage de son appareil. */
  function themeActuel() {
    var t = racine.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  }
  function libelle(bouton) {
    var l = themeActuel() === "dark" ? "Passer en thème clair" : "Passer en thème sombre";
    bouton.setAttribute("aria-label", l);
    bouton.setAttribute("title", l);
  }
  var boutonTheme = document.querySelector(".theme");
  if (boutonTheme) {
    libelle(boutonTheme);
    boutonTheme.addEventListener("click", function () {
      var nouveau = themeActuel() === "dark" ? "light" : "dark";
      racine.setAttribute("data-theme", nouveau);
      try { localStorage.setItem("theme", nouveau); } catch (e) {}
      libelle(boutonTheme);
    });
  }

  /* ---------- Visionneuse : s'approcher de l'œuvre ---------- */
  var dialogue = document.querySelector(".visionneuse");
  if (dialogue && typeof dialogue.showModal === "function") {
    var image = document.createElement("img");
    image.alt = "";
    dialogue.querySelector(".scene").appendChild(image);
    var legende = dialogue.querySelector("p");
    var origine = null;
    document.addEventListener("click", function (ev) {
      var lien = ev.target.closest("a.voir");
      if (!lien) return;
      ev.preventDefault();
      var vignette = lien.querySelector("img");
      origine = lien;
      image.src = lien.getAttribute("href");
      image.alt = vignette ? vignette.alt : "";
      legende.textContent = lien.getAttribute("data-legende") || "";
      dialogue.showModal();
    });
    function fermer() { dialogue.close(); }
    dialogue.querySelector(".fermer").addEventListener("click", fermer);
    dialogue.addEventListener("click", function (ev) {
      if (ev.target === dialogue || ev.target.classList.contains("scene")) fermer();
    });
    dialogue.addEventListener("close", function () {
      image.removeAttribute("src");
      if (origine) origine.focus();
    });
  }

  /* ---------- Copier l'adresse e-mail ---------- */
  document.querySelectorAll(".copier").forEach(function (b) {
    b.addEventListener("click", function () {
      var texte = b.getAttribute("data-copier");
      function ok() { b.textContent = "Adresse copiée"; setTimeout(function () { b.textContent = "Copier"; }, 2200); }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(texte).then(ok, function () {});
      }
    });
  });
})();

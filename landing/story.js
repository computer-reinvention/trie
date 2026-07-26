/* trie landing — minimal interactivity.
   Theme toggle, copy-to-clipboard on the install command, and a subtle
   reveal-on-scroll for section content. No dependencies. */

(function () {
  "use strict";

  /* ── theme toggle ─────────────────────────────────────────────────── */

  var toggle = document.getElementById("themeToggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var root = document.documentElement;
      var isLight = root.getAttribute("data-theme") === "light";
      if (isLight) {
        root.removeAttribute("data-theme");
      } else {
        root.setAttribute("data-theme", "light");
      }
      try {
        localStorage.setItem("trie-theme", isLight ? "dark" : "light");
      } catch (_) {
        /* localStorage blocked — theme just won't persist */
      }
    });
  }

  /* ── copy install command ─────────────────────────────────────────── */

  document.querySelectorAll(".cmd[data-copy]").forEach(function (cmd) {
    var btn = cmd.querySelector(".cmd__copy");
    var code = cmd.querySelector("code");
    if (!btn || !code) return;
    btn.addEventListener("click", function () {
      var text = code.textContent.trim();
      var done = function () {
        btn.textContent = "copied";
        setTimeout(function () {
          btn.textContent = "copy";
        }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () {});
      } else {
        var ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand("copy");
          done();
        } catch (_) {
          /* no clipboard available */
        }
        document.body.removeChild(ta);
      }
    });
  });

  /* ── subtle reveal-on-scroll ──────────────────────────────────────── */

  var reduced =
    window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!reduced && "IntersectionObserver" in window) {
    var targets = document.querySelectorAll(
      ".panel, .loop__step, .checklist li, .filecard, .loop__payoff"
    );
    targets.forEach(function (el) {
      el.classList.add("reveal-init");
    });
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("reveal-in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -5% 0px" }
    );
    targets.forEach(function (el) {
      io.observe(el);
    });
  }
})();

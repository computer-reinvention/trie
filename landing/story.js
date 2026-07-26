/* trie landing — copy-to-clipboard on the install command. Nothing else. */

(function () {
  "use strict";

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
})();

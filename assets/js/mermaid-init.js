(function () {
  "use strict";

  function showError(container, error) {
    container.classList.add("mermaid-render-error");
    container.textContent = "Diagram could not be rendered.";
    console.error("Mermaid rendering failed:", error);
  }

  async function renderMermaid() {
    if (typeof mermaid === "undefined") {
      console.error("Mermaid library did not load.");
      return;
    }

    mermaid.initialize({
      startOnLoad: false,
      securityLevel: "strict",
      theme: "default",
      suppressErrorRendering: true
    });

    const codeBlocks = document.querySelectorAll(
      "pre code.language-mermaid, pre code.lang-mermaid"
    );

    for (const codeBlock of codeBlocks) {
      const pre = codeBlock.closest("pre");
      if (!pre) continue;

      const container = document.createElement("div");
      container.className = "mermaid";
      container.textContent = codeBlock.textContent.trim();

      const wrapper = pre.closest("div.highlighter-rouge, div.highlight");
      if (wrapper) {
        wrapper.replaceWith(container);
      } else {
        pre.replaceWith(container);
      }

      try {
        await mermaid.run({ nodes: [container] });
      } catch (error) {
        showError(container, error);
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderMermaid, { once: true });
  } else {
    renderMermaid();
  }
})();

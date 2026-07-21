document.addEventListener("DOMContentLoaded", function () {
  if (typeof mermaid !== "undefined") {
    mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });
    const blocks = document.querySelectorAll("pre code.language-mermaid");
    blocks.forEach((block, index) => {
      const pre = block.parentElement;
      const container = document.createElement("div");
      container.className = "mermaid";
      container.textContent = block.textContent;
      pre.replaceWith(container);
    });
    mermaid.run();
  }
});

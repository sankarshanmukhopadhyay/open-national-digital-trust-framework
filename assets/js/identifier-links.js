(function () {
  const registryBase = '/open-national-digital-trust-framework/docs/information-model/identifier-registry.html#';
  const requirementsBase = '/open-national-digital-trust-framework/docs/core-specification/requirements-register.html#';
  const pattern = /\b(?:ONDTF-[A-Z]{3}-\d{3}|CT-[A-Z]{3}-\d{3}|JRN-[A-Z]{3}-\d{3}|ROLE-[A-Z0-9]+|IM-[A-Z]{3}|(?:URI|PLT|ADV|CLAR|CAP|THR|CTL|SB|AST|THCAT|SEC|EPA|RS|INT|AS|AP|TA|TB|ADR|LIM|MPR|EVD|IPR|REC|EQV|CAL|CCL|NCP|REV|GFM)-\d{2,4})\b/g;
  const skip = new Set(['A','CODE','PRE','SCRIPT','STYLE','TEXTAREA','KBD']);
  function targetFor(id) {
    return (id.startsWith('ONDTF-') ? requirementsBase : registryBase) + id.toLowerCase();
  }
  function labelFor(id) {
    return id.startsWith('ONDTF-') ? 'Open '+id+' in the ONDTF Requirements Register' : 'Open '+id+' in the ONDTF Identifier Registry';
  }
  function link(root) {
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    const nodes=[]; while(walker.nextNode()) nodes.push(walker.currentNode);
    for(const n of nodes){
      if(!n.parentElement || skip.has(n.parentElement.tagName) || n.parentElement.closest('a,pre,code,script,style')) continue;
      const text=n.nodeValue; pattern.lastIndex=0; if(!pattern.test(text)) continue; pattern.lastIndex=0;
      const frag=document.createDocumentFragment(); let last=0,m;
      while((m=pattern.exec(text))){
        frag.append(text.slice(last,m.index));
        const a=document.createElement('a'); a.href=targetFor(m[0]); a.textContent=m[0]; a.className='ondtf-id-link'; a.title=labelFor(m[0]);
        frag.append(a); last=m.index+m[0].length;
      }
      frag.append(text.slice(last)); n.replaceWith(frag);
    }
  }
  document.addEventListener('DOMContentLoaded',()=>{ const main=document.querySelector('main'); if(main) link(main); });
})();

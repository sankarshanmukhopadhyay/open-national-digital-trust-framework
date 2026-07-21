#!/usr/bin/env python3
from pathlib import Path
import re, shutil
root=Path(__file__).resolve().parents[1]
out=root/'artifacts'/'mermaid'
if out.exists(): shutil.rmtree(out)
out.mkdir(parents=True)
count=0
for p in list((root/'docs').rglob('*.md'))+list((root/'profiles').rglob('*.md')):
    text=p.read_text(encoding='utf-8')
    for i,block in enumerate(re.findall(r'```mermaid\s*\n(.*?)\n```', text, re.S),1):
        count+=1
        name=str(p.relative_to(root)).replace('/','__').replace('.md','')+f'__{i}.mmd'
        (out/name).write_text(block.strip()+'\n',encoding='utf-8')
print(f'Extracted {count} Mermaid diagrams to {out}')

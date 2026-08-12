from pathlib import Path
import re,yaml
ROOT=Path(__file__).resolve().parents[1]
reg=yaml.safe_load((ROOT/'model/references/identifier-registry.yaml').read_text())
ids=[x['id'] for x in reg['identifiers']]
assert len(ids)==len(set(ids)), 'duplicate identifier registry entries'
page=(ROOT/'docs/information-model/identifier-registry.md').read_text()
for ident in ids: assert f'id="{ident.lower()}"' in page, f'missing anchor {ident}'
print(f'Identifier registry validation: PASS ({len(ids)} resolvable identifiers, 0 duplicate entries)')

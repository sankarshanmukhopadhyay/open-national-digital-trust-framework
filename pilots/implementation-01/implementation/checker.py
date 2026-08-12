from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[3]
model=yaml.safe_load((ROOT/'model/operations/provider-lifecycle.yaml').read_text())
allowed={(t['from'],t['to']):(t['decision_role'],set(t.get('evidence',[]))) for t in model['transitions']}
def allows(src,dst,role,evidence):
    rule=allowed.get((src,dst))
    return bool(rule and rule[0]==role and rule[1].issubset(set(evidence)))
if __name__=='__main__':
    assert allows('active','suspended','ROLE-SA',['suspension_decision'])
    assert not allows('active','suspended','ROLE-FA',['suspension_decision'])
    assert not allows('active','suspended','ROLE-SA',[])
    print('Independent pilot simulation: PASS (3 assertions)')

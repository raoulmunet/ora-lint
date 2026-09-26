from __future__ import annotations
from dataclasses import dataclass,asdict
import re

@dataclass(frozen=True)
class Finding:
    rule:str; line:int; message:str; suggestion:str
    def to_dict(self): return asdict(self)

RULES=[
("ORA001",r"\bSELECT\s+\*", "SELECT * couples code to table shape.", "List the required columns explicitly."),
("ORA002",r"\bWHEN\s+OTHERS\s+THEN\s+NULL\b", "Exception is swallowed silently.", "Log/contextualize the error and RAISE when the caller must see the failure."),
("ORA003",r"\bNOT\s+IN\s*\(", "NOT IN can produce surprising results when NULL is present.", "Review NULL semantics; NOT EXISTS is often clearer for anti-joins."),
("ORA004",r"\bCOUNT\s*\(\s*\*\s*\)\s*(?:>|=)\s*0", "COUNT(*) may scan more rows than needed for existence checks.", "Consider EXISTS when only existence is required."),
("ORA005",r"\bWHERE\s+(?:UPPER|LOWER|TRUNC|TO_CHAR)\s*\(\s*[A-Za-z][\w$#]*", "A function wraps a predicate column.", "Review whether ordinary index access is affected; a function-based index may be appropriate."),
]
def lint(sql:str)->list[Finding]:
    out=[]
    for rule,pat,msg,sugg in RULES:
        for m in re.finditer(pat,sql,re.I|re.S):
            out.append(Finding(rule,sql.count("\n",0,m.start())+1,msg,sugg))
    for m in re.finditer(r"\bFOR\b[\s\S]{0,2000}?\bLOOP\b([\s\S]{0,2000}?)\bEND\s+LOOP\b",sql,re.I):
        c=re.search(r"\bCOMMIT\b",m.group(1),re.I)
        if c:
            pos=m.start(1)+c.start()
            out.append(Finding("ORA006",sql.count("\n",0,pos)+1,"COMMIT appears inside a loop.","Batch commits deliberately; per-row commits add overhead and change transaction semantics."))
    return sorted(out,key=lambda x:(x.line,x.rule))

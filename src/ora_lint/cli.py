from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import lint

def main(argv=None):
    p=argparse.ArgumentParser(description="Lint Oracle SQL/PLSQL.")
    p.add_argument("source"); p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv); findings=lint(Path(a.source).read_text(encoding="utf-8"))
    if a.format=="json": print(json.dumps([f.to_dict() for f in findings],indent=2))
    else:
        for f in findings: print(f"{a.source}:{f.line}: {f.rule} {f.message}\n  Suggestion: {f.suggestion}")
    return 1 if findings else 0
if __name__=="__main__": raise SystemExit(main())

# ora-lint

A small Oracle SQL / PL/SQL static checker focused on high-signal anti-patterns.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported |
> | Oracle Database 23ai | ✅ Supported |
> | Oracle AI Database 26ai | ✅ Supported |
>
> Rules are written to be portable across these releases unless a rule explicitly states otherwise.

## Current checks

- `SELECT *`;
- `WHEN OTHERS THEN NULL`;
- `COMMIT` inside a simple loop block;
- `NOT IN` review warning because NULL semantics can surprise;
- `COUNT(*)` used as an existence-check candidate;
- likely literal-heavy predicates that may benefit from bind variables;
- function-wrapped predicate columns that can affect ordinary index access.

## Installation

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-lint.git"
```

## Usage

```bash
ora-lint examples/bad_sql.sql
ora-lint examples/bad_sql.sql --format json
```

Exit code is non-zero when warnings are found, which makes the tool suitable for CI.

## Philosophy

Rules are **review prompts**, not automatic verdicts. Oracle SQL performance is contextual, so messages explain why a pattern deserves attention instead of claiming it is always wrong.

## License

MIT.

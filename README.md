# ora-lint

[![tests](https://github.com/raoulmunet/ora-lint/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-lint/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.

<div align="center">

# Hi, I'm Duo

**SQL tooling · database internals · parsers**

<a href="https://github.com/sqlfluff/sqlfluff">
  <img src="https://img.shields.io/badge/contributor-sqlfluff-2f6f4e?style=flat-square" alt="sqlfluff">
</a>
<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="python">
<img src="https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="rust">
<img src="https://img.shields.io/badge/-SQL-4479A1?style=flat-square" alt="sql">

</div>

---

### What I'm working on

I contribute to [sqlfluff](https://github.com/sqlfluff/sqlfluff), a modular SQL
linter and formatter. Most of my work is dialect grammar: teaching the parser to
read real syntax it currently rejects, without making it stricter about
everything else.

Merged so far:

| PR | Change |
|:--|:--|
| [#8858](https://github.com/sqlfluff/sqlfluff/pull/8858) | Trino: parse `TRUNCATE TABLE` |
| [#8857](https://github.com/sqlfluff/sqlfluff/pull/8857) | Redshift: parse `SHOW` statements |
| [#8818](https://github.com/sqlfluff/sqlfluff/pull/8818) | Redshift: masking policies |

A few more are open and waiting on review — the interesting one is
[#8868](https://github.com/sqlfluff/sqlfluff/pull/8868), a reusable parser
matcher for delimiters that have to sit on their own line (Oracle's `/`).

### Things I find interesting

- SQL dialects and how a grammar stays permissive without becoming useless
- Parser performance — I made alignment on a 200-column query go from 32s to 1.1s
  ([#8869](https://github.com/sqlfluff/sqlfluff/pull/8869))
- Compilers. I've written a C-minus one for a course and enjoyed the front end
  more than the back end.

### Elsewhere

Duo-ee means 对！

<sub>This profile README is hand-written, but I do use AI assistance in my
contributions; every PR I open says so.</sub>

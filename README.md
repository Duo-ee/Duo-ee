<div align="center">

# Hi, I'm Duo

**SQL tooling · database internals · parsers**

<a href="https://github.com/sqlfluff/sqlfluff">
  <img src="https://img.shields.io/badge/contributor-sqlfluff-2f6f4e?style=flat-square" alt="sqlfluff">
</a>
<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="python">
<img src="https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="rust">
<img src="https://img.shields.io/badge/-SQL-4479A1?style=flat-square" alt="sql">

<br><br>

<img height="158" src="https://github-readme-stats.vercel.app/api?username=Duo-ee&show_icons=true&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=2F81F7&icon_color=2F81F7&text_color=C9D1D9&hide=stars" alt="stats" />
<img height="158" src="https://github-readme-streak-stats.herokuapp.com/?user=Duo-ee&theme=github-dark-blue&hide_border=true&background=0D1117&ring=2F81F7&fire=2F81F7&currStreakNum=C9D1D9&currStreakLabel=2F81F7" alt="streak" />

</div>

---

### What I'm working on

I contribute to [sqlfluff](https://github.com/sqlfluff/sqlfluff), a modular SQL
linter and formatter. Most of my work is dialect grammar: teaching the parser to
read real syntax it currently rejects, without making it stricter about
everything else.

Merged so far:

<!-- MERGED:START -->
| Repository | PR | Change |
|:--|:--|:--|
| [Rekin226/aquascope](https://github.com/Rekin226/aquascope) | [#632](https://github.com/Rekin226/aquascope/pull/632) | docs: state the Archive catalog and mirror as two numbers |
| [truera/trulens](https://github.com/truera/trulens) | [#2999](https://github.com/truera/trulens/pull/2999) | ci: install Miniconda in the conda packaging job |
| [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) | [#8869](https://github.com/sqlfluff/sqlfluff/pull/8869) | perf(reflow): find alignment siblings in a single walk |
| [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) | [#8857](https://github.com/sqlfluff/sqlfluff/pull/8857) | fix(redshift): parse SHOW statements |
| [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) | [#8858](https://github.com/sqlfluff/sqlfluff/pull/8858) | fix(trino): parse TRUNCATE TABLE statements |
| [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) | [#8818](https://github.com/sqlfluff/sqlfluff/pull/8818) | Redshift: support dynamic data masking policies |
| [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) | [#8841](https://github.com/sqlfluff/sqlfluff/pull/8841) | Databricks: preserve magic-cell newlines for LT01 |
<!-- MERGED:END -->

A few more are open and waiting on review — the interesting one is
[#8868](https://github.com/sqlfluff/sqlfluff/pull/8868), a reusable parser
matcher for delimiters that have to sit on their own line (Oracle's `/`).

### Also working on

Over at [aquascope](https://github.com/Rekin226/aquascope), a hydrology data
project: I got the archive to state its size the same way everywhere
([#632](https://github.com/Rekin226/aquascope/pull/632), merged), and have five
more open — Sen's slope measured against the calendar year rather than against
sequence positions ([#671](https://github.com/Rekin226/aquascope/pull/671)),
GloFAS requests sent to the EWDS endpoint that actually serves them
([#672](https://github.com/Rekin226/aquascope/pull/672)), Theis drawdown for a
dropped well ([#674](https://github.com/Rekin226/aquascope/pull/674)), near-dry
basins kept out of the "rivers much above normal" findings
([#675](https://github.com/Rekin226/aquascope/pull/675)), and a record-quality
half on the site reconnaissance ([#676](https://github.com/Rekin226/aquascope/pull/676)).

In [truera/trulens](https://github.com/truera/trulens) I fixed the conda
packaging job ([#2999](https://github.com/truera/trulens/pull/2999), merged).

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

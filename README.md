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

| PR | Change |
|:--|:--|
| [#8858](https://github.com/sqlfluff/sqlfluff/pull/8858) | Trino: parse `TRUNCATE TABLE` |
| [#8857](https://github.com/sqlfluff/sqlfluff/pull/8857) | Redshift: parse `SHOW` statements |
| [#8818](https://github.com/sqlfluff/sqlfluff/pull/8818) | Redshift: masking policies |

A few more are open and waiting on review — the interesting one is
[#8868](https://github.com/sqlfluff/sqlfluff/pull/8868), a reusable parser
matcher for delimiters that have to sit on their own line (Oracle's `/`).

### Also working on

Over at [aquascope](https://github.com/Rekin226/aquascope) I opened
[#632](https://github.com/Rekin226/aquascope/pull/632), getting the project to
state the size of its archive the same way everywhere: 75,833 stations
catalogued, 5,850 of them mirrored, taken straight from the harvest manifest
rather than from an old figure in the roadmap.

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

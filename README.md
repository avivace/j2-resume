<h1>
<img src=".meta/name.svg" alt="j2-resume" width="200">
</h1>

> An opinionated workflow to produce different versions of a Curriculum Vitae (rèsumè) document using different localisations, templates, styles and formats without having to mantain them all.

<br>

![Architecture](.meta/flow.svg)

## Goals

- Have an agnostic data source (JSON) and edit ONLY that when updating the informations (API access to a remote endpoint exposing a compliant JSON is trivially implementable, too).
- Have data source compliant and validated against a formal specification or schema (use JSON schema and possibly the JSON-Resume specification?). Templates must respect this schema too.
- Easily update and version the data source using a text editor or a (visual) JSON editor;
- Keep the hybrid Jinja2 templates clean and similar to their plain format versions;


## Requirements

- a TeX distribution
- XeLaTeX

On Debian:

```bash
sudo apt install texlive-base pandoc
```

## Build

### LaTeX TeX/J2 template

```bash
python j2tex.py
xelatex cv_render.tex
```

### VueJS web version

TODO

### markdown/pandoc exports

TODO


## Related projects

If you wish to remain sane, something like [pandoc-resume](https://github.com/mszep/pandoc_resume) could fit your use-case with less effort (BUT it doesn't provide a serialized data source, it's markdown).

## References

Various resources, links and threads examined for the project.

- [How to loop over the JSON object / list?](https://tex.stackexchange.com/questions/489417/how-to-loop-over-the-json-object-list)
- [Error as I try to read and display the results from JSON file](https://tex.stackexchange.com/questions/489395/error-as-i-try-to-read-and-display-the-results-from-json-file/489397#489397)
- [API JSON in Latex](https://tex.stackexchange.com/questions/272401/api-json-in-latex)
- [jq json processor](https://stedolan.github.io/jq/manual/)
- [Transform a JSON file into a formated Latex](https://groups.google.com/forum/#!topic/pandoc-discuss/VBHwMj6IVOY)
- [How to iterate over a comma separated list?](https://tex.stackexchange.com/questions/159118/how-to-iterate-over-a-comma-separated-list)
- [Why choose LuaLaTeX over XeLaTeX?](https://tex.stackexchange.com/questions/126206/why-choose-lualatex-over-xelatex)
- [Considerations when migrating from XeTeX to LuaTeX?](https://tex.stackexchange.com/questions/23598/considerations-when-migrating-from-xetex-to-luatex)

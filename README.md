# ETJump Documentation
[**ETJump**](http://etjump.com) is a [Wolfenstein: Enemy Territory](https://en.wikipedia.org/wiki/Wolfenstein:_Enemy_Territory) trickjump modification. The documentation contains set of all available ETJump cvars, mapping entities and more. The documentation is hosted on the [http://etjump.rtfd.io/](http://etjump.rtfd.io/). 

## How to contribute

This documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) with [MyST Parser](https://myst-parser.readthedocs.io/en/latest/). This allows the documentation to be written using Markdown, while having the full power of reStructuredText available if desired. If you wish to contribute, we prefer contributions written in Markdown - but we accept pages written in reStructuredText too if that is what you prefer to write.

For simple edits (fixing typos, rewording things etc), editing the pages directly in GitHub is the simplest way to contribute.

1. Fork the project
2. Do your edits in your fork of the repository
3. Create a Pull Request to this repository

For more complex edits, it is recommended to setup an environment to build the documentation locally.

### Setting up a local build environment

1. Install [Python](https://www.python.org/)
2. Clone the repository
3. Optional, but **highly recommended:** setup a [virtual Python environment](https://docs.python.org/3/library/venv.html)
4. Navigate to the documentation directory and install the dependencies
```sh
pip install -r docs/requirements.txt
```

### Building the documentation

For building, there are two main options: `make` and `sphinx-autobuild`.

#### Using make
1. Install [make](https://www.gnu.org/software/make)
2. Navigate to the `docs` directory and build the documentation
```sh
cd docs
make html
```
4. Open `docs/_build/html/index.html` in your browser to view the pages

#### Using sphinx-autobuild (recommended)
1. Install [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/)
```sh
pip install sphinx-autobuild
```
2. Build the documentation
```sh
sphinx-autobuild docs docs/_build/html
```
3. This will start an HTTP server at http://127.0.0.1:8000 and monitors changes in the `docs` directory. Whenever you make changes to the pages, `sphinx-autobuild` will rebuild the documentation automatically, allowing for much faster workflow.

### Adding new pages

If you're adding new pages to the documentation, the pages must be included within a `toctree` directive in `index.md`. After adding the page, it's necessary to do a clean rebuild of the documentation for the page to appear in the navigation.

```sh
cd docs
make clean
make html
```

See the examples for existing pages in the `index.md`, and the documentation for [toctree](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree) in Sphinx documentation.

======================
Cookiecutter PyPackage
======================

text

Features
--------

* Testing setup with Pytest_ and Coverage_.
* Linting wiht Black_, import sorting with Isort_.
* Package managing with Flit_.
* GithubActions_: Simple continuous integration with github actions.
* Nox_ testing: Setup to easily test for Python 3.8.
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* Release to PyPI_ when running ``make publish`` or ``flit publish``.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/plaguss/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Install Flit_, and then install the requirements of the project: ``make install``.
* Register_ your project with PyPI.
* Run the Travis CLI command ``travis encrypt --add deploy.password`` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and ``setup.py`` differences.

* `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions.
  See ``README.rst`` or the `github comparison view`_ for exhaustive list of
  additions and modifications.

* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements files rather than a requirements list in the ``setup.py`` file.

* `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_ instead of bump2version_ and with separate requirements files.

* `briggySmalls/cookiecutter-pypackage`_: A fork using Poetry_ for neat package management and deployment, with linting, formatting, no makefiles and more.

* `veit/cookiecutter-namespace-template`_: A cookiecutter template for python modules with a namespace

* `zillionare/cookiecutter-pypackage`_: A template containing Poetry_, Mkdocs_, Github CI and many more. It's a template and a package also (can be installed with `pip`)

* `waynerv/cookiecutter-pypackage`_: A fork using Poetry_, Mkdocs_, Pre-commit_, Black_ and Mypy_. Run test, staging and release workflows with GitHub Actions, automatically generate release notes from CHANGELOG.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Nox: https://nox.thea.codes/en/stable/
.. _GithubActions: https://github.com/features/actions
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _PyPi: https://pypi.python.org/pypi
.. _Isort: https://pycqa.github.io/isort/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Mypy: https://mypy.readthedocs.io/en/stable/
.. _Pytest: https://docs.pytest.org/en/6.2.x/contents.html
.. _Coverage: https://pypi.org/project/pytest-cov/
.. _Flit: https://flit.readthedocs.io/en/latest/

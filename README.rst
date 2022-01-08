======================
Cookiecutter PyPackage
======================

text

Features
--------

* Testing setup with Pytest_ and Coverage_.
* Linting wiht Black_, import sorting with Isort_.
* Package managing with Flit_ and PyProjectToml_.
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
* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* Release your package by running ``make publish``.
* Manage your dependencies by means of PyProjectToml_.

.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

Not Exactly What You Want?
--------------------------

Please read the original `audreyfeldroy/cookiecutter-pypackage`_, all the necessary info can be found there.

.. _`audreyfeldroy/cookiecutter-pypackage`: https://github.com/audreyfeldroy/cookiecutter-pypackage


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
.. _PyProjectToml: https://www.python.org/dev/peps/pep-0621/
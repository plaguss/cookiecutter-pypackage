import nox


def install_flit_dev_deps(session):
    session.install("flit")
    session.run("flit", "install", "--deps", "develop")


@nox.session(python=["3.8"])
def tests(session):
    install_flit_dev_deps(session)
    session.run("pytest", "--cov={{ cookiecutter.project_slug }}", "--cov-report=xml", "tests")


@nox.session
def lint(session):
    install_flit_dev_deps(session)
    session.run("isort", "{{ cookiecutter.project_slug }}")
    session.run("black", "--check", "{{ cookiecutter.project_slug }}")
    session.run("mypy", "{{ cookiecutter.project_slug }}")
    session.run("make", "docs")

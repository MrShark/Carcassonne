import nox


@nox.session(python="3.11")
def docs(session):
    """Build the documentation."""
    session.install("-r", "docs/requirements.txt")
    session.run("sphinx-build", "docs", "docs/_build")

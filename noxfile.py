"""Nox sessions for building and managing the Carcassonne project documentation."""

import nox


@nox.session(python="3.11")
def docs(session: nox.Session) -> None:
    """Build the documentation."""
    session.install("-r", "docs/requirements.txt")
    session.run("sphinx-build", "docs", "docs/_build")

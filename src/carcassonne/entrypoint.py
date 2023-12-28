import logging

import click

from . import Card, __version__
from .sets import card_sets, set_names

logger = logging.getLogger()


@click.command()
@click.version_option(version=__version__)
@click.option("--output-dir", default="tiles", help="Directory to write tiles in.")
@click.option(
    "--feature", default="", help="Only draw tiles with this feature. (default all)"
)
@click.option("--list", is_flag=True, default=False, help="List alls sets (and quit).")
@click.option("-v", "--verbose", count=True, help="Increase verbosity")
@click.argument("sets", nargs=-1)
def generate_sets(output_dir, feature, sets, list, verbose):
    """Generate carcassonne tiles in SETS."""

    if verbose == 1:
        logger.setLevel(logging.INFO)
    if verbose >= 2:
        logger.setLevel(logging.DEBUG)

    if list:
        for cardset in card_sets:
            print(f"{cardset}: {set_names[cardset]}")

    if not sets:
        sets = card_sets.keys()

    for cardset in sets:
        for n, card in card_sets[cardset].items():
            for i in range(card[0]):
                if not feature or feature in card[1].keys():
                    Card(f"{cardset}{n:02}", output_dir=output_dir, **card[1]).draw(
                        i + 1
                    )


@click.command()
@click.version_option(version=__version__)
def helper():
    ways = set()
    for s in card_sets.values():
        for c in s.values():
            for w in c[1].get("river", "").split():
                print(f'        direction["{w}"] = ("╺", 0)')

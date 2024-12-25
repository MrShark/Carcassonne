"""Entrypoints for scripts."""

import logging

import click

from . import Card, __version__, tile_cards
from .sets import card_sets, set_names

logger = logging.getLogger()


@click.command()
@click.version_option(version=__version__)
@click.option("--output-dir", default="tiles", help="Directory to write tiles in.")
@click.option("--feature", default="", help="Only draw tiles with this feature. (default all)")
@click.option("--list", "list_sets", is_flag=True, default=False, help="List alls sets (and quit).")
@click.option("-v", "--verbose", count=True, help="Increase verbosity")
@click.argument("sets", nargs=-1)
def generate_sets(output_dir: str, feature: str, sets: str, *, list_sets: bool, verbose: int) -> None:
    """Generate carcassonne tiles in SETS."""
    if verbose == 1:
        logger.setLevel(logging.INFO)
    if verbose >= 2:  # noqa: PLR2004
        logger.setLevel(logging.DEBUG)

    if list_sets:
        for cardset in card_sets:
            print(f"{cardset}: {set_names[cardset]}")  # noqa: T201

    if not sets:
        sets = card_sets.keys()

    for cardset in sets:
        for n, card in card_sets[cardset].items():
            for i in range(card[0]):
                if not feature or feature in card[1]:
                    Card(f"{cardset}{n:02}-{i+1}", output_dir=output_dir, **card[1]).draw()


@click.command()
@click.version_option(version=__version__)
@click.option("--output", default="tiled.svg", help="Document to tile the tiles in.")
@click.option("--width", default=5, type=int, help="Number of cards on each row.")
@click.argument("tiles", nargs=-1)
def tiler(output: str, width: int, tiles: list[str]) -> None:
    """Tile the given tiles/bricks into one document."""
    tile_cards(output, tiles, width)


@click.command()
@click.version_option(version=__version__)
def helper() -> None:
    """Helper script during development."""
    for s in card_sets.values():
        for c in s.values():
            for w in c[1].get("river", "").split():
                print(f'        direction["{w}"] = ("╺", 0)')  # noqa: T201

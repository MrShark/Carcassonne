import logging
import xml.etree.ElementTree as ET
from os import path
from typing import Iterable

__version__ = "0.1.0"
GFX_DIR = path.join(path.dirname(__file__), "..", "gfx")
logger = logging.getLogger()


def get_gfx(filename):
    """Open `filename` in GFX_DIR and return the ELementTree element with the id gfx"""
    logging.debug(f"Reading graphics from {filename}")
    tree = ET.parse(path.join(GFX_DIR, filename))
    return tree.find(".//*[@id='gfx']")


def write_tile(filename: str, gfx: Iterable):
    """Create a tile with the graphics in gfx added."""
    tree = ET.parse(path.join(GFX_DIR, "tile.svg"))
    tile = tree.find(".//*[@id='tile']")
    for g in gfx:
        if g:
            tile.append(g)
    tree.write(filename)


class Card:
    """A Carcassonne card"""

    def __init__(self, name, output_dir="tiles", **args) -> None:
        self.roads = ""
        self.city = ""
        self.river = ""

        self.shield = False  # Do the card have a Shield
        self.monastery = False
        self.cathedral = False
        self.inn = False
        self.spring = False
        self.lake = False
        self.pigs = False
        self.vulcano = False
        self.cloth = False
        self.grain = False
        self.wine = False
        self.dragon = False
        self.princess = False
        self.portal = False
        self.tower = False
        self.abbey = False
        self.shrine = False
        self.name = name

        self.output_dir = output_dir
        for attr, value in args.items():
            if attr in self.__dict__:
                self.__dict__[attr] = value
            else:
                raise AttributeError(
                    f"{self.__class__.__name__} have no attribute {attr}"
                )
        # print(self.roads)

        self.tile = ET.parse(path.join(GFX_DIR, "tile.svg"))
        self.features = self.tile.find(".//*[@id='tile']")

    def draw(self, count: int):
        if self.roads:
            for dir in self.roads.split(" "):
                logging.debug(f"Adding {dir} Road to {self.name}")
                self.features.append(get_gfx(f"Road-{dir}.svg"))
        if self.city:
            for dir in self.city.split(" "):
                logging.debug(f"Adding {dir} City to {self.name}")
                self.features.append(get_gfx(f"City-{dir}.svg"))
        if self.river:
            for dir in self.river.split(" "):
                logging.debug(f"Adding {dir} River to {self.name}")
                self.features.append(get_gfx(f"River-{dir}.svg"))

        if self.abbey:
            logging.debug(f"Adding Abbey to {self.name}")
            self.features.append(get_gfx("Abbey.svg"))

        if self.cathedral:
            logging.debug(f"Adding Cathedral to {self.name}")
            self.features.append(get_gfx("Cathedral.svg"))

        if self.cloth:
            logging.debug(f"Adding Cloth to {self.name}")
            self.features.append(get_gfx("Cloth.svg"))

        if self.dragon:
            logging.debug(f"Adding Dragon to {self.name}")
            self.features.append(get_gfx("Dragon.svg"))

        if self.grain:
            logging.debug(f"Adding Grain to {self.name}")
            self.features.append(get_gfx("Grain.svg"))

        if self.inn:
            logging.debug(f"Adding Inn to {self.name}")
            self.features.append(get_gfx("Inn.svg"))

        if self.lake:
            logging.debug(f"Adding Lake to {self.name}")
            self.features.append(get_gfx("Lake.svg"))

        if self.monastery:
            logging.debug(f"Adding Monastery to {self.name}")
            self.features.append(get_gfx("Monastery.svg"))

        if self.pigs:
            logging.debug(f"Adding Pigs to {self.name}")
            self.features.append(get_gfx("Pigs.svg"))

        if self.portal:
            logging.debug(f"Adding Portal to {self.name}")
            self.features.append(get_gfx("Portal.svg"))

        if self.princess:
            logging.debug(f"Adding Princess to {self.name}")
            self.features.append(get_gfx("Princess.svg"))

        if self.shield:
            logging.debug(f"Adding Shield to {self.name}")
            self.features.append(get_gfx("Shield.svg"))

        if self.shrine:
            logging.debug(f"Adding Shrine to {self.name}")
            self.features.append(get_gfx("Shrine.svg"))

        if self.spring:
            logging.debug(f"Adding Spring to {self.name}")
            self.features.append(get_gfx("Spring.svg"))

        if self.tower:
            logging.debug(f"Adding Tower to {self.name}")
            self.features.append(get_gfx("Tower.svg"))

        if self.vulcano:
            logging.debug(f"Adding Vulcano to {self.name}")
            self.features.append(get_gfx("Vulcano.svg"))

        if self.wine:
            logging.debug(f"Adding Wine to {self.name}")
            self.features.append(get_gfx("Wine.svg"))

        logging.info(f"Writing to {self.output_dir}/{self.name}-{count:02}.svg")
        self.tile.write(f"{self.output_dir}/{self.name}-{count:02}.svg")

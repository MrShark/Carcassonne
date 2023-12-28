import logging
import random
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


def get_element(tree: ET.ElementTree, element: str) -> ET.Element:
    """Type protected ET.ElementTree.find()"""

    rv = tree.find(f".//*[@id='{element}']")
    if rv is not None:
        return rv
    else:
        raise TypeError


def write_tile(filename: str, gfx: Iterable):
    """Create a tile with the graphics in gfx added."""
    tree = ET.parse(path.join(GFX_DIR, "tile.svg"))
    tile = get_element(tree, "tile")
    for g in gfx:
        if g:
            tile.append(g)
    tree.write(filename)


class Card:
    """A Carcassonne card"""

    direction = {}
    direction["E"] = ("╺", 0)
    direction["EN"] = ("┗", 0)
    direction["ENS"] = ("┳", 3)
    direction["ENsw"] = ("╄", 0)
    direction["ENSW"] = ("╋", 0)
    direction["ENW"] = ("┳", 2)
    direction["ES"] = ("┗", 1)
    direction["ESW"] = ("┳", 0)
    direction["EW"] = ("┃", 1)
    direction["Ew"] = ("╼", 0)
    direction["N"] = ("╺", 3)
    direction["Nes"] = ("┞", 0)
    direction["Nesw"] = ("╀", 0)
    direction["NS"] = ("┃", 0)
    direction["Nsw"] = ("┦", 0)
    direction["NSW"] = ("┳", 1)
    direction["NW"] = ("┗", 3)
    direction["NWes"] = ("╃", 0)
    direction["S"] = ("╺", 1)
    direction["SW"] = ("┗", 2)
    direction["W"] = ("╺", 2)

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

        self.seed = ""
        self.output_dir = output_dir
        for attr, value in args.items():
            if attr in self.__dict__:
                self.__dict__[attr] = value
                self.seed += str(attr) + str(value)
            else:
                raise AttributeError(
                    f"{self.__class__.__name__} have no attribute {attr}"
                )
        # print(self.roads)

        self.tile = ET.parse(path.join(GFX_DIR, "tile.svg"))
        self.features = get_element(self.tile, "tile")

    def draw_roads(self, direction):
        logging.debug(f"Adding {direction} Road to {self.name}")
        W1 = (0, 22.5)
        W2 = (0, 27.5)
        E1 = (50, 22.5)
        E2 = (50, 27.5)
        S1 = (22.5, 50)
        S2 = (27.5, 50)
        N1 = (22.5, 0)
        N2 = (27.5, 0)
        glyph, rotation = self.direction[direction]
        if glyph == "╺":
            a = (random.random() * 5 + 22.5, random.random() * 10 + 20)

            path = f"""M {E1[0]} {E1[1]}
                    C {E1[0]-5} {E1[1]} {a[0]+5} {(a[1]-2.5+E1[1])/2} {a[0]} {a[1]-2.5}
                    Q {a[0]-5} {a[1]} {a[0]} {a[1]+2.5}
                    C {a[0]+5} {(a[1]+2.5+E2[1])/2} {E2[0]-5} {E2[1]} {E2[0]} {E2[1]}
                    """
        elif glyph == "┗":
            a = (random.random() * 10 + 20, random.random() * 10 + 20)

            path = f"""M {N1[0]} {N1[1]}
                    Q {a[0]} {a[1]} {E2[0]} {E2[1]}
                    M {N2[0]} {N2[1]}
                    Q {a[0]+4} {a[1]-4} {E1[0]} {E1[1]}
                    """

        elif glyph == "┃":
            a = (random.random() * 10 + 17.5, random.random() * 10 + 20)

            path = f"""M {N1[0]} {N1[1]}
                    Q {a[0]} {a[1]} {S1[0]} {S1[1]}
                    M {N2[0]} {N2[1]}
                    Q {a[0]+5} {a[1]} {S2[0]} {S2[1]}
                    """

        elif glyph == "┳":
            a = (random.random() * 10 + 20, random.random() * 10 + 22.5)

            path = f"""M {W1[0]} {W1[1]}
                    Q {a[0]-5} {a[1]-5} {E1[0]} {E1[1]}
                    M {W2[0]} {W2[1]}
                    C {a[0]-2.5} {a[1]} {a[0]-2.5} {a[1]} {S1[0]} {S1[1]}
                    M {S2[0]} {S2[1]}
                    C {a[0]+2.5} {a[1]} {a[0]+2.5} {a[1]} {E2[0]} {E2[1]}
                    """
        elif glyph == "╋":
            a = (random.random() * 20 + 15, random.random() * 20 + 15)

            path = f"""M {W2[0]} {W2[1]}
                    C {a[0]-2.5} {a[1]+2.5} {a[0]-2.5} {a[1]+2.5} {S1[0]} {S1[1]}
                    M {S2[0]} {S2[1]}
                    C {a[0]+2.5} {a[1]+2.5} {a[0]+2.5} {a[1]+2.5} {E2[0]} {E2[1]}
                    M {E1[0]} {E1[1]}
                    C {a[0]+2.5} {a[1]-2.5} {a[0]+2.5} {a[1]-2.5} {N2[0]} {N2[1]}
                    M {N1[0]} {N1[1]}
                    C {a[0]-2.5} {a[1]-2.5} {a[0]-2.5} {a[1]-2.5} {W1[0]} {W1[1]}
                    """

        else:
            logging.error(
                f"Strange glyph {glyph} when adding {direction} road to {self.name}"
            )

    def draw_river(self, direction):
        logging.debug(f"Adding {direction} River to {self.name}")
        W1 = (0, 20)
        W2 = (0, 30)
        E1 = (50, 20)
        E2 = (50, 30)
        S1 = (20, 50)
        S2 = (30, 50)
        N1 = (20, 0)
        N2 = (30, 0)
        glyph, rotation = self.direction[direction]
        if glyph == "╺":
            a = (random.random() * 5 + 22.5, random.random() * 10 + 20)

            path = f"""M {E1[0]} {E1[1]}
                    C {E1[0]-5} {E1[1]} {a[0]+5} {a[1]-5} {a[0]} {a[1]-5}
                    Q {a[0]-10} {a[1]} {a[0]} {a[1]+5}
                    C {a[0]+5} {a[1]+5} {E2[0]-5} {E2[1]} {E2[0]} {E2[1]}
                    """
        elif glyph == "┗":
            a = (random.random() * 10 + 20, random.random() * 10 + 20)

            path = f"""M {N1[0]} {N1[1]}
                    Q {a[0]} {a[1]} {E2[0]} {E2[1]}
                    M {N2[0]} {N2[1]}
                    Q {a[0]+8} {a[1]-8} {E1[0]} {E1[1]}
                    """

        elif glyph == "┃":
            a = (random.random() * 10 + 17.5, random.random() * 10 + 20)

            path = f"""M {N1[0]} {N1[1]}
                    Q {a[0]} {a[1]} {S1[0]} {S1[1]}
                    M {N2[0]} {N2[1]}
                    Q {a[0]+10} {a[1]} {S2[0]} {S2[1]}
                    """

        elif glyph == "┳":
            a = (random.random() * 10 + 20, random.random() * 10 + 15)

            path = f"""M {W1[0]} {W1[1]}
                    Q {a[0]} {a[1]} {E1[0]} {E1[1]}
                    M {W2[0]} {W2[1]}
                    C {a[0]-5} {a[1]+10} {a[0]-5} {a[1]+10} {S1[0]} {S1[1]}
                    M {S2[0]} {S2[1]}
                    C {a[0]+5} {a[1]+10} {a[0]+5} {a[1]+10} {E2[0]} {E2[1]}
                    """
        else:
            logging.error(
                f"Strange glyph {glyph} when adding {direction} river to {self.name}"
            )

        road = ET.Element(
            "{http://www.w3.org/2000/svg}path",
            style="fill:none;stroke:#000000;stroke-width:0.264583px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1",
            d=path,
            id=f"road{direction}",
            transform=f"rotate({rotation*90} 25 25)",
        )
        self.features.append(road)

    def draw(self, count: int):
        for n in range(1, count + 1):
            if self.roads:
                for dir in self.roads.split(" "):
                    self.draw_roads(dir)
            if self.city:
                for dir in self.city.split(" "):
                    logging.debug(f"Adding {dir} City to {self.name}")
                    self.features.append(get_gfx(f"City-{dir}.svg"))
            if self.river:
                for dir in self.river.split(" "):
                    self.draw_river(dir)

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

            logging.info(f"Writing to {self.output_dir}/{self.name}-{n:1}.svg")
            self.tile.write(f"{self.output_dir}/{self.name}-{n:1}.svg")

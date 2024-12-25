"""Definition of the various card sets for Carcassonne.

set_names is a dictionary from set label to human readable name
>>> set_names["CAR"]
'Base set'
>>> set_names["HES"]
'Heretics & Shrines'

card_sets is a dictionary from set label to a dictionary describing the set,
that dictionary is from integer to tupple with count and parameters for creating cards

>>> pprint(card_sets["HES"])
{1: (1, {'city': 'N', 'shrine': True}),
 2: (1, {'city': 'N', 'roads': 'S', 'shrine': True}),
 3: (1, {'city': 'N', 'roads': 'EW', 'shrine': True}),
 4: (1, {'shrine': True}),
 5: (1, {'roads': 'S', 'shrine': True}),
 6: (1, {'roads': 'NS', 'shrine': True})}
>>> Card("CAR-14", **card_sets["CAR"][14][1])
<carcassonne.Card object at 0x7f1c8d0e8cd0>

"""

card_sets = {}
set_names = {}

# Base set
# Carcassonne Complete Annotated Rules v7.4 p 24.
set_names["CAR"] = "Base set"
card_sets["CAR"] = {}
card_sets["CAR"][1] = (1, {"city": "ENSW", "shield": True})
card_sets["CAR"][2] = (3, {"city": "ENS"})
card_sets["CAR"][3] = (1, {"city": "ENS", "shield": True})
card_sets["CAR"][4] = (2, {"city": "ENS", "roads": "W", "shield": True})
card_sets["CAR"][5] = (1, {"city": "ENS", "roads": "W"})

card_sets["CAR"][6] = (3, {"city": "EN"})
card_sets["CAR"][7] = (2, {"city": "EN", "shield": True})
card_sets["CAR"][8] = (2, {"city": "N E"})
card_sets["CAR"][9] = (3, {"city": "EN", "roads": "SW"})
card_sets["CAR"][10] = (2, {"city": "EN", "roads": "SW", "shield": True})

card_sets["CAR"][11] = (3, {"city": "N S"})
card_sets["CAR"][12] = (2, {"city": "NS", "shield": True})
card_sets["CAR"][13] = (1, {"city": "NS"})
card_sets["CAR"][14] = (5, {"city": "N"})
card_sets["CAR"][15] = (3, {"city": "N", "roads": "SW"})

card_sets["CAR"][16] = (4, {"city": "N", "roads": "EW"})
card_sets["CAR"][17] = (3, {"city": "N", "roads": "ES"})
card_sets["CAR"][18] = (3, {"city": "N", "roads": "ESW"})
card_sets["CAR"][19] = (4, {"monastery": True})
card_sets["CAR"][20] = (2, {"monastery": True, "roads": "S"})

card_sets["CAR"][21] = (9, {"roads": "SW"})
card_sets["CAR"][22] = (8, {"roads": "SW"})
card_sets["CAR"][23] = (4, {"roads": "ESW"})
card_sets["CAR"][24] = (1, {"roads": "ENSW"})

# Inns & Cathedrals
# Carcassonne Complete Annotated Rules v7.4 p 33.
set_names["IAC"] = "Inns & Cathedrals"
card_sets["IAC"] = {}
card_sets["IAC"][1] = (1, {"monastery": True, "roads": "EW"})
card_sets["IAC"][2] = (2, {"cathedral": True})
card_sets["IAC"][3] = (1, {"city": "W N E S"})
card_sets["IAC"][4] = (1, {"city": "W N E"})
card_sets["IAC"][5] = (2, {"city": "N S", "roads": "EW"})

card_sets["IAC"][6] = (1, {"city": "NW S", "shield": True})
card_sets["IAC"][7] = (1, {"city": "Nes"})
card_sets["IAC"][8] = (1, {"city": "N", "roads": "S"})
card_sets["IAC"][9] = (1, {"city": "NW", "roads": "E"})
card_sets["IAC"][10] = (1, {"city": "EW", "roads": "NS", "shield": True})

card_sets["IAC"][11] = (1, {"city": "NW", "roads": "S", "inn": True})
card_sets["IAC"][12] = (1, {"city": "N", "roads": "SW", "inn": True})
card_sets["IAC"][13] = (1, {"city": "NW", "roads": "ES", "inn": True, "shield": True})
card_sets["IAC"][14] = (1, {"roads": "ESW", "inn": True})
card_sets["IAC"][15] = (1, {"roads": "EW", "inn": True})

card_sets["IAC"][16] = (1, {"roads": "SW", "inn": True})
card_sets["IAC"][17] = (1, {"roads": "SW EN"})

# River
# Carcassonne Complete Annotated Rules v7.4 p X.
set_names["RIV"] = "River"
card_sets["RIV"] = {}
card_sets["RIV"][1] = (1, {"river": "E", "spring": True})
card_sets["RIV"][2] = (1, {"river": "EW"})
card_sets["RIV"][3] = (1, {"river": "SW"})
card_sets["RIV"][4] = (1, {"river": "SW", "roads": "EN"})
card_sets["RIV"][5] = (1, {"river": "EW", "city": "EN"})

card_sets["RIV"][6] = (1, {"river": "EW", "roads": "S", "monastery": True})
card_sets["RIV"][7] = (1, {"river": "EW", "roads": "S", "city": "N"})
card_sets["RIV"][8] = (1, {"river": "EW", "city": "N S"})
card_sets["RIV"][9] = (1, {"river": "EW", "roads": "NS"})
card_sets["RIV"][10] = (1, {"river": "W", "lake": True})

# River II
# Carcassonne Complete Annotated Rules v7.4 p X.
set_names["RII"] = "River II"
card_sets["RII"] = {}
card_sets["RII"][1] = (1, {"river": "S", "spring": True})
card_sets["RII"][2] = (1, {"river": "ENW"})
card_sets["RII"][3] = (1, {"river": "ES", "roads": "NW"})
card_sets["RII"][4] = (1, {"river": "ES", "roads": "EN"})
card_sets["RII"][5] = (1, {"river": "NW", "pigs": True})

card_sets["RII"][6] = (1, {"river": "ES", "city": "NW", "shield": True})
card_sets["RII"][7] = (1, {"river": "NS", "city": "EW"})
card_sets["RII"][8] = (1, {"river": "NS", "city": "W", "roads": "E"})
card_sets["RII"][9] = (1, {"river": "EW", "monastery": True})
card_sets["RII"][10] = (1, {"river": "NS", "inn": True})

card_sets["RII"][11] = (1, {"river": "N", "city": "S", "lake": True})
card_sets["RII"][12] = (1, {"river": "N", "lake": True, "vulcano": True})

# Traders & Builders
# Carcassonne Complete Annotated Rules v7.4 p 39.
set_names["TRB"] = "Traders & Builders"
card_sets["TRB"] = {}
card_sets["TRB"][1] = (1, {"city": "NW E S", "cloth": True})
card_sets["TRB"][2] = (1, {"city": "NW ES", "wine": True})
card_sets["TRB"][3] = (1, {"city": "NS E", "wine": True})
card_sets["TRB"][4] = (1, {"city": "NS E", "cloth": True})
card_sets["TRB"][5] = (1, {"city": "ENS", "grain": True})

card_sets["TRB"][6] = (1, {"roads": "W", "city": "ES N", "grain": True})
card_sets["TRB"][7] = (1, {"roads": "W", "city": "ES N", "cloth": True})
card_sets["TRB"][8] = (1, {"roads": "W", "city": "ENS", "wine": True})
card_sets["TRB"][9] = (1, {"city": "EN", "wine": True})
card_sets["TRB"][10] = (1, {"city": "EN", "grain": True})

card_sets["TRB"][11] = (1, {"roads": "W", "city": "ENsw", "grain": True})
card_sets["TRB"][12] = (1, {"roads": "W", "city": "EN", "grain": True})
card_sets["TRB"][13] = (1, {"roads": "S", "city": "EN", "cloth": True})
card_sets["TRB"][14] = (1, {"roads": "S", "city": "ENsw", "wine": True})
card_sets["TRB"][15] = (1, {"roads": "E S", "city": "NW", "wine": True})

card_sets["TRB"][16] = (1, {"roads": "S W", "city": "ENsw", "cloth": True})
card_sets["TRB"][17] = (1, {"city": "NS", "wine": True})
card_sets["TRB"][18] = (1, {"roads": "W", "city": "NS", "grain": True})
card_sets["TRB"][19] = (1, {"roads": "W", "city": "NS", "wine": True})
card_sets["TRB"][20] = (1, {"roads": "W S", "city": "N"})

card_sets["TRB"][21] = (1, {"roads": "E W", "city": "NS", "wine": True})
card_sets["TRB"][22] = (1, {"roads": "E", "city": "N"})
card_sets["TRB"][23] = (1, {"roads": "ESW", "monastery": True})
card_sets["TRB"][24] = (1, {"roads": "EW NS"})


# The Princess & The Dragon
# Carcassonne Complete Annotated Rules v7.4 p X.
set_names["PRD"] = "The Princess & The Dragon"
card_sets["PRD"] = {}
card_sets["PRD"][1] = (1, {"city": "ENW", "princess": True, "shield": True})
card_sets["PRD"][2] = (1, {"city": "Nsw ES", "princess": True})
card_sets["PRD"][3] = (1, {"city": "NW", "princess": True})
card_sets["PRD"][4] = (1, {"city": "NWes", "princess": True})
card_sets["PRD"][5] = (1, {"roads": "ES", "city": "NW", "princess": True})
card_sets["PRD"][6] = (1, {"roads": "ESW", "city": "N", "princess": True})
card_sets["PRD"][7] = (1, {"roads": "ESW", "dragon": True, "monastery": True})
card_sets["PRD"][8] = (1, {"city": "ENW", "dragon": True, "monastery": True})
card_sets["PRD"][9] = (1, {"roads": "NS", "city": "EW", "dragon": True})
card_sets["PRD"][10] = (1, {"city": "EW", "dragon": True, "shield": True})
card_sets["PRD"][11] = (1, {"city": "NW", "dragon": True})
card_sets["PRD"][12] = (1, {"roads": "ES", "city": "N", "dragon": True})
card_sets["PRD"][13] = (1, {"roads": "SW", "city": "N", "dragon": True})
card_sets["PRD"][14] = (1, {"city": "N", "dragon": True})
card_sets["PRD"][15] = (1, {"roads": "ESW", "dragon": True})
card_sets["PRD"][16] = (1, {"roads": "EW", "dragon": True})
card_sets["PRD"][17] = (1, {"roads": "SW", "dragon": True})
card_sets["PRD"][18] = (1, {"city": "ENW", "portal": True, "shield": True})
card_sets["PRD"][19] = (1, {"roads": "ES", "city": "NW", "portal": True})
card_sets["PRD"][20] = (1, {"roads": "SW", "city": "N", "portal": True})
card_sets["PRD"][21] = (1, {"roads": "ES", "city": "N", "portal": True})
card_sets["PRD"][22] = (1, {"roads": "NW ES", "portal": True})
card_sets["PRD"][23] = (1, {"roads": "ESW", "portal": True})
card_sets["PRD"][24] = (1, {"city": "N E", "vulcano": True})
card_sets["PRD"][25] = (1, {"city": "N", "vulcano": True})
card_sets["PRD"][26] = (1, {"roads": "EW", "vulcano": True})
card_sets["PRD"][27] = (1, {"roads": "SW", "vulcano": True})
card_sets["PRD"][28] = (1, {"roads": "S", "vulcano": True})
card_sets["PRD"][29] = (1, {"vulcano": True})

# Tower
# Carcassonne Complete Annotated Rules v7.4 p X.
set_names["TOW"] = "Tower"
card_sets["TOW"] = {}
card_sets["TOW"][1] = (1, {"city": "N", "roads": "SW", "tower": True})
card_sets["TOW"][2] = (1, {"city": "N", "roads": "EW", "tower": True})
card_sets["TOW"][3] = (1, {"city": "NWes", "roads": "E", "tower": True})
card_sets["TOW"][4] = (1, {"city": "NW", "tower": True})
card_sets["TOW"][5] = (1, {"city": "NS", "roads": "EW", "tower": True})
card_sets["TOW"][6] = (1, {"city": "ENW", "roads": "S", "tower": True})
card_sets["TOW"][7] = (1, {"city": "ENW S", "tower": True, "shield": True})
card_sets["TOW"][8] = (1, {"roads": "SW", "tower": True})
card_sets["TOW"][9] = (1, {"roads": "NW ES", "tower": True})
card_sets["TOW"][10] = (1, {"roads": "NSW", "tower": True})
card_sets["TOW"][11] = (1, {"roads": "ENSW", "tower": True})
card_sets["TOW"][12] = (1, {"tower": True})
card_sets["TOW"][13] = (1, {"city": "E W", "roads": "NS", "tower": True})
card_sets["TOW"][14] = (1, {"tower": True, "monastery": True})
card_sets["TOW"][15] = (2, {"city": "N", "tower": True})
card_sets["TOW"][16] = (1, {"city": "W N", "tower": True})
card_sets["TOW"][17] = (1, {"city": "N", "roads": "S", "tower": True})

# Abbey and Mayor
# Carcassonne Complete Annotated Rules v7.4 p 68 (plus abby tiles from 57).
set_names["ABM"] = "Abbey and Mayor"
card_sets["ABM"] = {}
card_sets["ABM"][1] = (1, {"city": "ENSW", "shield": 2})
card_sets["ABM"][2] = (1, {"city": "EW NS", "shield": True})
card_sets["ABM"][3] = (1, {"city": "NS Ew", "shield": True})
card_sets["ABM"][4] = (1, {"city": "N E", "roads": "W S"})
card_sets["ABM"][5] = (1, {"city": "Nesw", "shield": True})
card_sets["ABM"][6] = (1, {"city": "N", "roads": "W"})
card_sets["ABM"][7] = (1, {"city": "N", "roads": "SW"})
card_sets["ABM"][8] = (1, {"city": "NS", "roads": "EW", "shield": True})
card_sets["ABM"][9] = (1, {"city": "N", "roads": "ES"})
card_sets["ABM"][10] = (1, {"roads": "W"})
card_sets["ABM"][11] = (1, {"roads": "ESW"})
card_sets["ABM"][12] = (1, {"roads": "ENSW", "monastery": True})
card_sets["ABM"][13] = (6, {"city": "ENSW", "abbey": True})

# King and Robber Baron
# Carcassonne Complete Annotated Rules v7.4 p 71.
set_names["KRB"] = "King and Robber Baron"
card_sets["KRB"] = {}
card_sets["KRB"][1] = (1, {"city": "NW NS"})
card_sets["KRB"][2] = (1, {"city": "ENsw", "roads": "W S"})
card_sets["KRB"][3] = (1, {"city": "N", "monastery": True})
card_sets["KRB"][4] = (1, {"city": "N", "roads": "W"})
card_sets["KRB"][5] = (1, {"city": "N", "roads": "W ES"})

# Heretics & Shrines
# Carcassonne Complete Annotated Rules v7.4 p X.
set_names["HES"] = "Heretics & Shrines"
card_sets["HES"] = {}
card_sets["HES"][1] = (1, {"city": "N", "shrine": True})
card_sets["HES"][2] = (1, {"city": "N", "roads": "S", "shrine": True})
card_sets["HES"][3] = (1, {"city": "N", "roads": "EW", "shrine": True})
card_sets["HES"][4] = (1, {"shrine": True})
card_sets["HES"][5] = (1, {"roads": "S", "shrine": True})
card_sets["HES"][6] = (1, {"roads": "NS", "shrine": True})

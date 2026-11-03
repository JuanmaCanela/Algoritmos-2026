# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente 
# a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
# - los índices de cada uno de los árboles deben ser nombre, número y tipo;
# - mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad,
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# - mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# - realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# - mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# - mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# - determinar cuantos Pokémons tienen megaevolucion.
# - determinar cuantos Pokémons tiene forma gigamax.
# - cargue al menos 100 Pokémons.

from tree import BinaryTree

pokemons = [
    {'nombre': 'Gyarados', 'numero': 130, 'tipos': ['Agua', 'Volador'], 'debilidades': ['Eléctrico', 'Roca'], 'mega': True, 'gigamax': False},
    {'nombre': 'Hydreigon', 'numero': 635, 'tipos': ['Siniestro', 'Dragón'], 'debilidades': ['Hielo', 'Lucha', 'Bicho', 'Dragón', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Psyduck', 'numero': 54, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Kyogre', 'numero': 382, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Goodra', 'numero': 706, 'tipos': ['Dragón'], 'debilidades': ['Hielo', 'Dragón', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Aggron', 'numero': 306, 'tipos': ['Acero', 'Roca'], 'debilidades': ['Agua', 'Lucha', 'Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Charmander', 'numero': 4, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Dialga', 'numero': 483, 'tipos': ['Acero', 'Dragón'], 'debilidades': ['Lucha', 'Tierra'], 'mega': False, 'gigamax': False},
    {'nombre': 'Magikarp', 'numero': 129, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Lucario', 'numero': 448, 'tipos': ['Lucha', 'Acero'], 'debilidades': ['Fuego', 'Lucha', 'Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Sandaconda', 'numero': 844, 'tipos': ['Tierra'], 'debilidades': ['Agua', 'Planta', 'Hielo'], 'mega': False, 'gigamax': True},
    {'nombre': 'Bulbasaur', 'numero': 1, 'tipos': ['Planta', 'Veneno'], 'debilidades': ['Fuego', 'Hielo', 'Volador', 'Psíquico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Orbeetle', 'numero': 826, 'tipos': ['Bicho', 'Psíquico'], 'debilidades': ['Fuego', 'Volador', 'Bicho', 'Roca', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': True},
    {'nombre': 'Flareon', 'numero': 136, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Giratina', 'numero': 487, 'tipos': ['Fantasma', 'Dragón'], 'debilidades': ['Hielo', 'Fantasma', 'Dragón', 'Siniestro', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Latias', 'numero': 380, 'tipos': ['Dragón', 'Psíquico'], 'debilidades': ['Hielo', 'Bicho', 'Fantasma', 'Dragón', 'Siniestro', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Cinderace', 'numero': 815, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': True},
    {'nombre': 'Chikorita', 'numero': 152, 'tipos': ['Planta'], 'debilidades': ['Fuego', 'Hielo', 'Veneno', 'Volador', 'Bicho'], 'mega': False, 'gigamax': False},
    {'nombre': 'Urshifu', 'numero': 892, 'tipos': ['Lucha', 'Siniestro'], 'debilidades': ['Lucha', 'Volador', 'Hada'], 'mega': False, 'gigamax': True},
    {'nombre': 'Ivysaur', 'numero': 2, 'tipos': ['Planta', 'Veneno'], 'debilidades': ['Fuego', 'Hielo', 'Volador', 'Psíquico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Kingler', 'numero': 99, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': True},
    {'nombre': 'Steelix', 'numero': 208, 'tipos': ['Acero', 'Tierra'], 'debilidades': ['Fuego', 'Agua', 'Lucha', 'Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Aerodactyl', 'numero': 142, 'tipos': ['Roca', 'Volador'], 'debilidades': ['Agua', 'Eléctrico', 'Hielo', 'Roca', 'Acero'], 'mega': True, 'gigamax': False},
    {'nombre': 'Tyranitar', 'numero': 248, 'tipos': ['Roca', 'Siniestro'], 'debilidades': ['Agua', 'Planta', 'Lucha', 'Tierra', 'Bicho', 'Acero', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Groudon', 'numero': 383, 'tipos': ['Tierra'], 'debilidades': ['Agua', 'Planta', 'Hielo'], 'mega': False, 'gigamax': False},
    {'nombre': 'Flapple', 'numero': 841, 'tipos': ['Planta', 'Dragón'], 'debilidades': ['Hielo', 'Veneno', 'Volador', 'Bicho', 'Dragón', 'Hada'], 'mega': False, 'gigamax': True},
    {'nombre': 'Palkia', 'numero': 484, 'tipos': ['Agua', 'Dragón'], 'debilidades': ['Dragón', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Sharpedo', 'numero': 319, 'tipos': ['Agua', 'Siniestro'], 'debilidades': ['Planta', 'Eléctrico', 'Lucha', 'Bicho', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Zubat', 'numero': 41, 'tipos': ['Veneno', 'Volador'], 'debilidades': ['Eléctrico', 'Hielo', 'Psíquico', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Gastly', 'numero': 92, 'tipos': ['Fantasma', 'Veneno'], 'debilidades': ['Tierra', 'Psíquico', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Latios', 'numero': 381, 'tipos': ['Dragón', 'Psíquico'], 'debilidades': ['Hielo', 'Bicho', 'Fantasma', 'Dragón', 'Siniestro', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Lugia', 'numero': 249, 'tipos': ['Psíquico', 'Volador'], 'debilidades': ['Eléctrico', 'Hielo', 'Roca', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Slowpoke', 'numero': 79, 'tipos': ['Agua', 'Psíquico'], 'debilidades': ['Planta', 'Eléctrico', 'Bicho', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Manectric', 'numero': 310, 'tipos': ['Eléctrico'], 'debilidades': ['Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Machamp', 'numero': 68, 'tipos': ['Lucha'], 'debilidades': ['Volador', 'Psíquico', 'Hada'], 'mega': False, 'gigamax': True},
    {'nombre': 'Dratini', 'numero': 147, 'tipos': ['Dragón'], 'debilidades': ['Hielo', 'Dragón', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Venusaur', 'numero': 3, 'tipos': ['Planta', 'Veneno'], 'debilidades': ['Fuego', 'Hielo', 'Volador', 'Psíquico'], 'mega': True, 'gigamax': True},
    {'nombre': 'Porygon', 'numero': 137, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': False, 'gigamax': False},
    {'nombre': 'Umbreon', 'numero': 197, 'tipos': ['Siniestro'], 'debilidades': ['Lucha', 'Bicho', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Duraludon', 'numero': 884, 'tipos': ['Acero', 'Dragón'], 'debilidades': ['Lucha', 'Tierra'], 'mega': False, 'gigamax': True},
    {'nombre': 'Blaziken', 'numero': 257, 'tipos': ['Fuego', 'Lucha'], 'debilidades': ['Agua', 'Tierra', 'Volador', 'Psíquico'], 'mega': True, 'gigamax': False},
    {'nombre': 'Pikachu', 'numero': 25, 'tipos': ['Eléctrico'], 'debilidades': ['Tierra'], 'mega': False, 'gigamax': True},
    {'nombre': 'Rayquaza', 'numero': 384, 'tipos': ['Dragón', 'Volador'], 'debilidades': ['Hielo', 'Roca', 'Dragón', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Scyther', 'numero': 123, 'tipos': ['Bicho', 'Volador'], 'debilidades': ['Fuego', 'Eléctrico', 'Hielo', 'Volador', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Quaxly', 'numero': 912, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Coalossal', 'numero': 839, 'tipos': ['Roca', 'Fuego'], 'debilidades': ['Agua', 'Lucha', 'Tierra', 'Roca'], 'mega': False, 'gigamax': True},
    {'nombre': 'Fuecoco', 'numero': 909, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Rotom', 'numero': 479, 'tipos': ['Eléctrico', 'Fantasma'], 'debilidades': ['Tierra', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Zoroark', 'numero': 571, 'tipos': ['Siniestro'], 'debilidades': ['Lucha', 'Bicho', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Gallade', 'numero': 475, 'tipos': ['Psíquico', 'Lucha'], 'debilidades': ['Volador', 'Fantasma', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Geodude', 'numero': 74, 'tipos': ['Roca', 'Tierra'], 'debilidades': ['Agua', 'Planta', 'Hielo', 'Lucha', 'Tierra', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Kangaskhan', 'numero': 115, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': True, 'gigamax': False},
    {'nombre': 'Pinsir', 'numero': 127, 'tipos': ['Bicho'], 'debilidades': ['Fuego', 'Volador', 'Roca'], 'mega': True, 'gigamax': False},
    {'nombre': 'Gardevoir', 'numero': 282, 'tipos': ['Psíquico', 'Hada'], 'debilidades': ['Veneno', 'Fantasma', 'Acero'], 'mega': True, 'gigamax': False},
    {'nombre': 'Lapras', 'numero': 131, 'tipos': ['Agua', 'Hielo'], 'debilidades': ['Planta', 'Eléctrico', 'Lucha', 'Roca'], 'mega': False, 'gigamax': True},
    {'nombre': 'Garbodor', 'numero': 569, 'tipos': ['Veneno'], 'debilidades': ['Tierra', 'Psíquico'], 'mega': False, 'gigamax': True},
    {'nombre': 'Swampert', 'numero': 260, 'tipos': ['Agua', 'Tierra'], 'debilidades': ['Planta'], 'mega': True, 'gigamax': False},
    {'nombre': 'Ampharos', 'numero': 181, 'tipos': ['Eléctrico'], 'debilidades': ['Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Snorlax', 'numero': 143, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': False, 'gigamax': True},
    {'nombre': 'Rillaboom', 'numero': 812, 'tipos': ['Planta'], 'debilidades': ['Fuego', 'Hielo', 'Veneno', 'Volador', 'Bicho'], 'mega': False, 'gigamax': True},
    {'nombre': 'Reshiram', 'numero': 643, 'tipos': ['Dragón', 'Fuego'], 'debilidades': ['Tierra', 'Roca', 'Dragón'], 'mega': False, 'gigamax': False},
    {'nombre': 'Glaceon', 'numero': 471, 'tipos': ['Hielo'], 'debilidades': ['Fuego', 'Lucha', 'Roca', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Alakazam', 'numero': 65, 'tipos': ['Psíquico'], 'debilidades': ['Bicho', 'Fantasma', 'Siniestro'], 'mega': True, 'gigamax': False},
    {'nombre': 'Hatterene', 'numero': 858, 'tipos': ['Psíquico', 'Hada'], 'debilidades': ['Veneno', 'Fantasma', 'Acero'], 'mega': False, 'gigamax': True},
    {'nombre': 'Ho-Oh', 'numero': 250, 'tipos': ['Fuego', 'Volador'], 'debilidades': ['Agua', 'Eléctrico', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Sceptile', 'numero': 254, 'tipos': ['Planta'], 'debilidades': ['Fuego', 'Hielo', 'Veneno', 'Volador', 'Bicho'], 'mega': True, 'gigamax': False},
    {'nombre': 'Jolteon', 'numero': 135, 'tipos': ['Eléctrico'], 'debilidades': ['Tierra'], 'mega': False, 'gigamax': False},
    {'nombre': 'Necrozma', 'numero': 800, 'tipos': ['Psíquico'], 'debilidades': ['Bicho', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Alcremie', 'numero': 869, 'tipos': ['Hada'], 'debilidades': ['Veneno', 'Acero'], 'mega': False, 'gigamax': True},
    {'nombre': 'Sableye', 'numero': 302, 'tipos': ['Siniestro', 'Fantasma'], 'debilidades': ['Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Haunter', 'numero': 93, 'tipos': ['Fantasma', 'Veneno'], 'debilidades': ['Tierra', 'Psíquico', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Tyrantrum', 'numero': 697, 'tipos': ['Roca', 'Dragón'], 'debilidades': ['Hielo', 'Lucha', 'Tierra', 'Dragón', 'Acero', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Mimikyu', 'numero': 778, 'tipos': ['Fantasma', 'Hada'], 'debilidades': ['Fantasma', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Inteleon', 'numero': 818, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': True},
    {'nombre': 'Melmetal', 'numero': 809, 'tipos': ['Acero'], 'debilidades': ['Fuego', 'Lucha', 'Tierra'], 'mega': False, 'gigamax': True},
    {'nombre': 'Grimmsnarl', 'numero': 861, 'tipos': ['Siniestro', 'Hada'], 'debilidades': ['Veneno', 'Acero', 'Hada'], 'mega': False, 'gigamax': True},
    {'nombre': 'Mew', 'numero': 151, 'tipos': ['Psíquico'], 'debilidades': ['Bicho', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Magnemite', 'numero': 81, 'tipos': ['Eléctrico', 'Acero'], 'debilidades': ['Fuego', 'Lucha', 'Tierra'], 'mega': False, 'gigamax': False},
    {'nombre': 'Leafeon', 'numero': 470, 'tipos': ['Planta'], 'debilidades': ['Fuego', 'Hielo', 'Veneno', 'Volador', 'Bicho'], 'mega': False, 'gigamax': False},
    {'nombre': 'Zekrom', 'numero': 644, 'tipos': ['Dragón', 'Eléctrico'], 'debilidades': ['Hielo', 'Tierra', 'Dragón', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Jigglypuff', 'numero': 39, 'tipos': ['Normal', 'Hada'], 'debilidades': ['Veneno', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Slowbro', 'numero': 80, 'tipos': ['Agua', 'Psíquico'], 'debilidades': ['Planta', 'Eléctrico', 'Bicho', 'Fantasma', 'Siniestro'], 'mega': True, 'gigamax': False},
    {'nombre': 'Audino', 'numero': 531, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': True, 'gigamax': False},
    {'nombre': 'Vaporeon', 'numero': 134, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Kyurem', 'numero': 646, 'tipos': ['Dragón', 'Hielo'], 'debilidades': ['Lucha', 'Roca', 'Dragón', 'Acero', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Lycanroc', 'numero': 745, 'tipos': ['Roca'], 'debilidades': ['Agua', 'Planta', 'Lucha', 'Tierra', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Altaria', 'numero': 334, 'tipos': ['Dragón', 'Volador'], 'debilidades': ['Hielo', 'Roca', 'Dragón', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Abra', 'numero': 63, 'tipos': ['Psíquico'], 'debilidades': ['Bicho', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Corviknight', 'numero': 823, 'tipos': ['Volador', 'Acero'], 'debilidades': ['Fuego', 'Eléctrico'], 'mega': False, 'gigamax': True},
    {'nombre': 'Ditto', 'numero': 132, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': False, 'gigamax': False},
    {'nombre': 'Arcanine', 'numero': 59, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Absol', 'numero': 359, 'tipos': ['Siniestro'], 'debilidades': ['Lucha', 'Bicho', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Squirtle', 'numero': 7, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': False, 'gigamax': False},
    {'nombre': 'Diancie', 'numero': 719, 'tipos': ['Roca', 'Hada'], 'debilidades': ['Agua', 'Planta', 'Tierra', 'Acero'], 'mega': True, 'gigamax': False},
    {'nombre': 'Dragapult', 'numero': 887, 'tipos': ['Dragón', 'Fantasma'], 'debilidades': ['Hielo', 'Fantasma', 'Dragón', 'Siniestro', 'Hada'], 'mega': False, 'gigamax': False},
    {'nombre': 'Espeon', 'numero': 196, 'tipos': ['Psíquico'], 'debilidades': ['Bicho', 'Fantasma', 'Siniestro'], 'mega': False, 'gigamax': False},
    {'nombre': 'Sylveon', 'numero': 700, 'tipos': ['Hada'], 'debilidades': ['Veneno', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Salamence', 'numero': 373, 'tipos': ['Dragón', 'Volador'], 'debilidades': ['Hielo', 'Roca', 'Dragón', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Copperajah', 'numero': 879, 'tipos': ['Acero'], 'debilidades': ['Fuego', 'Lucha', 'Tierra'], 'mega': False, 'gigamax': True},
    {'nombre': 'Centiskorch', 'numero': 851, 'tipos': ['Fuego', 'Bicho'], 'debilidades': ['Agua', 'Volador', 'Roca'], 'mega': False, 'gigamax': True},
    {'nombre': 'Sprigatito', 'numero': 906, 'tipos': ['Planta'], 'debilidades': ['Fuego', 'Hielo', 'Veneno', 'Volador', 'Bicho'], 'mega': False, 'gigamax': False},
    {'nombre': 'Garchomp', 'numero': 445, 'tipos': ['Dragón', 'Tierra'], 'debilidades': ['Hielo', 'Dragón', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Onix', 'numero': 95, 'tipos': ['Roca', 'Tierra'], 'debilidades': ['Agua', 'Planta', 'Hielo', 'Lucha', 'Tierra', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Meowth', 'numero': 52, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': False, 'gigamax': True},
    {'nombre': 'Glalie', 'numero': 362, 'tipos': ['Hielo'], 'debilidades': ['Fuego', 'Lucha', 'Roca', 'Acero'], 'mega': True, 'gigamax': False},
    {'nombre': 'Toxtricity', 'numero': 849, 'tipos': ['Eléctrico', 'Veneno'], 'debilidades': ['Tierra', 'Psíquico'], 'mega': False, 'gigamax': True},
    {'nombre': 'Heracross', 'numero': 214, 'tipos': ['Bicho', 'Lucha'], 'debilidades': ['Fuego', 'Volador', 'Psíquico', 'Hada'], 'mega': True, 'gigamax': False},
    {'nombre': 'Banette', 'numero': 354, 'tipos': ['Fantasma'], 'debilidades': ['Fantasma', 'Siniestro'], 'mega': True, 'gigamax': False},
    {'nombre': 'Drednaw', 'numero': 834, 'tipos': ['Agua', 'Roca'], 'debilidades': ['Planta', 'Eléctrico', 'Lucha', 'Tierra'], 'mega': False, 'gigamax': True},
    {'nombre': 'Cubone', 'numero': 104, 'tipos': ['Tierra'], 'debilidades': ['Agua', 'Planta', 'Hielo'], 'mega': False, 'gigamax': False},
    {'nombre': 'Beedrill', 'numero': 15, 'tipos': ['Bicho', 'Veneno'], 'debilidades': ['Fuego', 'Volador', 'Psíquico', 'Roca'], 'mega': True, 'gigamax': False},
    {'nombre': 'Scizor', 'numero': 212, 'tipos': ['Bicho', 'Acero'], 'debilidades': ['Fuego'], 'mega': True, 'gigamax': False},
    {'nombre': 'Houndoom', 'numero': 229, 'tipos': ['Siniestro', 'Fuego'], 'debilidades': ['Agua', 'Lucha', 'Tierra', 'Roca'], 'mega': True, 'gigamax': False},
    {'nombre': 'Vulpix', 'numero': 37, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Charizard', 'numero': 6, 'tipos': ['Fuego', 'Volador'], 'debilidades': ['Agua', 'Eléctrico', 'Roca'], 'mega': True, 'gigamax': True},
    {'nombre': 'Gengar', 'numero': 94, 'tipos': ['Fantasma', 'Veneno'], 'debilidades': ['Tierra', 'Psíquico', 'Fantasma', 'Siniestro'], 'mega': True, 'gigamax': True},
    {'nombre': 'Mawile', 'numero': 303, 'tipos': ['Acero', 'Hada'], 'debilidades': ['Fuego', 'Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Appletun', 'numero': 842, 'tipos': ['Planta', 'Dragón'], 'debilidades': ['Hielo', 'Veneno', 'Volador', 'Bicho', 'Dragón', 'Hada'], 'mega': False, 'gigamax': True},
    {'nombre': 'Butterfree', 'numero': 12, 'tipos': ['Bicho', 'Volador'], 'debilidades': ['Fuego', 'Eléctrico', 'Hielo', 'Volador', 'Roca'], 'mega': False, 'gigamax': True},
    {'nombre': 'Metagross', 'numero': 376, 'tipos': ['Acero', 'Psíquico'], 'debilidades': ['Fuego', 'Tierra', 'Fantasma', 'Siniestro'], 'mega': True, 'gigamax': False},
    {'nombre': 'Mewtwo', 'numero': 150, 'tipos': ['Psíquico'], 'debilidades': ['Bicho', 'Fantasma', 'Siniestro'], 'mega': True, 'gigamax': False},
    {'nombre': 'Ninetales', 'numero': 38, 'tipos': ['Fuego'], 'debilidades': ['Agua', 'Tierra', 'Roca'], 'mega': False, 'gigamax': False},
    {'nombre': 'Camerupt', 'numero': 323, 'tipos': ['Fuego', 'Tierra'], 'debilidades': ['Agua', 'Tierra'], 'mega': True, 'gigamax': False},
    {'nombre': 'Tapu Koko', 'numero': 785, 'tipos': ['Eléctrico', 'Hada'], 'debilidades': ['Veneno', 'Tierra'], 'mega': False, 'gigamax': False},
    {'nombre': 'Pidgeot', 'numero': 18, 'tipos': ['Normal', 'Volador'], 'debilidades': ['Eléctrico', 'Hielo', 'Roca'], 'mega': True, 'gigamax': False},
    {'nombre': 'Blastoise', 'numero': 9, 'tipos': ['Agua'], 'debilidades': ['Planta', 'Eléctrico'], 'mega': True, 'gigamax': True},
    {'nombre': 'Togekiss', 'numero': 468, 'tipos': ['Hada', 'Volador'], 'debilidades': ['Eléctrico', 'Hielo', 'Veneno', 'Roca', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Xerneas', 'numero': 716, 'tipos': ['Hada'], 'debilidades': ['Veneno', 'Acero'], 'mega': False, 'gigamax': False},
    {'nombre': 'Eevee', 'numero': 133, 'tipos': ['Normal'], 'debilidades': ['Lucha'], 'mega': False, 'gigamax': True},
    {'nombre': 'Abomasnow', 'numero': 460, 'tipos': ['Planta', 'Hielo'], 'debilidades': ['Fuego', 'Lucha', 'Veneno', 'Volador', 'Bicho', 'Roca', 'Acero'], 'mega': True, 'gigamax': False}
]

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)

    for tipo in pokemon['tipos']:
        arbol_tipo.insert_node(tipo, pokemon)


# funcion para mostrar mejor los datos
def mostrar_pokemon(pokemon):
    print("Nombre:", pokemon['nombre'])
    print("Numero:", pokemon['numero'])
    print("Tipos:", pokemon['tipos'])
    print("Debilidades:", pokemon['debilidades'])
    print("Mega evolucion:", pokemon['mega'])
    print("Gigamax:", pokemon['gigamax'])
    print("-----------------------------")


# funcion extra porque los barridos del modulo no permiten acceder a todos los datos de los nodos necesarios para resolver algunos puntos
def recorrer_inorden(raiz, funcion):
    if raiz is not None:
        recorrer_inorden(raiz.left, funcion)
        funcion(raiz)
        recorrer_inorden(raiz.right, funcion)

# - mostrar todos los datos de un Pokémon a partir de su número y nombre
print("-----")

def buscar_por_numero(numero):
    pokemon = arbol_numero.search(numero)

    if pokemon is not None:
        mostrar_pokemon(pokemon.other_values)
    else:
        print("No se encontro el Pokemon.")

buscar_por_numero(int(input("Ingrese el numero de Pokemon buscado: ")))

def buscar_por_proximidad(nombre):
    nombre = nombre.lower()

    arbol_nombre.proxy_search(nombre)

    print()
    print("Datos completos:")

    def mostrar_coincidencias(nodo):
        if nodo is not None:
            mostrar_coincidencias(nodo.left)

            if nombre in nodo.value.lower():
                mostrar_pokemon(nodo.other_values)

            mostrar_coincidencias(nodo.right)

    mostrar_coincidencias(arbol_nombre.root)

buscar_por_proximidad(input("Ingrese el nombre o parte del nombre: "))

# - mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
print("-----")

def mostrar_por_tipos():
    tipos_buscados = ['Fantasma', 'Fuego', 'Acero', 'Eléctrico']

    for tipo in tipos_buscados:
        print()
        print("Tipo:", tipo)
        vistos = []

        def buscar(nodo):
            if nodo.value == tipo:
                pokemon = nodo.other_values

                if pokemon['numero'] not in vistos:
                    print("-", pokemon['nombre'])
                    vistos.append(pokemon['numero'])

        recorrer_inorden(arbol_tipo.root, buscar)

mostrar_por_tipos()

# - realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("-----")

print()
print("Pokemons ordenados por numero:")
arbol_numero.inorden()

print()
print("Pokemons ordenados por nombre:")
arbol_nombre.inorden()

print()
print("Pokemons ordenados por nivel por nombre:")
arbol_nombre.by_level()

# - mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
print("-----")

def mostrar_debiles():
    nombres = ['Jolteon', 'Lycanroc', 'Tyrantrum']
    tipos = []

    for nombre in nombres:
        pokemon = arbol_nombre.search(nombre)

        if pokemon is not None:
            for tipo in pokemon.other_values['tipos']:
                if tipo not in tipos:
                    tipos.append(tipo)
    print()
    print("Tipos de los Pokemon buscados:", tipos)
    print()
    print("Pokemon debiles frente a ellos:")

    def buscar(nodo):
        pokemon = nodo.other_values

        for tipo in tipos:
            if tipo in pokemon['debilidades']:
                print(pokemon['nombre'])
                break

    recorrer_inorden(arbol_nombre.root, buscar)

mostrar_debiles()

# - mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
print("-----")

def mostrar_cantidad_por_tipo():
    cantidades = {}

    def contar(nodo):
        if nodo.value not in cantidades:
            cantidades[nodo.value] = 1
        else:
            cantidades[nodo.value] += 1

    recorrer_inorden(arbol_tipo.root, contar)

    print()
    print("Cantidad de Pokemon por tipo:")
    for tipo, cantidad in cantidades.items():
        print(tipo, ":", cantidad)

mostrar_cantidad_por_tipo()

# - determinar cuantos Pokémons tienen megaevolucion.
print("-----")

def contar_mega():
    cantidad = 0

    def contar(nodo):
        nonlocal cantidad

        if nodo.other_values['mega']:
            cantidad += 1

    recorrer_inorden(arbol_nombre.root, contar)

    print("Cantidad de Pokemon con Mega Evolucion:", cantidad)

contar_mega()

# - determinar cuantos Pokémons tiene forma gigamax.
print("-----")

def contar_gigamax():
    cantidad = 0

    def contar(nodo):
        nonlocal cantidad

        if nodo.other_values['gigamax']:
            cantidad += 1

    recorrer_inorden(arbol_nombre.root, contar)

    print("Cantidad de Pokemon con Gigamax:", cantidad)

contar_gigamax()

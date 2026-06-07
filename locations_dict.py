from icecream import ic

class Location(list):
    def __init__[T](self, name: str, xy: tuple[T, T]) -> None:
        super().__init__()
        self.append(name)
        self.append(xy)

    def get_name(self) -> str:
        return self[0]

    def get_coords[T](self) -> tuple[T, T]:
        return self[1]

class Locations:
    def __init__(self) -> None:
        self.locations: dict[str, Location] = {'a': Location("Alpha", (377 ,307)),
                                               'b': Location("Bravo", (334, 229)),
                                               'c': Location("Charlie", (377, 226)),
                                               'd': Location("Delta", (419, 228)),
                                               'e': Location("Echo", (459, 270)),
                                               'f': Location("Foxtrot", (459, 304)),
                                               'g': Location("Golf", (460, 345)),
                                               'h': Location("Hotel", (418, 392)),
                                               'i': Location("India", (375, 394)),
                                               'j': Location("Juliett", (335, 393)),
                                               'k': Location("Kilo", (296, 345)),
                                               'l': Location("Lima", (295, 308)),
                                               'm': Location("Mike", (293, 266)),
                                               'n': Location("November", (253, 186)),
                                               'o': Location("Oscar", (500, 185)),
                                               'p': Location("Papa", (500, 432)),
                                               'q': Location("Quebec", (252, 433)),
                                               'r': Location("Romeo", (173, 105)),
                                               's': Location("Sierra", (377, 105)),
                                               't': Location("Tango", (584,101)),
                                               'u': Location("Uniform", (588, 313)),
                                               'v': Location("Victor", (588, 510)),
                                               'w': Location("Whiskey", (377, 515)),
                                               'x': Location("XRay", (172, 511)),
                                               'y': Location("Yankee", (172, 308)),
                                               'tr1': Location("Transformer 1", (544, 388)),
                                               'tr2': Location("Transformer 2", (157, 404)),
                                               'tr3': Location("Transformer 3", (218, 112))}


def main():
    locations = Locations()

    ic(locations.locations)

if __name__ == '__main__':
    main()
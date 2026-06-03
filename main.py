from PIL import Image
from PIL import ImageDraw
from os import system
from locations_dict import Locations, Location
from collections.abc import Callable

class Drawer:
    def __init__(self, mapfile: str) -> None:
        self._path: str = mapfile
        self._raw_map_image: Image.Image = Image.open(mapfile)

        self._locations: Locations = Locations()

        self._locations_names_queued: list[str] = []

        self._commands: dict [str, Callable] = {'a': self.add_loop,
                                                'r': self.rasterize_map,
                                                's': self.show_locations,
                                                'q': quit}

        self._current_queue: list[Location] = [self._locations.locations['a'][1]] #self._locations['alpha'][1] = (377 ,307)

    @staticmethod
    def clear_screen() -> None:
        system('cls')

    def show_locations(self) -> None:
        self.clear_screen()
        for location in self._locations_names_queued:
            print(location)
        input("\nPress Enter to continue...")

    def add_loop(self) -> None:
        user_input = 'x'

        while user_input:
            user_input = input("Location to add (leave blank to go back): ").lower()

            try:
                self.clear_screen()
                self._current_queue.append(self._locations.locations[user_input][1]) #self._locations[ui][1] = tuple[int, int]
                location_name: str = self._locations.locations[user_input][0] #self._locations[ui][0] = str
                self._locations_names_queued.append(location_name)
                print(f'{location_name} added to queue')

            except KeyError:
                self.clear_screen()
                print("Not a valid location")


    @staticmethod
    def quick_vector_sort(vector):
        return sum(x*x for x in vector)

    def rasterize_map(self) -> None:
        map_draw: ImageDraw.Draw = ImageDraw.Draw(self._raw_map_image)

        self._current_queue.sort(key=self.quick_vector_sort)

        self._current_queue = self._current_queue[::-1]

        self._current_queue.append(self._locations.locations['a'][1]) #read comments above for magic number definition

        map_draw.polygon(xy=self._current_queue, outline="green", width=2)

        self._raw_map_image.show()

        self._locations_names_queued.clear()
        self._current_queue.clear()

        self._current_queue.append(self._locations.locations['a'][1]) #read comments above for magic number definition

        self._raw_map_image = Image.open(self._path)

    def mainloop(self) -> None:
        while True:
            self.clear_screen()
            user_input: str = input(f'[A]dd locations\n[R]asterize map\n[S]how queued locations\n[Q]uit\n\nCommand: ').lower()

            try:
                self._commands[user_input]()

            except KeyError:
                self.clear_screen()
                print("Invalid command")


def main() -> None:
    d: Drawer = Drawer('./rawmap.png')

    d.mainloop()

if __name__ == '__main__':
    main()
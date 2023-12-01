from utils import helpers


class StringInput():
    def __init__(self, day: int, year: int) -> None:
        self.input = helpers.get_input(day, year)

    def print_input(self):
        print(self.input)
        print(f"\n# of characters: {len(self.input)}")

    @classmethod
    def return_input(cls, day: int, year: int):
        instance = cls(day, year)
        return instance, instance.input


class SplitStringInput(StringInput):
    def __init__(self, day: int, year: int) -> None:
        super().__init__(day, year)
        self.input = list(self.input.splitlines())

    def print_input(self):
        for string in self.input:
            print(string)
        print(f"\n# of lines: {len(self.input)}")


class IntInput(StringInput):
    def __init__(self, day: int, year: int) -> None:
        super().__init__(day, year)
        self.input = int(self.input)

    def print_input(self):
        print(self.input)


class SplitIntInput(StringInput):
    def __init__(self, day: int, year: int) -> None:
        super().__init__(day, year)
        self.input = [int(i) for i in self.input.splitlines()]

    def print_input(self):
        for integer in self.input:
            print(integer)
        print(f"\n# of lines: {len(self.input)}")

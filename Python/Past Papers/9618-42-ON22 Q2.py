class Character:
    def __init__(self, name: str, x_coordinate: int, y_coordinate: int):
        self._name = name
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

    def GetName(self):
        return self._name

    def GetX(self):
        return self._x_coordinate

    def GetY(self):
        return self._y_coordinate

    def ChangePosition(self, XChange: int, YChange: int):
        self._x_coordinate += XChange
        self._y_coordinate += YChange

def find_character(characters, search_name):
    for i, character in enumerate(characters):
        if character.GetName() == search_name:
            return i
    return -1

def display_character_info(character):
    print(f"{character.GetName()} has changed coordinates to X = {character.GetX()} and Y = {character.GetY()}")

characters = []
with open("Characters.txt", "r") as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 3):
        name = lines[i]
        x = int(lines[i + 1])
        y = int(lines[i + 2])
        characters.append(Character(name, x, y))

while True:
    user_input = input("Enter a character's name: ")
    index = find_character(characters, user_input)
    if index != -1:
        print(f"Character '{user_input}' found at index {index}")
        break
    else:
        print(f"Character '{user_input}' not found. Please try again.")

character = characters[index]
while True:
    move = input("Enter a valid move (A, W, S, or D): ").upper()
    if move in ["A", "W", "S", "D"]:
        if move == "A":
            character.ChangePosition(-1, 0)
        elif move == "W":
            character.ChangePosition(0, 1)
        elif move == "S":
            character.ChangePosition(0, -1)
        elif move == "D":
            character.ChangePosition(1, 0)
        display_character_info(character)
    else:
        print("Invalid move. Please try again.")
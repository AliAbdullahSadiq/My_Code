class HiddenBox:
    def __init__(self, BoxName, Creator, DateHidden, GameLocation):
        self._box_name = BoxName
        self._creator = Creator
        self._date_hidden = DateHidden
        self._game_location = GameLocation
        self._last_finds = [['', ''] for _ in range(10)]
        self._active = False

    def GetBoxName(self):
        return self._box_name

    def GetGameLocation(self):
        return self._game_location
    
class PuzzleBox(HiddenBox):
    def __init__(self, PuzzleText, Solution):
        self.__puzzle_text = PuzzleText
        self.__solution = Solution

TheBoxes = [] * 10000 # type HiddenBox

def NewBox(TheBoxes):
    ThisBox = input('Input box name: ')
    ThisCreator = input('Input creator name: ')
    ThisDate = input('Input the date: ')
    ThisGame = input('Input game: ')
    TheBoxes.append(HiddenBox(ThisBox, ThisCreator, ThisDate, ThisGame))
    return TheBoxes

TheBoxes = NewBox(TheBoxes)
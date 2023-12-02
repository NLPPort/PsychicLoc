import pyrandonaut


class randomNauto:
    def __init__(self):
        self.my_latitude = 0
        self.my_longitude = 0

    def useMyDefaultLoc(self) -> "randomNauto":
        self.my_latitude = 0
        self.my_longitude = 0
        return self

    def finalRes(self):
        res = pyrandonaut.get_coordinate(self.my_latitude, self.my_longitude)
        print(f"Now you can go to here {res}")

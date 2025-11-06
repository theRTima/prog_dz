class TimurCheck:

    @staticmethod
    def is_timur(name):
        return name == "Timur"

name_test = input()
print(TimurCheck.is_timur(name_test))

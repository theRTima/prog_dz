class TimurCheck:

    @staticmethod
    def is_timur(name):
        return name == "Timur"

print(f"\nправильное имя? {TimurCheck.is_timur("Timur")}")
print(f"\nправильное имя? {TimurCheck.is_timur("Alex")}")
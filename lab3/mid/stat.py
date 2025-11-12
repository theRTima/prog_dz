class Name:

    @staticmethod
    def is_timur(name):
        return name == "Timur"

print(f"\nправильное имя? {Name.is_timur("Timur")}")
print(f"\nправильное имя? {Name.is_timur("Alex")}")
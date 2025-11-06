from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self,title):
        self.title = title
    
    @abstractmethod
    def restriction(self):
        pass
    
    def get_title(self):
        return self.title

class FPS(Game):
    def restriction(self):
        return f"{self.title} Рейтинг: 18+"

class Sandbox(Game):
    def restriction(self):
        return f"{self.title} Рейтинг: 6+"

class GameFactory:
    @staticmethod
    def new_game(genre,title):
        if genre == "fps":
            return(FPS(title))
        elif genre == "sandbox":
            return(Sandbox(title))
        else:
            print(f"Неизвестный жанр - {genre}")

first_fps = GameFactory.new_game("fps","Counter_Strike")
first_sandbox = GameFactory.new_game("sandbox","WorldBox")

print(f"{first_fps.restriction()}")
print(f"{first_sandbox.restriction()}")
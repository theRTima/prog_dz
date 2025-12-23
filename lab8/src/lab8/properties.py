class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("get radius")
        return self._radius

def main():
    circle1 = Circle(40)
    print(circle1.radius)

if __name__ == '__main__':
    main()
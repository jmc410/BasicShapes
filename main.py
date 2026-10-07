from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    """Creates and shows several shapes."""
    shapes = [
        Circle(0, 0, 5),
        Circle(2, 3, 3, "Circle 2"),
        Rectangle(10, 5),
        Rectangle(4, 8, "Rectangle 2"),
        Square(6)
    ]

    print("Shapes:")
    for shape in shapes:
        print(shape.name, shape.area)

    print("\nChanging the circle radius:")
    shapes[0].radius = 8
    print(shapes[0].name, shapes[0].radius, shapes[0].area)

    print("\nChanging the rectangle:")
    shapes[2].length = 20
    shapes[2].width = 10
    print(shapes[2].name, shapes[2].length, shapes[2].width, shapes[2].area)

    print("\nChanging the square:")
    shapes[4].side = 10
    print(
        shapes[4].name,
        shapes[4].side,
        shapes[4].length,
        shapes[4].width,
        shapes[4].area
    )


if __name__ == "__main__":
    main()

from geometry import RegularPolygon


def main():
    # Create a polygon with default attributes
    polygon1 = RegularPolygon()
    # Print the perimeter and area of polygon 1
    print(f"Perimeter of polygon1 is {polygon1.getPerimeter():,.2f} units")
    print(f"Area of polygon1 is {polygon1.getArea():,.2f} square units\n")

    # Create a polygon with 6 sides, and length if each side is 4 units
    polygon2 = RegularPolygon(6, 4)
    # Print the perimeter and area of polyon 2
    print(f"Perimeter of polygon2 is {polygon2.getPerimeter():,.2f} units")
    print(f"Area of polygon2 is {polygon2.getArea():,.2f} square units\n")

    # Create a polygon with 10 sides, length if each side is 4 units, x coordinate of center is 5.6 and y coordinate of center is 7.8
    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)
    print(f"Perimeter of polygon3 is {polygon3.getPerimeter():,.2f} units")
    print(f"Area of polygon3 is {polygon3.getArea():,.2f} square units")



if __name__ == "__main__":
    main()
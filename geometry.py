from math import tan, pi

class RegularPolygon:
    """ An equilateral and equiangular polygon """
    def __init__(self, numberOfSides=3, lengthOfSide=1.0, xCoord=0.0, yCoord=0.0):
        """ Initialize all instance variables as private with default values """
        self.__n = numberOfSides
        self.__side = lengthOfSide
        self.__x =  xCoord
        self.__y = yCoord

    def __str__(self):
        """  When printing object, print its attributes instead """
        return f"Number of Sides: {self.__n}, Length of each side: {self.__side}, Center x coordinate: {self.__x}, Center y coordinate: {self.__y}"

    # Accessor methods (getters)
    def getN(self):
        """ Get the number of sides """
        return self.__n

    def getSide(self):
        """ Get the length of the sides """
        return self.__side

    def getX(self):
        """ Get the x coordinate of the center """
        return self.__x

    def getY(self):
        """ Get the y coordinate of the center """
        return self.__y

        
    # Mutator methods (setters with input checking)
    def setN(self,numberOfSides):
        """ Set a new number of sides """
        # If the given number of sides is an int greater than 2, then set it as the number of sides of the polygon
        if isinstance(numberOfSides, int) and numberOfSides > 2:
            self.__n = numberOfSides
        # Raise an error if the given number of sides is invalid
        else:
            raise ValueError("Number of sides wasn't changed: Number of sides must be an integer greater than 2")

    def setSide(self, lengthOfSide):
        """ Set a new length of the sides """
        # If the given length is an int, then convert it to float
        if isinstance(lengthOfSide, int):
            lengthOfSide = float(lengthOfSide)

        # If the given length of side is positive float, then set it as the length of each side of the polygon
        if isinstance(lengthOfSide, float) and lengthOfSide > 0:
            self.__side = lengthOfSide

        # Raise an error if the given length of side is invalid
        else:
            raise ValueError("Length of sides wasn't changed: Length of sides must be a number greater than 0")

    def setX(self, xCoord):
        """ Set a new x coordinate of the center """
        # If the given x coordinate is an int, then convert it to float
        if isinstance(xCoord, int):
            xCoord = float(xCoord)
        
        # If the given x coordinate is valid, then set it as the x coordinate of the polygon
        if isinstance(xCoord, float):
            self.__x = xCoord

        # Raise an error if the given x coordinate is invalid
        else:
            raise ValueError("X-coordinate wasn't changed: x coordinate must be a number")

    def setY(self, yCoord):
        """ Set a new y coordinate """
        # If the given y coordinate is an int, then convert it to float
        if isinstance(yCoord, int):
            yCoord = float(yCoord)
        
        # If the given y coordinate is valid, then set it as the y coordinate of the polygon
        if isinstance(yCoord, float):
            self.__y = yCoord

        # Raise an error if the given y coordinate is invalid
        else:
            raise ValueError("Y-coordinate wasn't changed: y coordinate must be a number")


    def getPerimeter(self):
        """ Returns the permineter of the polygon (by multiplying number of sides and length of each sides) """
        return self.__n * self.__side

    def getArea(self):
        """ Returns the area of the polygon (using a complex formula given in the pdf) """
        area = ( (self.__n * self.__side**2) / (4 * tan(pi / self.__n) ) )
        return area




# TEST (suggest using the uploaded test.py for testing)
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
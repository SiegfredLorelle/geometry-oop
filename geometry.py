from math import tan, pi

class RegularPolygon():
    """ TODO """
    def __init__(self, numberOfSides=3, lengthOfSide=1.0, xCoord=0.0, yCoord=0.0):
        self._n = numberOfSides
        self._side = lengthOfSide
        self._x =  xCoord
        self._y = yCoord

    def __str__(self):
        return f"Number of Sides: {self._n}, Length of a side: {self._side}, Center x coordinate: {self._x}, Center y coordinate: {self._y}"


    def getN(self):
        return self._n

    def setN(self,numberOfSides):
        """ TODO """
        if isinstance(numberOfSides, int) and numberOfSides > 2:
            self._n = numberOfSides
        else:
            raise ValueError("Number of sides wasn't changed: Number of sides must be an integer greater than 2")

    def getSide(self):
        return self._side

    def setSide(self, lengthOfSide):
        if isinstance(lengthOfSide, int):
            lengthOfSide = float(lengthOfSide)

        if isinstance(lengthOfSide, float) and lengthOfSide > 0:
            self._side = lengthOfSide
        else:
            raise ValueError("Length of sides wasn't changed: Length of sides must be a number greater than 0")

    def getX(self):
        return self._x

    def setX(self, xCoord):
        if isinstance(xCoord, int):
            xCoord = float(xCoord)
        
        if isinstance(xCoord, float):
            self._x = xCoord

        else:
            raise ValueError("X-coordinate wasn't changed: x coordinate must be a number")


    def getPerimeter(self):
        """ Return the permineter of the polygon """
        return self._n * self._side

    def getArea(self):
        """ Returns the area of the polygon """
        area = ((self._n * self._side**2) / (4 * tan(pi / self._n)))
        return area


# shape1 = RegularPolygon()
# shape1.setX(3)
# shape1.setSide(5.25)
# shape1.setN(4)
# print(shape1)
# print(f"Area: {shape1.getArea():,.2f}       Perimeter: {shape1.getPerimeter()}")



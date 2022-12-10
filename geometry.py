class RegularPolygon():
    """ TODO """
    def __init__(self, number_of_sides=3, length_of_side=1.0, x_coord=0.0, y_coord=0.0):
        self._n = number_of_sides
        self._side = length_of_side
        self._x = x_coord
        self._y = y_coord

    def __str__(self):
        return f"Number of Sides: {type(self._n)}, Length of a side: {self._side}, Center x coordinate: {self._x}, Center y coordinate: {self._y}"


    def get_n(self):
        return self._n

    def set_n(self, number_of_sides):
        """ TODO """
        if isinstance(number_of_sides, int) and number_of_sides > 2:
            self._n = number_of_sides
        else:
            print("No changes were made: Number of sides must be an integer greater than 2")

    def get_side(self):
        return self._side

    def set_side(self, length_of_side):
        if isinstance(length_of_side, int):
            length_of_side = float(length_of_side)

        if isinstance(length_of_side, float) and length_of_side > 0:
            self._side = length_of_side
        else:
            print("No chnages were made: Length of side must greater than 0")

    
    
    

        



        




shape1 = RegularPolygon()
# shape1.set_n(4.6)
shape1.set_side("a")
print(shape1.get_side())


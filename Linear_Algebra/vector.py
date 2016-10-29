"""http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html - to know more about str and eq ... str is used to know what needs to be done when print method is called and _eq_ is to find equal to """

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


my_vector = Vector([1,2,3])
print my_vector
my_vector2 = Vector([1,2,3])
b = (my_vector2==my_vector)
print b


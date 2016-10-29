"""http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html - to know more about str and eq ... str is used to know what needs to be done when print method is called and _eq_ is to find equal to
and http://stackoverflow.com/questions/16548584/adding-two-tuples-elementwise for add - i have used izip since sub is not supported using map and operator  """
#from itertools import izip
from operator import add,sub,mul
import math
"""https://www.tutorialspoint.com/python/number_pow.htm - for computing square"""
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

    def __add__(self,other):
        a=self.coordinates
        b=other.coordinates
        c=(map(add,a,b))
        print 'Vector addition is'
        return Vector(c)

    def __sub__(self,other):
        a=self.coordinates
        b=other.coordinates
        c=(map(sub,a,b))
        print 'Vector subtraction is'
        return Vector(c)
   
    """ This is multipication of vector function
    def __mul__(self,other):
        a=self.coordinates
        b=other.coordinates
        c=(map(mul,a,b))
        print 'Vector multipication is'
        return Vector(c)"""

    def scalar_mul(self,other):
        c=[other*x for x in self.coordinates] 
        print 'Vector multiplication is'
        return Vector(c)  

    def magnitude(self):
        c=math.sqrt(sum(math.pow(x,2) for x in self.coordinates))
        print 'Squared vector is'
        return c
    def normalized(self):
        d=self.magnitude()
        e=self.scalar_mul(1/d)
        return e  

my_vector_mag_1 = Vector([-0.221,7.437])
my_vector_mag_2 = Vector([8.813,-1.331,-6.247])
my_vector_nor_1 = Vector([5.581,-2.136])
my_vector_nor_2 = Vector([1.996,3.108,-4.554])


square_vector=my_vector_mag_1.magnitude()
print square_vector

square_vector2=my_vector_mag_2.magnitude()
print square_vector2

normalized_vector=my_vector_nor_1.normalized()
print normalized_vector


normalized_vector2=my_vector_nor_2.normalized()
print normalized_vector2

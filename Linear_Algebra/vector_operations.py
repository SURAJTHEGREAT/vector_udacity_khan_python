"""http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html - to know more about str and eq ... str is used to know what needs to be done when print method is called and _eq_ is to find equal to
and http://stackoverflow.com/questions/16548584/adding-two-tuples-elementwise for add - i have used izip since sub is not supported using map and operator  """
#from itertools import izip
from operator import add,sub,mul
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

my_vector_add_1 = Vector([8.218,-9.341])
my_vector_add_2 = Vector([-1.129,2.111])
my_vector_sub_1 = Vector([7.119,8.215])
my_vector_sub_2 = Vector([-8.223,0.878])
my_vector_mul_1 = Vector([1.671,-1.012,-0.318])
mul_scalar=7.41
added_vector=my_vector_add_1+my_vector_add_2

print added_vector
sub_vector=my_vector_sub_1-my_vector_sub_2

print sub_vector

mul_vector=my_vector_mul_1.scalar_mul(mul_scalar)
print mul_vector


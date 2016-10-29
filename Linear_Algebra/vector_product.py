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
        
        return Vector(c)

    def __sub__(self,other):
        a=self.coordinates
        b=other.coordinates
        c=(map(sub,a,b))
        
        return Vector(c)
   
    """ This is multipication of vector function """
    def multiply(self,Y):
        
        c=(sum(a*b for a,b in zip(self.coordinates,Y.coordinates)))
        
        return c

    def scalar_mul(self,other):
        c=[other*x for x in self.coordinates] 
       
        return Vector(c)  

    def magnitude(self):
        c=math.sqrt(sum(math.pow(x,2) for x in self.coordinates))
        
        return c
    def normalized(self):
        d=self.magnitude()
        e=self.scalar_mul(1/d)
        return e  
    def angle(self,Y):
        a=self.multiply(Y)
        d=self.magnitude()
        e=Y.magnitude()
        f=a/(d*e)
        g=math.acos(f)
        return g 
        
my_vector_prod_1 = Vector([7.887,4.138])
my_vector_prod_2 = Vector([-8.802,6.776])
my_vector_prod_3 = Vector([-5.955,-4.904,-1.874])
my_vector_prod_4 = Vector([-4.496,-8.755,7.103])


my_vector_ang_1 = Vector([3.183,-7.627])
my_vector_ang_2 = Vector([-2.668,5.319])
my_vector_ang_3 = Vector([7.35,0.221,5.188])
my_vector_ang_4 = Vector([2.751,8.259,3.985])

my_vector_test=Vector([1,2,3])

dot_product1=my_vector_prod_1.multiply(my_vector_prod_2)
print dot_product1


dot_product2=my_vector_prod_3.multiply(my_vector_prod_4)
print dot_product2

angle1=my_vector_ang_1.angle(my_vector_ang_2)
print angle1

angle2=my_vector_ang_3.angle(my_vector_ang_4)
angle_degree=math.degrees(angle2)
print angle_degree

dot_product_zero=my_vector_test.multiply(my_vector_test)
print dot_product_zero


angle2=my_vector_test.angle(my_vector_test)
angle_degree=math.degrees(angle2)
print angle_degree



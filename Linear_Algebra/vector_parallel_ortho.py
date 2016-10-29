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
        


vVector1=Vector([-7.579,-7.88]);
wVector1=Vector([22.737,23.64]);

vVector2=Vector([-2.209,9.97,4.172]);
wVector2=Vector([-9.231,-6.639,-7.245]);

vVector3=Vector([-2.238,-7.284,-1.214]);
wVector3=Vector([-1.821,1.072,-2.94]);

vVector4=Vector([2.118,4.827]);
wVector4=Vector([0,0]);



angle1=vVector1.angle(wVector1)
angle_degree1=math.degrees(angle1)
print ("v1 angle is %s",angle_degree1)


angle2=vVector2.angle(wVector2)
angle_degree2=math.degrees(angle2)
print ("v1 angle is %s",angle_degree2)



angle3=vVector3.angle(wVector3)
angle_degree3=math.degrees(angle3)
print ("v3 angle is %s",angle_degree3)


angle4=vVector4.angle(wVector4)
angle_degree4=math.degrees(angle4)
print ("v4 angle is %s",angle_degree4)






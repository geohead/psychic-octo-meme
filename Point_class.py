'''
    This an attempt to create a base class called Point.

'''

__authour__ = "Boneya Hassan<bonairhassan@gmail.com>"




from math import atan, atan2, cos, degrees, pi, radians,  sqrt, sin



class Point (object):
    
    ''' This point defines how we represent a point in 2D cartesian plane.
With the necessary propeties and methods.'''
    
    
    __slots__ = ('x','y')
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self,p):

<<<<<<< HEAD
        if  isinstance (p,Point):
=======
        if not isinstance(p,Point):
            raise TypeError("Not an instance of class Point.")
        else:
>>>>>>> a9b3d3ae068a4cc470476cdc0aa1cb899a579794
            return self.x == p.x and self.y == p.y
        else:
            return NotImplemented

    def __add__(self,p):


        if isinstance(p,Point):

        if not isinstance(p,Point):
            raise TypeError("Not an instance of class Point.")
        else:

            return Point (self.x + p.x, self.y + p.y)
        else:
            return NotImplemented
        
    def __sub__(self,p):


        if isinstance(p,Point):

        if  not isinstance(p,Point):
            raise TypeError("Not an instance of class Point.")
        else:

            return Point (self.x - p.x, self.y - p.y)
        else:
            return NotImplemented


    def __mul__(self, m):

        if (isinstance(m,int) or (isinstance(m,float))):
            return Point (self.x * m, self.y * m)
        else:
            return NotImplemented

    def __rmul__(self,m):

        return self.__mul__(m)
    

    def __truediv__(self, m):

        if (isinstance(m,int) or (isinstance(m,float))):
            return Point (self.x / m, self.y / m)
        else:
            return NotImplemented


    def __neg__(self):

        return Point (-self.x, -self.y)

    def __abs__(self):

        return Point (abs(self.x), abs(self.y))

    def __round__(self,m):

        return  Point (round(self.x,m),round (self.y,m))

        
    def __getitem__(self,item):
        if item ==0:
            return self.x
        elif item == 1:
            return self.y
        else:
            return None

    def __len__(self):
        return 2

    def __str__(self):
        return "({} {})".format(self.x, self.y)

    def __repr__(self):
       return  ' {} ({} {})'.format('Point', self.x, self.y )
    

    def offset(self, dx,dy):
        return Point (self.x + dx, self.y + dy)
    

    def next_point(self, distance,bearing):
        
        dy = cos(radians(bearing)) * distance
        dx = sin(radians(bearing)) * distance

        return (self.x + dx, self.y + dy)

    

    def distance_from_point (self,p):
        ''' Returns the straight line distance between the two points, p1 and p2 of the Point class.'''
        return sqrt(((self.x - p.x)**2) + ((self.y -p.y)**2))
    
    def travelling_distance (self, p):
        "Returns the distance btn two points following a line network (Manhattan Distance)"
        return ((abs(p.x - self.x)) +(abs(p.y - self.y)))
    

    def angle_from (self,p):
        ''' The return value is the angle in the Cartesian plane formed by the x-axis,
            and a vector starting from the p1, and terminating at the second point, p2 .'''

        dx = (p.x - self.x)
        dy = (p.y - self.y)

        if dy == 0 and dx >0:
            return 0

        if dy == 0 and dx<0:
            return 180
        
        if dy >0 and dx == 0:
            return 90
        
        if dy <0 and dx == 0:
            return 270
        
        if dy == 0 and x == 0:
                return 0
        
        
        theta = atan2(dy,dx)
        angle =  degrees (theta)

<<<<<<< HEAD
=======
        # condtional statement to workout which quadrant an angle fall from 1-4 resp
>>>>>>> a9b3d3ae068a4cc470476cdc0aa1cb899a579794
        if theta > 0 and theta <(pi/2):
            return  angle
        if theta > (pi/2) and theta <= pi:
            return angle
        if theta > (-pi) and theta < (-pi/2):
            return (angle +360 )
        if theta > (-pi/2) and theta < 0:
            return (angle +360)

    def bearing_from (self,p):
        ''' The return value of bearing (angle from measurd from north),
            and a vector starting from the p1, and terminating at the second point, p2 .'''

        dx = (p.x - self.x)
        dy = (p.y - self.y)

        if dy == 0 and dx >0:
            return 180

        if dy == 0 and dx<0:
            return 270
        
        if dy >0 and dx == 0:
            return 0
        
        if dy <0 and dx == 0:
            return 180
        
        if dy == 0 and x == 0:
                return 0
        
        
        theta = atan2(dx,dy)
        angle =  degrees (theta)

        # condtional statement to workout which quadrant an angle fall from 1-4 resp.
        if theta > 0 and theta <(pi/2):
            return  angle
        if theta > (pi/2) and theta <= pi:
            return  angle
        if theta > (-pi) and theta < (-pi/2):
            return  (angle +360 )
        if theta > (-pi/2) and theta < 0:
            return  (angle +360)



    
##################################################

def main ():
    if __name__ =='__main__':
        p1= Point (2,3)
        p2= Point(4,14)
        p3= Point (8,9)
        
        print (p1)
        print (p2)
        print (p3)
    
        print (p1.distance_from_point(p2))
        print (p1.travelling_distance(p2))

        p0 = Point (0,0)
        p1 = Point (1,5)
        p2 = Point (-1,5)
        p3 = Point (-1,-5)
        p4 = Point (1,-5)
    

        print (p0.bearing_from(p1))
        print (p0.bearing_from(p2))
        print (p0.bearing_from(p3))
        print (p0.bearing_from(p4))

    
    
main()

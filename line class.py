'''
    This an attempt to create a class for a Line segment.

'''

__authour__ = "Boneya Hassan<bonairhassan@gmail.com>"


from Point_class import Point

class LineSegment(object):

    ''' This class creates a line segment from two points, start point and end point.
        This point objects can be from the Point class or a tuple. '''
    
    def __init__(self, startpoint, endpoint):
        
        if startpoint != endpoint:
            self.sp = startpoint
            self.ep = endpoint
        else:
            raise ValueError ('Startpoint cannot be equal to endpoint')


    def __eq__(self,l):

        if isinstance(l,LineSegment):
            return self.sp == l.sp and self.ep == l.ep
        else:
            return NotImplemented


    def __repr__(self):
        return 'LineSegment ({},{})'.format(self.sp, self.ep )
    

    def __str__(self):
        return '({},{})'.format(self.sp, self.sp )

    @property
    def midpoint(self):
        x = ((self.sp[0] + self.ep[0])/2)
        y = ((self.sp[1] + self.ep[1])/2)
        return Point(x,y)

    @property
    def length(self):
        ''' Returns the length of a line segment '''
        
        return Point.distance_from_point(self.sp,self.ep)
    
    @property
    def direction(self):
        ''' Returns the bearing of a line wrt to north'''
        return Point.bearing_from(self.sp,self.ep)

    def distanceToPoint(self,p):
        ''' Returns the Euclidean distance between this line segment
            and the specified point.  '''
        pass

    def isPointInLine (self,p):
        ''' checks if a point (x,y) in the Point class falls within
            the bounds of the line segment.'''

        v= (self.ep -self.sp)
        w = (p -self.sp)

        cross_prod = (v.x *w.y) - (v.y * w.x)

        if cross_prod != 0: return False
        
        v = (self.ep - self.sp)
        w = (p - self.sp)
        
        dot_prod = (v.x *w.x) + (v.y *w.y)

        if dot_prod < 0: return False

        len_sq = (self.length * self.length)

        if dot_prod >= len_sq: return False

        return True
    
    def getIntersectionWithLine (self,l2):
        ''' Finds the intesection point of two line segments if they intersect. Returns a
            Point, otherwise returns False if there is no intersection. l2 is line 2'''
        
        if not self == l2:
            
            p = self.sp
            r = self.ep -self.sp

            q = l2.sp
            s = l2.ep - l2.sp

            v =(q -p)
            w = s

            # calculates   t = ...

            nom_t = (v.x * w.y) - ( v.y * w.x)

            denom_t = (r.x * s.y) - (r.y * s.x)




	    # calculates   u = (p − q) × r / (s × r)
	    
            v1 = (p -q)
            w1 = r

            nom_u = (v1.x * w1.y) - ( v1.y * w1.x)

            denom_u = (s.x * r.y) - (s.y * r.x)

            
            
            if denom_t == 0 and nom_u == 0:
                #"The two lines are collinear."
                return False

            elif denom_t == 0 and nom_u != 0:
                #"The two lines are parallel"
                return False

            else:
                t = (nom_t/denom_t)
                u = (nom_u/denom_u)

            
            
            
            if denom_t != 0 and ((t>=0 and t<= 1) and (u>=0 and u<= 1)):
                return (p + ( r * t))
            
            else:
                #"The two lines are not parallel and dont intersect."
                return False
        else:
            #"The two lines are the same."
            return False

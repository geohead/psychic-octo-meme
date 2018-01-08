'''
    Implementation of angles class.


'''

__authour__ = 'Boneya Hassan<bonairhassan@gmail.com>'


class Angle (object):
    '''
    This is a class for Angle. This class represents and
    uses Angle for computations.

    '''

    def __init__(self, dd,mm=0,ss=0):
    
        self.bearing = dd + (mm/60) + (ss/3600)
        self.dd =int(self.bearing)
        self.mm=int ((self.bearing-self.dd)*60)
        self.ss= float((((self.bearing-self.dd)*60)-self.mm)*60)


    def __str__(self):
        
        return (" {}{} {}\' {}{} ").format(self.dd,chr(176), self.mm, self.ss,chr(34))
    
    def __repr__(self):
        return '{}'.format(self.bearing)

    def __add__ (self, other):
        if not isinstance(other,Angle):
            return NotImplemented
        else:
            return Angle(self.bearing + other.bearing)

    def __radd__(self,other):
        return self.__add__(other)
    
        
    def __sub__(self,other):
        if not isinstance(other,Angle):
            return NotImplemented
        else:
            return Angle(self.bearing - other.bearing)
        
    def __rsub__(self, other):
        if not isinstance(other,Angle):
            return NotImplemented
        else:
            return self.__sub__(other)

    def __mul__(self,other):
        if not (isinstance (other,int) or isinstance (other,float)):
            return NotImplemented
        
        return self.bearing * other

    def __rmul__(self,other):
        return self.__mul__(other)
        
    
    def __truediv__ (self,other):
        if not (isinstance (other,int) or isinstance (other,float)):
            return NotImplemented
        
        return (self.bearing / other)

    def __eq__(self,other):
        
        if self.bearing == other.bearing:
            return True
        else:
            return False

        
    def __lt__(self,other):
        
        if (isinstance (other,Angle)):
            if self.bearing < other.bearing:
                return True
            else: return False
        else:
            return NotImplemented

    def __gt__ (self,other):

        if (isinstance (other,Angle)):
            if self.bearing > other.bearing:
                return True
            else: return False
        else:
            return NotImplemented

      
    def __le__(self,other):

        if (isinstance (other,Angle)):
            if self.bearing <= other.bearing:
                return True
            else: return False
        else:
            return NotImplemented
        

    def __ge__(self,other):

        if (isinstance (other,Angle)):
            if self.bearing >= other.bearing:
                return True
            else: return False
        else:
            return NotImplemented
                        
      



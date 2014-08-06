import math
import numpy as np

def angle( x, y ):
    dot = np.dot( x, y )
    x_mod = np.linalg.norm( x )
    y_mod = np.linalg.norm( y )
    cos_angle = dot / ( x_mod * y_mod )
    return np.degrees( np.arccos( cos_angle ) )

class Cell:

    def __init__( self, matrix ):
        assert type( matrix ) is np.ndarray
        assert matrix.shape == ( 3, 3 )
        self.matrix = matrix # 3 x 3 numpy Array

    def dr( self, r1, r2, cutoff = None ):
        delta_r_cartesian = ( r1 - r2 ).dot( self.matrix )
        delta_r_squared = sum( delta_r_cartesian**2 )
        if cutoff != None:
            cutoff_squared = cutoff ** 2
            if delta_r_squared > cutoff_squared:
                return None
        return( math.sqrt( delta_r_squared ) )

    def nearest_image( self, origin, point ):
        return( origin + self.minimum_image( origin, point ) )

    def minimum_image( self, r1, r2 ):
        delta_r = r2 - r1
        delta_r = np.array( [ x - math.copysign( 1.0, x) if abs(x) > 0.5 else x for x in delta_r ] )
        return( delta_r )

    def minimum_image_dr( self, r1, r2, cutoff = None ):
        delta_r_vector = self.minimum_image( r1, r2 )
        return( self.dr( np.zeros( 3 ), delta_r_vector, cutoff ) )

    def lengths( self ):
        return( np.array( [ math.sqrt( sum( row**2 ) ) for row in self.matrix ] ) )

    def angles( self ):
        ( a, b, c ) = [ row for row in self.matrix ]
        return [ angle( b, c ), angle( a, c ), angle( a, b ) ]

    def centre( self, points ):
        print( points )

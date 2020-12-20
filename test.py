from datetime import datetime, time, timedelta
from spoken_time import *
from spoken_time import _

if __name__ == '__main__': # Test code
        
    for t in ( datetime.now().time(),
        time( 11, 30), time( 12    ), time( 13, 15),
        time(  1, 20), time(  3, 45), time( 15, 50),
        time( 23, 30), time(  0    ), time(  0, 10)):
        print( t, _('It is {time}.').format( time=spoken_time( t)))
    
    print()
    today = datetime.now().date()
    for delta in range( -14, 14):
        date = today + timedelta( delta)
        print( date,
            _('Today is {date}.').format( date=absolute_spoken_date( date)),
                '/', relative_spoken_date( date))

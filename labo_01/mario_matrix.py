"""
==============================================
Sensehat - Matrix - Mario
==============================================
Mario Jumps
----------------------------------------------
Course:     Web Of Things (WOT)
Option:     New Media Development
Department: Graphic and Digital Media
College:    Artevelde University College Ghent
----------------------------------------------
Authors:
    - Philippe De Pauw - Waterschoot
    - Dieter De Weirdt
----------------------------------------------
Resources:
    - https://github.com/svvitale/nxppy
==============================================
"""

import os, sys, time
from sense_hat import SenseHat

print('Application started.')

sense = SenseHat()

Bk = (0,0,0)
Wh = (255,255,255)
Rd = (255, 0, 77)
Bl = (41, 173, 255)
Br = (187, 90, 59)
Pk = (255, 208, 174)
Yl = (250, 252, 44)


mario = [
    Bk, Bk, Bk, Rd, Rd, Rd, Wh, Bk,
    Bk, Bk, Bk, Rd, Rd, Rd, Rd, Rd,
    Bk, Bk, Br, Pk, Br, Bk, Pk, Bk,
    Bk, Bk, Br, Pk, Pk, Br, Br, Pk,
    Bk, Bk, Bk, Br, Pk, Pk, Pk, Bk,
    Bk, Rd, Rd, Yl, Bl, Bl, Yl, Bk,
    Wh, Bk, Bl, Bl, Bl, Bl, Bk, Bl,
    Bk, Bk, Br, Bk, Bk, Bk, Rd, Bk  
    
]

mario_jump = [
    Bk, Bk, Bk, Rd, Rd, Rd, Rd, Rd,
    Bk, Bk, Br, Pk, Br, Bk, Pk, Bk,
    Bk, Bk, Br, Pk, Pk, Br, Br, Pk,
    Bk, Bk, Bk, Br, Pk, Pk, Pk, Bk,
    Wh, Rd, Bl, Yl, Bl, Bl, Yl, Bl,
    Bk, Bk, Br, Bk, Bk, Bk, Rd, Bk,  
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,   
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk    
]

blank = [
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk
]

sense.set_pixels(mario)
left = False
jump = False 


while True:
    try:        
        jump = False
        for event in sense.stick.get_events(): 
            if event.direction == 'left':
                left = True
            if event.direction == 'right':
                left = False
            if event.direction == 'up':
                jump = True
                
        if jump :
            sense.set_pixels(mario_jump)
        else :
            sense.set_pixels(mario)

        if left :
            sense.flip_h()

        time.sleep(.5)
        
    except (KeyboardInterrupt, SystemExit):
        print('Application closed.')
        sense.set_pixels(blank)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
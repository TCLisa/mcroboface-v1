from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0,17)
sm = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
fr = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0.0]
while True:
    for id in range(0, len(sm)):
            if(sm[id] !=0):
                np[id] = (255,0,0)
            else:
                np[id] = (0,0,0)
    np.show()
    sleep(1000)
    for id in range(0, len(fr)):
            if(fr[id] !=0):
                np[id] = (0,0,255)
            else:
                np[id] = (0,0,0)
    np.show()
    sleep(1000)
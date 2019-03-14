#!/usr/bin/env python3
# Midi experimentation using neopixel library and mido
# Author: Alex Fisher



import time
from neopixel import *
import argparse
import mido

# LED strip configuration:
LED_COUNT      = 25      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.



def inputPixel(strip):
    pixAddr=0
    redValue=0
    greenValue=0
    blueValue=0
    
    try:
        pixAddr=int(raw_input("Input Which Pixel to Address"))
    except ValueError:
        print "Not a number"
    try:
        redValue=int(raw_input('Input R:'))
    except ValueError:
        print "Not a number"
    try:
        greenValue=int(raw_input('Input G:'))
    except ValueError:
        print "Not a number"
    try:
        blueValue=int(raw_input('Input B:'))
    except ValueError:
        print "Not a number"  
    strip.setPixelColor(pixAddr,Color(greenValue,redValue,blueValue))
    strip.show()
    time.sleep(1/4)

def clearStrip(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        time.sleep(40/1000.0) #40ms per light to clear  
   

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            inputPixel(strip)

    except KeyboardInterrupt:
        if args.clear:
            clearStrip(strip)
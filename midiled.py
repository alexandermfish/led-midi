
# Midi experimentation using neopixel library and mido
# Author: Alex Fisher
# note: install mido with sudo pip on rpi using GPIO



import time
from neopixel import *
import argparse
import mido
import random

# LED strip configuration:
LED_COUNT      = 25      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# MIDI CONTROLLER - you will need to set this up yourself
MIDI_CONTROLLER = 'Arturia MINILAB:Arturia MINILAB MIDI 1 20:0' #use mido.get_input_names() to get this (first console print)
FIRST_NOTE     = 48     #set the first note of your current midi controller in default octaves
LAST_NOTE      = 72      #set the last note of your current midi controller in default octaves (print midi msgs to get)

# standard Color() constants for ease of use. please note, these are in G,R,B format
VIOLET        = Color(0,255,60)
CYAN           = Color(255,0,255)
YELLOW         = Color(155,255,0)
GREEN         = Color(255,0,0)
RED         = Color(0,255,0)



inport = mido.open_input(MIDI_CONTROLLER)
globalx = 0
midiNotes = range(FIRST_NOTE, LAST_NOTE+1)
lifeSpans = [0]*LED_COUNT #create a list of LED_COUNT 0s to house lifeSpans of notes
life = 1700 #set the lifespan
ledColors = [[0]*3]*LED_COUNT


defaultColor = Color(20/20, 255/20, 70/20) #set this to a constant of your choice or the Color function
colorCycle = 1
darkness=20
r = 0
b = 0
g = 0
mode = "simple"

# Define functions which animate LEDs in various ways.




def fadeOut(r,g,b):

    #for loop is used to keep track of the remaining life of a LED after a keypress
    for i in range(len(lifeSpans)):
        red = r
        green = g
        blue= b
        
        if lifeSpans[i]>0:
           
            lifeSpans[i] = lifeSpans[i] - 1
            
            if lifeSpans[i] ==0:
                strip.setPixelColor(i, defaultColor)
                strip.show()
            
            elif lifeSpans[i] == ((life/20)*19):
                
                intR = int(float(red)*0.95)
                intG = int(float(green)*0.95)
                intB = int(float(blue)*0.95)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*18):
                
                intR = int(float(red)*0.90)
                intG = int(float(green)*0.90)
                intB = int(float(blue)*0.90)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*17):
                
                intR = int(float(red)*0.85)
                intG = int(float(green)*0.85)
                intB = int(float(blue)*0.85)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
                
            elif lifeSpans[i] == ((life/20)*16):
                
                intR = int(float(red)*0.80)
                intG = int(float(green)*0.80)
                intB = int(float(blue)*0.80)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
                
            elif lifeSpans[i] == ((life/20)*15):
                
                intR = int(float(red)*0.75)
                intG = int(float(green)*0.75)
                intB = int(float(blue)*0.75)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*14):
                
                intR = int(float(red)*0.70)
                intG = int(float(green)*0.70)
                intB = int(float(blue)*0.70)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*13):
                
                intR = int(float(red)*0.65)
                intG = int(float(green)*0.65)
                intB = int(float(blue)*0.65)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*12):
                
                intR = int(float(red)*0.60)
                intG = int(float(green)*0.60)
                intB = int(float(blue)*0.60)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*11):
                
                intR = int(float(red)*0.55)
                intG = int(float(green)*0.55)
                intB = int(float(blue)*0.55)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*10):
                
                intR = int(float(red)*0.50)
                intG = int(float(green)*0.50)
                intB = int(float(blue)*0.50)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*9):
                
                intR = int(float(red)*0.45)
                intG = int(float(green)*0.45)
                intB = int(float(blue)*0.45)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*8):
                
                intR = int(float(red)*0.40)
                intG = int(float(green)*0.40)
                intB = int(float(blue)*0.40)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*7):
                
                intR = int(float(red)*0.35)
                intG = int(float(green)*0.35)
                intB = int(float(blue)*0.35)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*6):
                
                intR = int(float(red)*0.30)
                intG = int(float(green)*0.30)
                intB = int(float(blue)*0.30)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*5):
                
                intR = int(float(red)*0.25)
                intG = int(float(green)*0.25)
                intB = int(float(blue)*0.25)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*4):
                
                intR = int(float(red)*0.2)
                intG = int(float(green)*0.2)
                intB = int(float(blue)*0.2)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*3):
                
                intR = int(float(red)*0.15)
                intG = int(float(green)*0.15)
                intB = int(float(blue)*0.15)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*2):
                
                intR = int(float(red)*0.1)
                intG = int(float(green)*0.1)
                intB = int(float(blue)*0.1)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
            elif lifeSpans[i] == ((life/20)*1):
                
                intR = int(float(red)*0.05)
                intG = int(float(green)*0.05)
                intB = int(float(blue)*0.05)

                strip.setPixelColor(i, Color(intG,intR,intB))
                strip.show()
                
                   





def midiPolling():
    midi = inport.poll() #constantlly check if there is a midi message being recieved
    return midi

def checkChangeMode(midiSignal):
    global mode
    global defaultColor
    global life
    global colorCycle
    global darkness
    global midiNotes
    
    if midiSignal != None:
        if midiSignal.type == 'note_on':
            red = Color(0,255/darkness,0)
            green = Color(255/darkness,0,0)
            blue = Color(0,0,255/darkness)
            yellow = Color(190/darkness,255/darkness,0)
            cyan = Color(255/darkness,0,255/darkness)
            purple = Color(0,255/darkness,155/darkness)

            
            if MIDI_CONTROLLER == 'Arturia MINILAB:Arturia MINILAB MIDI 1 20:0':

                    
                if midiSignal.note == 36:
                    print("Mode: Simple")
                    mode = "simple"
                elif midiSignal.note == 37:
                    print("Mode: Random")
                    #mode = "random"
                elif midiSignal.note == 38:
                    print("Control: Lengthen Fade")
                    life = life + 500

                elif midiSignal.note == 39:
                    print("Control: Shorten Fade")
                    if life>500:
                        life = life - 500

                elif midiSignal.note == 40:
                    print("Control: Change Color")
                    colorCycle +=1
                    if colorCycle == 1:
                        defaultColor = red
                        print("Red")
                    elif colorCycle == 2:
                        defaultColor = green
                        print("Green")
                    elif colorCycle == 3:
                        defaultColor = blue
                        print("Blue")
                    elif colorCycle == 4:
                        defaultColor = yellow
                        print("Orange/Yellow")
                    elif colorCycle == 5:
                        defaultColor = cyan
                        print("Cyan")
                    elif colorCycle == 6:
                        defaultColor = purple
                        print("Purple")
                    elif colorCycle ==7:
                        colorCycle = 0
                        
                    for note in midiNotes:
                        strip.setPixelColor(midiNotes.index(note), defaultColor) #map the pixel address to the note
                        strip.show()
                        
                        
                elif midiSignal.note == 42:
                    print("Control: Brighten BG")
                    if darkness>3:
                        darkness = darkness-3
                    else:
                        print("Max brightness")
                    
                    for note in midiNotes:
                        strip.setPixelColor(midiNotes.index(note), defaultColor) #map the pixel address to the note
                        strip.show()

                elif midiSignal.note == 41:
                    print("Control: Dim BG")
                    darkness = darkness+3
                    for note in midiNotes:
                        strip.setPixelColor(midiNotes.index(note), defaultColor) #map the pixel address to the note
                        strip.show()

                elif midiSignal.note == 43:
                    pass
        

def midoLed(midiSignal):
    global midiNotes
    global lifeSpans
    global life
    global r
    global g
    global b
    global mode

    

    
    # will constantly return None when no signal, so we need to avoid dealing in that realm with the following
    if midiSignal != None: 


        
        if mode == "simple":
            if midiSignal.type == 'note_on':

                print("note on: " + str(midiSignal.note)) #diagnostics
                for note in midiNotes:
      
                    if midiSignal.note == note: #check if any note being played exists in the array
                        r = 255
                        g = 200
                        b = 0

                        strip.setPixelColor(midiNotes.index(note), Color(g,r,b )) #map the pixel address to the note
                        strip.show()
                        
                        
            if midiSignal.type == 'note_off':
                print("note off: " + str(midiSignal.note)) #diagnostics
                for note in midiNotes:
                    currentIndex = midiNotes.index(note)
                    
                    if midiSignal.note == note:
                        lifeSpans[currentIndex] = life
                        print("LED/currentIndex:" + str(currentIndex))


#for coloring the whole strip on initialization
def colorStrip(strip): 
    global defaultColor
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, defaultColor) #GRB ordering for some reason (could be my wiring mistake?)
        strip.show()
        time.sleep(20/1000.0) #20ms per light to color for the neat effect, no other reason    

def clearStrip(strip):
    for i in reversed(range(strip.numPixels())):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        time.sleep(20/1000.0) #20ms per light to clear  for the neat effect, no other reason
   

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
    print(mido.get_input_names())
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        print(ledColors)
        colorStrip(strip)
        while True:
            #inputPixel(strip)
            midiInput=midiPolling()
            midoLed(midiInput)
            checkChangeMode(midiInput)
            
            fadeOut(r,g,b)

    except KeyboardInterrupt:
        if args.clear:
            clearStrip(strip)
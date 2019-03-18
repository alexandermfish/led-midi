
# Midi experimentation using neopixel library and mido
# Author: Alex Fisher
# note: install mido with sudo pip on rpi using GPIO



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
#MIDI CONTROLLER
MIDI_CONTROLLER = 'Arturia MINILAB:Arturia MINILAB MIDI 1 20:0' #use mido.get_input_names() to get this
FIRST_NOTE = 48     #set the first note of your current midi controller in default octaves
LAST_NOTE = 72      #set the last note of your current midi controller in default octaves (print midi msgs to get)

inport = mido.open_input(MIDI_CONTROLLER)
globalx = 0
midiNotes = range(FIRST_NOTE, LAST_NOTE+1)
lifeSpans = [0]*LED_COUNT #create a list of zeros to house lifespans of notes
life = 5000 #set the lifespan



# Define functions which animate LEDs in various ways.

def midoLed():
    global midiNotes
    global lifeSpans
    global life
    
    midiSignal = inport.poll() #constantlly check if there is a midi message being recieved
    # will constantly return None when no signal, so we need to avoid dealing in that realm with the following
 
    #for loop is used to keep track of the remaining life of a LED after a keypress
    for i in range(len(lifeSpans)):
        if lifeSpans[i]>0:
            lifeSpans[i] = lifeSpans[i] - 1
            if lifeSpans[i] ==0:
                strip.setPixelColor(i, Color(0,10,0))
                strip.show()
            if lifeSpans[i] ==4000:
                strip.setPixelColor(i, Color(10,55,255))
                strip.show()
            if lifeSpans[i] ==3000:
                strip.setPixelColor(i, Color(10,55,150))
                strip.show()    
            if lifeSpans[i] ==2000:
                strip.setPixelColor(i, Color(10,55,100))
                strip.show()    
            if lifeSpans[i] ==1000:
                strip.setPixelColor(i, Color(10,55,20))
                strip.show()  
            if lifeSpans[i] ==3500:
                strip.setPixelColor(i, Color(30,55,170))
                strip.show()
            if lifeSpans[i] ==2500:
                strip.setPixelColor(i, Color(20,55,120))
                strip.show()    
            if lifeSpans[i] ==1500:
                strip.setPixelColor(i, Color(22,55,50))
                strip.show()    
            if lifeSpans[i] ==500:
                strip.setPixelColor(i, Color(15,50,15))
                strip.show() 

       
        
    
    if midiSignal != None: 
        
        
        if midiSignal.type == 'note_on':
            print("note:" + str(midiSignal.note)) #diagnostics
            for note in midiNotes:
                if midiSignal.note == note: #check if any note being played exists in the array
                    strip.setPixelColor(midiNotes.index(note), Color(255,255,255)) #map the pixel address to the note
                    strip.show()
                    

        if midiSignal.type == 'note_off': 
            print("note off:" + str(midiSignal.note)) #diagnostics
            for note in midiNotes:
                
                currentIndex = midiNotes.index(note)
                
                if midiSignal.note == note:
                    lifeSpans[currentIndex] = life
                    print("LED/currentIndex:" + str(currentIndex))
    
    
            
    #time.sleep(2)
    
    
    
#testing code, unused in final
def inputPixel(strip):
    pixAddr=0
    redValue=0
    greenValue=0
    blueValue=0
    
    try:
        pixAddr=int(raw_input("Input Which Pixel to Address"))
    except ValueError:
        print("Not a number")
    try:
        redValue=int(raw_input('Input R:'))
    except ValueError:
        print("Not a number")
    try:
        greenValue=int(raw_input('Input G:'))
    except ValueError:
        print("Not a number")
    try:
        blueValue=int(raw_input('Input B:'))
    except ValueError:
        print("Not a number")  
    strip.setPixelColor(pixAddr,Color(greenValue,redValue,blueValue))
    strip.show()
    time.sleep(1/4)

def clearStrip(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        time.sleep(40/1000.0) #40ms per light to clear  for the neat effect, no other reason
   

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
            #inputPixel(strip)
            midoLed()

    except KeyboardInterrupt:
        if args.clear:
            clearStrip(strip)
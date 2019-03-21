# led-midi
Using python with midi libraries and a raspberry pi to create a makeshift midi based lighting controller


## Usage:
ENSURE all pip dependency installs are done using sudo. This is because using the RGB 281x lib requires python to run in sudo. This is frowned upon, but annoyingly necessary.

**Requires a 281x RGB strip, a raspberry pi and a midi controller**

- set the constants to your midi controller/led requirements
- navigate to the directory in terminal and run `sudo python midiled.py -c`

### To do:

- additionally send the midi to a DAW to generate sounds (external computer)


## Demo
![](demo.gif)

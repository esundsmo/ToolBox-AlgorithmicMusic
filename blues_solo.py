""" Synthesizes a blues solo algorithmically.

    For the Olin College Software Design class. 
    Script skeleton and instruction provided.
    https://sites.google.com/site/sd16spring/home/project-toolbox/algorithmic-music-composition

    @Author Elizabeth Sundsmo 3/13/2016
"""

from Nsound import *
import numpy as np
from random import choice

def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

        out: the stream to add the note to
        instr: the instrument that should play the note
        key_num: the piano key number (A 440Hzz is 49)
        duration: the duration of the note in beats
        bpm: the tempo of the music
        volume: the volume of the note
    """
    freq = (2.0**(1/12.0))**(key_num-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream

# this controls the sample rate for the sound file you will generate
sampling_rate = 44100.0
Wavefile.setDefaults(sampling_rate, 16)

# allows for easier selection of instrument
bass = GuitarBass(sampling_rate)    # use a guitar bass as the instrument
clarinet = Clarinet(sampling_rate)    # use a guitar bass as the instrument
# drum_bass = DrumKickBass(sampling_rate, high_frequency, low_frequency)    # use a guitar bass as the instrument
drum_bd01 = DrumBD01(sampling_rate)    # use a guitar bass as the instrument
hat = Hat(sampling_rate)    # use a guitar bass as the instrument
organ = OrganPipe(sampling_rate)    # use a guitar bass as the instrument
flute = FluteSlide(sampling_rate)    # use a slide flute as the instrument

solo = AudioStream(sampling_rate, 1)

""" these are the piano key numbers for a 3 octave blues scale in A
    See: http://en.wikipedia.org/wiki/Blues_scale """
blues_scale = [25, 28, 30, 31, 32, 35, 37, 40, 42, 43, 44, 47, 49, 52, 54, 55, 56, 59, 61]
beats_per_minute = 45               # Let's make a slow blues solo

# add_note(solo, bass, blues_scale[0], 1.0, beats_per_minute, 1.0)

instrument = bass
curr_note = 0
add_note(solo, instrument, blues_scale[curr_note], 1.0, beats_per_minute, 1.0)

# possible sound paths, randomly strung together by computer. [change from current note, duration]
licks = [ [[-1,2]],
          [[1,2]],
          [[ 1,0.5*1.1],  [ 1,0.5*0.9],  [ 1,1]],
          [[-1,0.5*1.1],  [-1,0.5*0.9],  [-1,1]],
          [[-2,0.5*1.1],  [ 1,0.5*0.9],  [ 1,1]],
          [[ 4,1*1.1],    [-3, 1*0.9]],
          [[-4, 1*1.1],   [ 3, 1*0.9]],
          [[-3, 1],       [ 1,0.5*1.1],  [ 1, 0.5*0.9]],
          [[ 3, 1],       [-1,0.5*1.1],  [-1, 0.5*0.9]] ]

"""The range is how many licks will be strung together in the solo. 
   a measure is two licks (a measure has 4 beats and a lick has 2)"""
for i in range(32):
    # randomly choose which lick to play next. Format: choice(licks) or choice(range(start, stop, step))
    lick = choice(licks)
    print lick
    for note in lick:
        #start from previous note
        curr_note += note[0]
        #start from a root note
        # curr_note = choice(range(0,18,6))

        #push current note up or down if it is about to go to low or high (respectively)
        if curr_note==0 or curr_note==len(blues_scale)-1:
            #random jump:
            # curr_note = choice(range(0, len(blues_scale)-1, 1))
            #reverse jump:
            curr_note -= 2*note[0]
            
        add_note(solo, instrument, blues_scale[curr_note], note[1], beats_per_minute, 1.0)

#play just the solo:
# solo >> "blues_solo.wav"

#play the solo with background music:
backing_track = AudioStream(sampling_rate, 1)
Wavefile.read('backing.wav', backing_track)

m = Mixer()

solo *= 0.4             # adjust relative volumes to taste
backing_track *= 2.0

m.add(2.25, 0, solo)    # delay the solo to match up with backing track   
m.add(0, 0, backing_track)

m.getStream(500.0) >> "slow_blues.wav"
# ToolBox-AlgorithmicMusic
Algorithmic Music Composition Project Toolbox

The Basics:

Plays algorithmically generated blues solo over a background track.


To Run Code:

Install Nsound and  matplotlib.pylab:
			        (see Full Instructions, end of README)
			        sudo apt-get install python-matplotlib 

In the terminal run 		python blues_solo.py
and then either                 cvlc slow_blues.wav
OR                              cvlc blues_solo.wav
to play the solo over the background track or just the solo (respectively). Press Ctrl+c to quit cvlc.


To Understand/Change Code:

Uses Nsound, numpy, and random libraries to algorithmically generate music. Random is used to choose a lick from a list of user created licks (pattern of notes and lengths) and put them into a sequence. This sequence is played on a 3 octave blues scale in A with a user designated instrument (currently bass guitar).

To modify the sound try changing the instrument (line 50, instrument types lines 33-39) or adding some new licks (line 55). Changing the scale or bpm is not advised unless another background track is chosen. 

To play just your solo uncomment line 87 and comment lines 90-101.

Full instructions at https://sites.google.com/site/sd16spring/home/project-toolbox/algorithmic-music-composition

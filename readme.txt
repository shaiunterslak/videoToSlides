Takes in an mp4 file (such as a screen recording of a slide show presentation) and saves all unique frames to a new directory. 

To run from command line where video name is "example.mp4" :

python vidToSlides.py example.mp4

Will create a directory with the video name which is where all of the slides will be saved. 
Will output every time a unique slide is found with how far into the video it was found in minutes.


Finally outputs the total number of unique slides found


Note: Only checks every 500 frames for efficiency. Every slide that is up for less than 500 frames will be ignored.


# LeapMotion_python_app
Leap Motion App using Python 3.x

- LeapMotionApp.py : This class is just a template with basic functions defined.
- LeapMotionApp1.py: Shows Frames movement with relevant data on your console.
- LeapMotionApp2.py : Extension of LeapMotionApp1.py,shows how to get the controls values and positions.


## How to run 
 - You should have a leap motion device to test it out.
 - This example is compatible with windows OS preferrably Windows 10 OS.
 - Clone this project
 - Install Python 3.x
 - python LeapMotionApp.py OR python LeapMotionApp1.py OR python LeapMotionApp2.py
 
 
### If you are getting Error like 

####Error

 - ImportError: DLL load failed: %1 is not a valid Win32 application.

####Solution

- Suspect Number 1

Looks like you are on windows 64 bit but have installed python of windows 32 bit or vice versa.


- Suspect Number 2

Looks like you are on Windiws 64 bit and accessing APIs which are meant for windows 32 bit

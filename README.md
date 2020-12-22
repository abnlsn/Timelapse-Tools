# Timelapse Tools
 A simple tool for creating timelapses in Blender. Currently, it is pretty basic, but I am planning to add more functionality.
 **Current Functions:**
 - Turntable (demo [here](https://bit.ly/ab3dchannel).) More info below.
 
## Installation
Download the code from GitHub by clicking `Code` and then `download as .zip`. Don't unzip the download. In blender, open up your preferences by going to `Edit > Preferences`. Choose the addon tab and click `Install Add-On`. Locate the zip file on your computer and import it. The addon should show up in a box, and then just check the checkbox to activate it.
## Usage
Now you are ready to use it. Currently Timelapse Tools only has a Turntable function. Here is the basics of what it does. The turntable is designed to be used in a seperate window from the one where you actually do the work.
### Using Turntable
Timelapse Tools can be found under the sidebar (press `N` to see it) in the `Tool` tab. You should see a header called `Timelapse Tools` and open it if it isn't already. You should see some different options:
- Degrees of Rotation  - How many degrees the turntable rotates around the z axis every interval.
- Wait Seconds - How many seconds per interval (How often the turntable moves)
- New Window - Opens a new window with only a View3D
- Start Turntable - Starts the turntable in the current window
- Cancel Turntable - Cancels all turntables
### Recording
I use [OBS](https://obsproject.com) for recording my timelapses. I just turn down the FPS so I don't have to record unnecessary frames (because I am going to speed it up anyways). I use a window capture source to record only the turntable window.

## Issues
This is mostly just a personal project, and I haven't tested it thoroughly at all. But if you find it helpful and have a bug to report or a feature request, feel free to open up an issue! Thanks!

from CoreLib.Windows.windowClass import * # Import the library like this

global SetThemeColors
from CoreLib.setcolor import SetThemeColors

#	Import other libraries like this:

global datetime
import datetime

global re
import re

from pathlib import Path
global Path

global msg
msg = "Changed Config"

global theme_buttons
global color_buttons
global taskbarColor_buttons

color_buttons = [
"blue_button",
"black_button",
"cyan_button",
"green_button",
"magenta_button",
"red_button",
"white_button",
"yellow_button"
]

theme_buttons = [
"light_button",
"dark_button"
]

taskbarColor_buttons = [
"blue_button2",
"black_button2",
"cyan_button2",
"green_button2",
"magenta_button2",
"red_button2",
"white_button2",
"yellow_button2"
]
#	The main function
def mainWinFunction(window, key, clickedButton):
    SetThemeColors()
    global color
    global lines
    global theme
    global change
    f3 = open("config.cfg", "r")
    config = f3.readlines()
    color = config[1]
    theme = config[2]
    taskbar = config[3]
    if clickedButton != 0: # If you have clicked a button
#	If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow() # Close the window
        else: #If we aren't closing the window

#	Set Background Colors
            if clickedButton["widgetID"] in color_buttons:
                color = "COLOR:"+ (clickedButton["widgetID"].split("_"))[0]
                change = "colors"

#	Set Window Themes
            elif clickedButton["widgetID"] in theme_buttons:
                theme = "THEME:"+(clickedButton["widgetID"].split("_"))[0]
                change = "theme"
                
            elif clickedButton["widgetID"] in taskbarColor_buttons:
                taskbar = "TSKBRCLR:"+(clickedButton["widgetID"].split("_"))[0]
                change = "taskbar"

#	Write to file
            with open("config.cfg", "r") as f:
                lines = f.readlines()

#	Test if we are changing the background on the desktop
            if change == "colors\n":
                lines[1] = f"{color}"

#	Test if we are changing the window theme
            elif change == "theme":
                lines[2] = f"{theme}\n"

#	Test if we are changing the taskbar colors
            elif change == "taskbar":
                lines[3] = f"{taskbar}"

#	Run something if it is nothing, it'll probably crash, but this code shouldn't ever even be called
            else:
                lines[1] = f"{color}\n"

#	Add a message at the top of the config file
            lines[0] = "This File Is Automatically Generated By TWS-Settings, Do Not Edit This File!\n"

#	Write the changes to the file (only what is different)
            with open("config.cfg", "w") as f:
                f.writelines(lines)   
                f.close()

#	Display the conformation message that we in fact did change the configuration
            window.getWidgetByID("Config_Update")["text"] = msg

'''
Ran on initilization to set up the widgets
'''           
Widgy = 2

mainWin = Window("TWS-Settings", mainWinFunction) # Create a window

try:
    mainWin.width = int(curses.COLS/1.3)
    mainWin.height = int(curses.LINES/1.2)-10
    mainWin.x = curses.COLS//9
    mainWin.y = curses.LINES//9
except:
    pass

mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
mainWin.addLabel("", 1, Widgy, "╔══════════════════════╗") # Add a title with an id of "Config_Update"
mainWin.addLabel("", 2, Widgy, "║Change System Settings║") # Add a title with an id of "Config_Update"
mainWin.addLabel("", 3, Widgy, "╚══════════════════════╝") # Add a title with an id of "Config_Update"
mainWin.addLabel("Config_Update", 4, Widgy, "") # Add a label with an id of "Config_Update"

#	Color Labels
mainWin.addTitle("Colors_Header", 5, Widgy, "*Colors*") # Add a label with an id of "Colors_Header"
mainWin.addButton("blue_button", 6, Widgy, "Blue") # Add a button with an id of "blue_button"
mainWin.addButton("black_button", 7, Widgy, "Black") # Add a button with an id of "black_button"
mainWin.addButton("cyan_button", 8, Widgy, "Cyan") # Add a button with an id of "cyan_button"
mainWin.addButton("green_button", 9, Widgy, "Green") # Add a button with an id of "green_button"
mainWin.addButton("magenta_button", 10, Widgy, "Magenta") # Add a button with an id of "magenta_button"
mainWin.addButton("red_button", 11, Widgy, "Red") # Add a button with an id of "red_button"
mainWin.addButton("white_button", 12, 2, "White") # Add a button with an id of "white_button"
mainWin.addButton("yellow_button", 13, Widgy, "Yellow") # Add a button with an id of "yellow_button"

#	Theme Labels
mainWin.addTitle("Themes_Header", 15, Widgy, "*Themes*") # Add a label with an id of "Themes_Header"
mainWin.addButton("light_button", 16, Widgy, "Light") # Add a button with an id of "light_button"
mainWin.addButton("dark_button", 17, Widgy, "Dark") # Add a button with an id of "dark_button"

mainWin.addTitle("TaskBar_Colors_Header", 19, Widgy, "*Taskbar and Window Border Colors*") # Add a label with an id of "Colors_Header"
mainWin.addButton("blue_button2", 20, Widgy, "Blue") # Add a button with an id of "blue_button"
mainWin.addButton("black_button2", 21, Widgy, "Black") # Add a button with an id of "black_button"
mainWin.addButton("cyan_button2", 22, Widgy, "Cyan") # Add a button with an id of "cyan_button"
mainWin.addButton("green_button2", 23, Widgy, "Green") # Add a button with an id of "green_button"
mainWin.addButton("magenta_button2", 24, Widgy, "Magenta") # Add a button with an id of "magenta_button"
mainWin.addButton("red_button2", 25, Widgy, "Red") # Add a button with an id of "red_button"
mainWin.addButton("white_button2", 26, Widgy, "White") # Add a button with an id of "white_button"
mainWin.addButton("yellow_button2", 27, Widgy, "Yellow") # Add a button with an id of "yellow_button"

#	The Totally Secret Credits
mainWin.addLabel("credits_01", 100, Widgy, "Why did you scroll this far.") # Add a label with an id of "credits_01"
mainWin.addLabel("credits_02", 105, Widgy, "CREDITS:") # Add a label with an id of "credits_02"
mainWin.addLabel("credits_03", 107, Widgy, "Nathan Macleod: Writing most of the entire windowing system, and most of the apps") # Add a label with an id of "credits_03"
mainWin.addLabel("credits_04", 109, Widgy, "RobiTheGit: Writing this app, a file manager, fixing some bugs, and some other things") # Add a label with an id of "credits_04"
mainWin.addLabel("credits_05", 111, Widgy, "Jacob Macleod: Doing something?") # Add a label with an id of "credits_05"

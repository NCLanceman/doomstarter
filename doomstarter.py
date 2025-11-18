import os
import subprocess

path = os.getcwd()

gameplaySettings = []
mapsSettings = []
miscSettings = []
sourceSettings = []
previousSettings = []


def menuPrinter(list):
    for i in range(len(list)):
        print(str(i) + ": " + list[i])


# Dynamic Introduction!
print("So it looks like you wanna play some fuckin\' DOOM!")

print("Checking current directories...")
# On Start: Check if necessary folders are there
# ./gameplay/, ./maps/, ./misc/
if (os.path.isdir('gameplay') == False):
    print("Making Gameplay folder...")
    os.mkdir('gameplay')
if (os.path.isdir('maps') == False):
    print("Making Maps folder...")
    os.mkdir('maps')
if (os.path.isdir('misc') == False):
    print("Making Misc Folder...")
    os.mkdir('misc')

# Load Config File
settings = ((open("Settings.txt")).read()).splitlines()

currentSetting = ""

for i in settings:
    print("Examining " + i)
    print("Current Setting is: " + currentSetting)

    if (i == "[Source Ports]"):
        currentSetting = "Source Ports"
    elif (i == "[Maps]"):
        currentSetting = "Maps"
    elif (i == "[Gameplay]"):
        currentSetting = "Gameplay"
    elif (i == "[Misc]"):
        currentSetting = "Misc"
    elif (i == "[Last Used]"):
        currentSetting = "Previous"
    if i:
        if (currentSetting == "Source Ports" and i[0] != '['):
            sourceSettings.append(i)
            print("Adding " + i + " to Source Ports")
        elif (currentSetting == "Maps" and i[0] != '['):
            mapsSettings.append(i)
            print("Adding " + i + " to Maps")
        elif (currentSetting == "Gameplay" and i[0] != '['):
            gameplaySettings.append(i)
            print("Adding " + i + " to Gameplay")
        elif (currentSetting == "Misc" and i[0] != '['):
            miscSettings.append(i)
            print("Adding " + i + " to Misc")
        elif (currentSetting == "Previous" and i[0] != '['):
            previousSettings.append(i)
            print("Adding " + i + " to Previous Settings")

print("Printing Source Settings...")
print(sourceSettings)
print("Printing Maps...")
print(mapsSettings)
print("Printing Gameplay WADs...")
print(gameplaySettings)
print("Printing Misc WADs...")
print(miscSettings)
print("Printing Previous Settings...")
print(previousSettings)
# TODO: Throw everything into a dictionary and utilize at runtime


# Detect SourcePorts
# Source Port list: GZDoom, UZDoom, ChocolateDoom, DSDA-Doom, Woof!
settingsDict = {
    "sourcePorts": {},
    "maps": {},
    "gameplay": {},
    "misc": {},
    "previous": {}
}

# print("Running UZDoom with no arguements...")
# subprocess.run(sourceport_dict["UZDoom"]["runcommand"]
# + " ./gameplay/PVT_STONE_V12_5.wad", shell = True)
# subprocess.run(sourceport_dict["Woof"]["runcommand"], shell=True)

# List all that stuff in a file
print("Listing everything in Maps...")
print(os.listdir("./maps/"))

print("Adding maps to the main dict...")
mapName = ""
tempDict = {}
for i in range(len(mapsSettings)):
    tempName = "map" + str(i)
    print("Examining " + mapsSettings[i])

    if (mapsSettings[i][:2] != "--"):
        if len(tempDict) != 0:
            settingsDict["maps"].update({tempName: tempDict})
        tempDict["filename"] = mapsSettings[i]
    else:
        temp = mapsSettings[i][2:].split("=")
        tempDict.update({temp[0]: temp[1]})
if len(tempDict) != 0:
    settingsDict["maps"].update({tempName: tempDict})

print("Listing everything in Gameplay...")
print(os.listdir("./gameplay/"))

print("Listing everything in Misc...")
print(os.listdir("./misc/"))

print(settingsDict)

# print("Sample Maps listing: ")
# menuPrinter(os.listdir("./maps/"))

# Store last configs for later use

# Configure SourcePort

# Add Gameplay WAD (optional)

# Select Map WADs

print("END OF PROGRAM")

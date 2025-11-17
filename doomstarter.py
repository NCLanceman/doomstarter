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

for i in range(len(settings)):
    currentSettingGroup = []

    if (i == "[Source Ports]"):
        currentSettingGroup = sourceSettings
    elif (i == "[Maps]"):
        sourceSettings = currentSettingGroup
        currentSettingGroup = mapsSettings
    elif (i == "[Gameplay]"):
        mapsSettings = currentSettingGroup
        currentSettingGroup = gameplaySettings
    elif (i == "[Misc]"):
        gameplaySettings = currentSettingGroup
        currentSettingGroup = miscSettings
    elif (i == "[Last Used]"):
        miscSettings = currentSettingGroup
        currentSettingGroup = previousSettings
    else:
        currentSettingGroup.append(i)

previousSettings = currentSettingGroup

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
sourceport_dict = {
    "UZDoom": {
        "runcommand": "uzdoom-alpha"
    },
    "Woof": {
        "runcommand": "~/Games/Woof/woof/build/src/woof"
    }
}

print("The command for running UZDoom is: " +
      sourceport_dict["UZDoom"]["runcommand"])
# print("Running UZDoom with no arguements...")
# subprocess.run(sourceport_dict["UZDoom"]["runcommand"]
# + " ./gameplay/PVT_STONE_V12_5.wad", shell = True)
# subprocess.run(sourceport_dict["Woof"]["runcommand"], shell=True)

# List all that stuff in a file
print("Listing everything in Maps...")
print(os.listdir("./maps/"))

print("Listing everything in Gameplay...")
print(os.listdir("./gameplay/"))

print("Listing everything in Misc...")
print(os.listdir("./misc/"))


print("Sample Maps listing: ")
menuPrinter(os.listdir("./maps/"))

# Store last configs for later use

# Configure SourcePort

# Add Gameplay WAD (optional)

# Select Map WADs

print("END OF PROGRAM")

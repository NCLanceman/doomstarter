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


def mapSettingsRead(mainDict):
    tempDict = {}
    counter = 0
    for i in range(len(mapsSettings)):
        tempName = "map" + str(counter).zfill(2)
        print("Examining " + mapsSettings[i])

        if (mapsSettings[i][:2] != "--"):
            if len(tempDict) != 0:
                settingsDict["maps"].update({tempName: tempDict})
                tempDict = {}
                counter = counter + 1
            tempDict["filename"] = mapsSettings[i]
        else:
            temp = mapsSettings[i][2:].split("=")
            tempDict.update({temp[0]: temp[1]})

    if len(tempDict) != 0:
        mainDict["maps"].update({tempName: tempDict})

    return mainDict


# Dynamic Introduction!
print("So it looks like you wanna play some fuckin\' DOOM!")
print("Checking current directories...")
# On Start: Check if necessary folders are there
# ./gameplay/, ./maps/, ./misc/
# If not, end the program to allow user to add WAD files.
if not (os.path.isdir('gameplay') and os.path.isdir('maps') and os.path.isdir('misc')):
    print("Making Gameplay folder...")
    os.mkdir('gameplay')
    print("Making Maps folder...")
    os.mkdir('maps')
    print("Making Misc Folder...")
    os.mkdir('misc')

    print("Folders Created! Now go forth and fill them! Return when you are ready to DOOM!")
else:
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
    # TODO: Add maps to main dict

    # Read information from the settings file
    print("Adding maps to the main dict...")
    settingsDict = mapSettingsRead(settingsDict)

    print("Listing everything in Gameplay...")
    print(os.listdir("./gameplay/"))
    # TODO: Add gameplay WADS to main dict

    print("Listing everything in Misc...")
    print(os.listdir("./misc/"))
    # TODO: Add misc wads to the main dict

    print(settingsDict)

    # print("Sample Maps listing: ")
    # menuPrinter(os.listdir("./maps/"))

    # Store last configs for later use

    # Configure SourcePort

    # Add Gameplay WAD (optional)

    # Select Map WADs

print("END OF PROGRAM")

import os
import subprocess

path = os.getcwd()

# FIX: is this actually necessary?


def menuPrinter(list):
    for i in range(len(list)):
        print(str(i) + ": " + list[i])


def settingsReader(mainDict, file):
    tempDict = {}
    currentSetting = ""
    counter = 0
    counterName = str(counter).zfill(2)
    settings = ((open(file)).read()).splitlines()

    for i in settings:
        print("Examining " + i)
        print("Current Setting is: " + currentSetting)
        counterName = str(counter).zfill(2)

        if (i == "[Source Ports]"):
            currentSetting = "Source Ports"
            print("Addings Source Ports from Settings file...")
        elif (i == "[Maps]"):
            currentSetting = "Maps"
            counter = 0
            print("Adding maps to the main dict...")
        elif (i == "[Gameplay]"):
            currentSetting = "Gameplay"
            counter = 0
        elif (i == "[Misc]"):
            currentSetting = "Misc"
            counter = 0
        elif (i == "[Last Used]"):
            currentSetting = "Previous"
            counter = 0
        # TODO: Compress/cut down this whole block
        if i:
            if (currentSetting == "Source Ports" and i[0] != '['):
                # sourcePortSettingsRead
                if (i[:2] != "--"):
                    tempDict = {}
                    tempDict["title"] = i
                    counter = counter + 1
                    counterName = str(counter).zfill(2)
                else:
                    temp = i[2:].split("=")
                    tempDict.update({temp[0]: temp[1]})

                mainDict["sourcePorts"].update({counterName: tempDict})
            elif (currentSetting == "Maps" and i[0] != '['):
                # mapSettingsRead
                if (i[:2] != "--"):
                    tempDict = {}
                    tempDict["filename"] = "./maps/" + i
                    counter = counter + 1
                    counterName = str(counter).zfill(2)
                else:
                    temp = i[2:].split("=")
                    tempDict.update({temp[0]: temp[1]})

                mainDict["maps"].update({counterName: tempDict})
            elif (currentSetting == "Gameplay" and i[0] != '['):
                # gameplaySettingsRead
                if (i[:2] != "--"):
                    tempDict = {}
                    tempDict["filename"] = "./gameplay/" + i
                    counter = counter + 1
                    counterName = str(counter).zfill(2)
                else:
                    temp = i[2:].split("=")
                    tempDict.update({temp[0]: temp[1]})

                mainDict["gameplay"].update({counterName: tempDict})
            elif (currentSetting == "Misc" and i[0] != '['):
                # miscSettingsRead
                if (i[:2] != "--"):
                    tempDict = {}
                    tempDict["filename"] = "./misc/" + i
                    counter = counter + 1
                    counterName = str(counter).zfill(2)
                else:
                    temp = i[2:].split("=")
                    tempDict.update({temp[0]: temp[1]})

                mainDict["misc"].update({counterName: tempDict})
            elif (currentSetting == "Previous" and i[0] != '['):
                # previousSettingsRead
                if (i[:2] != "--"):
                    tempDict = {}
                    tempDict["command"] = i
                    counter = counter + 1
                    counterName = str(counter).zfill(2)
                else:
                    temp = i[2:].split("=")
                    tempDict.update({temp[0]: temp[1]})

                mainDict["previous"].update({counterName: tempDict})

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
    # Load Config File and return populated settingsDict

    blankDict = {
        "sourcePorts": {},
        "maps": {},
        "gameplay": {},
        "misc": {},
        "previous": {}
    }

    settingsDict = settingsReader(blankDict, "Settings.txt")
    # print("Running UZDoom with no arguements...")
    # subprocess.run(sourceport_dict["UZDoom"]["runcommand"]
    # + " ./gameplay/PVT_STONE_V12_5.wad", shell = True)
    # subprocess.run(sourceport_dict["Woof"]["runcommand"], shell=True)

    print("Listing everything in Maps...")
    print(os.listdir("./maps/"))

    print("Listing everything in Gameplay...")
    print(os.listdir("./gameplay/"))

    print("Listing everything in Misc...")
    print(os.listdir("./misc/"))

    print(settingsDict)

    # TODO: Now that I can read a settings file, create one

    # Store last configs for later use

    # Configure SourcePort

    # Add Gameplay WAD (optional)

    # Select Map WADs

print("END OF PROGRAM")

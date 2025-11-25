import os
import subprocess

path = os.getcwd()


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
        # print("Examining " + i)
        # print("Current Setting is: " + currentSetting)
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
                    tempDict["listing"] = i
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
                    tempDict["listing"] = i
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
                    tempDict["listing"] = i
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

# TODO: Print output and confirm before returning the itemDict


def detailAdder(itemDict, itemType):
    if (itemType == "sourcePorts"):
        itemDict["description"] = input("Source Port Description: ")
    if (itemType == "maps"):
        itemDict["name"] = input("Map WAD Name: ")
        itemDict["description"] = input("Map Description: ")
    if (itemType == "gameplay"):
        itemDict["name"] = input("Gameplay WAD Name: ")
        itemDict["description"] = input("Gameplay Description: ")
    if (itemType == "misc"):
        itemDict["name"] = input("Misc WAD Name: ")
        itemDict["description"] = input("WAD Description: ")

    return itemDict

# TODO: Ensure only .wad files get added to lists


def settingsGen(mapList, gameList, miscList):
    result = ""
    # Add a spot for Source Ports
    result = result + "[Source Ports]\n"
    # Add the maps
    result = result + "[Maps]\n"
    for i in mapList:
        if ((i.split('.'))[1].lower() == "wad"):
            result = result + str(i) + "\n"
    # Add the gameplay wads
    result = result + "[Gameplay]\n"
    for i in gameList:
        if ((i.split('.'))[1].lower() == "wad"):
            result = result + str(i) + "\n"
    # Add misc wads
    result = result + "[Misc]\n"
    for i in miscList:
        if ((i.split('.'))[1].lower() == "wad"):
            result = result + str(i) + "\n"
    result = result + "[Last Used]"

    return result


def settingsSave(mainDict):
    result = ""

    # Add Source Ports
    result = result + "[Source Ports]\n"
    for i in mainDict["sourcePorts"]:
        result = result + mainDict["sourcePorts"][i]["title"] + "\n"
        for j in mainDict["sourcePorts"][i].keys():
            if not (j == "title"):
                result = result + "--" + j + "=" + \
                    mainDict["sourcePorts"][i][j] + "\n"

    # Add Maps
    result = result + "[Maps]\n"
    for i in mainDict["maps"]:
        result = result + mainDict["maps"][i]["listing"] + "\n"
        for j in mainDict["maps"][i].keys():
            if not (j == "listing"):
                result = result + "--" + j + "=" + \
                    mainDict["maps"][i][j] + "\n"

    # Add Gameplay
    result = result + "[Gameplay]\n"
    for i in mainDict["gameplay"]:
        result = result + mainDict["gameplay"][i]["listing"] + "\n"
        for j in mainDict["gameplay"][i].keys():
            if not (j == "listing"):
                result = result + "--" + j + "=" + \
                    mainDict["gameplay"][i][j] + "\n"

    # Add Misc
    result = result + "[Misc]\n"
    for i in mainDict["misc"]:
        result = result + mainDict["misc"][i]["listing"] + "\n"
        for j in mainDict["misc"][i].keys():
            if not (j == "listing"):
                result = result + "--" + j + "=" + \
                    mainDict["misc"][i][j] + "\n"

    # Add Last Used
    result = result + "[Last Used]" + "\n"
    for i in mainDict["previous"]:
        result = result + i + "\n"

    return result


# INFO: MAIN METHOD!
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

    if (os.path.isfile('settings.txt')):
        settingsDict = settingsReader(blankDict, "settings.txt")
    else:
        maps = os.listdir("./maps/")
        game = os.listdir("./gameplay/")
        misc = os.listdir("./misc/")

        print("Writing to file...")
        with open("settings.txt", "w") as f:
            f.write(settingsGen(maps, game, misc))
            f.close()

        # This is so fucking jank
        settingsDict = settingsReader(blankDict, "settings.txt")

        # Insert a Source Port
        print("Add a Source Port.")
        portName = input("Source Port Name: ")
        portCommand = input("Launch Command: ")

        print("Port Name: " + portName + "\nPort Command: " + portCommand)
        newPort = {
            "title": portName,
            "runcommand": portCommand
        }
        settingsDict["sourcePorts"].update({"01": newPort})

        print("Testing out trying to add detail to all maps...")
        for i in range(len(settingsDict["maps"])):
            mapDict = settingsDict["maps"][str(i+1).zfill(2)]
            mapListing = mapDict["listing"]
            print("Enter description for " + mapListing + ": ")
            settingsDict["maps"].update(
                {(str(i+1).zfill(2)): detailAdder(mapDict, "maps")})

        print(settingsDict)
        print("\n\n Saving to new file!")
        with open("settings.txt", "w") as f:
            f.write(settingsSave(settingsDict))
            f.close()

    # print("Running UZDoom with no arguements...")
    # subprocess.run(sourceport_dict["UZDoom"]["runcommand"]
    # + " ./gameplay/PVT_STONE_V12_5.wad", shell = True)
    # subprocess.run(sourceport_dict["Woof"]["runcommand"], shell=True)

    # Configure SourcePort

    # Add Gameplay WAD (optional)

    # Select Map WADs

print("END OF PROGRAM")

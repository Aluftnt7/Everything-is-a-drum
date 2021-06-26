import pygame.mixer
from time import sleep
from pynput import keyboard
import time
import os.path
from os import path

set_idx = 0
sound_arr_a = ["kick.ogg","clap.ogg","hat.ogg", "openhat.ogg", "snr.ogg", "left.ogg", "right.ogg", "up.ogg","down.ogg"]
sets = ["elctroset", "acoustic", "vinyl", "farts", "punch", "family_guy", "tank_drum"]
keys_dict = {"w" : 0, "a" : 1, "s" : 2, "d" : 3, "space" : 4, "right" : 5, "up" : 6, "left" : 7, "down" : 8}
sounds ={"elctroset": [], "acoustic":[], "vinyl":[] , "farts":[], "punch":[], "family_guy":[], "tank_drum":[]}

def load_sounds():
    for set in sets:
        for sound in sound_arr_a:
            path_exists = get_path_exists("/home/pi/Desktop/burn/"+ set + "/" + sound) 
            if(path_exists):
                sounds.get(set).append(pygame.mixer.Sound("/home/pi/Desktop/burn/"+ set + "/" + sound))
          

def play_key(key):
    
    if(key in keys_dict and keys_dict[key] < len(sounds[sets[set_idx]])):
        #pygame.mixer.Channel(keys_dict[key]).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
        pygame.mixer.find_channel(True).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
    
        
def on_changing_set():
        global set_idx
        set_idx += 1
        set_idx %= len(sets)


def on_press(key):
    if hasattr(key, 'char'):
        key = '{0}'.format(key.char)
    else:
        key = '{0}'.format(key)[4:]
    if key == '0':
        on_changing_set()
    play_key(key)

def get_path_exists(path):
    path_exists =  os.path.exists(path)
    return path_exists


def on_release(key):
    if key == keyboard.Key.esc:
        print("Done!")
        # Stop listener
        return False
    
def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join() # wait for listener stop

def main():
    pygame.mixer.pre_init(48000, -16, len(keys_dict), 1024)
    pygame.mixer.quit()
    pygame.init()
    pygame.mixer.init(48000, -16, len(keys_dict), 1024)
    load_sounds()
    wait_for_user_input()
  
if __name__== "__main__":
      main()



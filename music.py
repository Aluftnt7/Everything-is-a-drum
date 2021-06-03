from playsound import playsound
import keyboard
from pynput.keyboard import Key, Listener
import os.path
from os import path


set_idx = 0
sound_arr_a = ["kick.wav","clap.wav","hat.wav", "openhat.wav", "snr.wav", "up.wav", "down.wav", "left.wav", "right.wav"]
sets = ["elctroset", "acoustic", "vinyl", "farts", "cough"]
keys_dict = {"w" : 0, "a" : 1, "s" : 2, "d" : 3, "space" : 4, "right" : 5, "up" : 6, "left" : 7, "down" : 8}
sounds ={"elctroset": [], "acoustic":[], "vinyl":[], "farts":[], "cough":[]}

def load_sounds():
    for set in sets:
        for sound in sound_arr_a:
            sounds.get(set).append("./"+ set + "/" + sound)



def play_key(key):
    path_exists = path.exists(sounds[sets[set_idx]][keys_dict[key]]) 
    if(key in keys_dict and path_exists):
        playsound(sounds[sets[set_idx]][keys_dict[key]], False)


def on_changing_set():
        global set_idx
        set_idx += 1
        set_idx %= len(sets)


def on_press(key):
    if hasattr(key, 'char'):
        key = '{0}'.format(key.char)
        if key == '0':
            on_changing_set()
            return 
    else:
        key = '{0}'.format(key)[4:]
    play_key(key)


def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
load_sounds()
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


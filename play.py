import pygame.mixer
from time import sleep
import keyboard
from pynput.keyboard import Key, Listener


set_idx = 0
sound_arr_a = ["kick.wav","clap.wav","hat.wav", "openhat.wav", "snr.wav"]
sets = ["elctroset", "acoustic", "vinyl", "farts"]
keys_dict = {"w" : 0, "a" : 1, "s" : 2, "d" : 3, "space" : 4}
sounds ={"elctroset": [], "acoustic":[], "vinyl":[], "farts":[]}

def load_sounds():
    for set in sets:
        for sound in sound_arr_a:
            sounds.get(set).append(pygame.mixer.Sound("./"+ set + "/" + sound))
    # print(sounds)        


def play_key(key):
    if(key in keys_dict):
        sounds[sets[set_idx]][keys_dict[key]].play()
        
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


def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        print("Done!")
        # Stop listener
        return False

pygame.mixer.init(48000, -16, 2, 1024)
load_sounds()

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
# while True:
#     sleep(1)
    




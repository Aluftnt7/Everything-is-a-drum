from playsound import playsound
import keyboard
from pynput.keyboard import Key, Listener


set_idx = 0
sound_arr_a = ["kick.wav","clap.wav","hat.wav", "openhat.wav", "snr.wav"]
sets = ["elctroset", "acoustic", "vinyl"]
keys_dict = {"w" : 0, "a" : 1, "s" : 2, "d" : 3, "space" : 4}



def play_key(key):
    if(key in keys_dict):
        playsound("./" + sets[set_idx] + "/" + sound_arr_a[keys_dict[key]], False)


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
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



# import pygame

# pygame.init()
# pygame.mixer.init()
# pygame.display.set_caption("EVERYTHING IS A DRUM")
# pygame.display.set_mode((400, 400), 0, 32)


# set_idx = 0
# sound_arr_a = ["kick.wav","clap.wav","hat.wav", "openhat.wav", "snr.wav"]
# sets = ["elctroset", "acoustic", "vinyl"]
# keys_dict = {"w" : 0, "a" : 1, "s" : 2, "d" : 3, "space" : 4}



# def on_press(key):
#     print(key)
#     if(key in keys_dict):
#         pygame.mixer.Sound("./" + sets[set_idx] + "/" + sound_arr_a[keys_dict[key]]).play()


# def on_changing_set():
#         global set_idx
#         set_idx += 1
#         set_idx %= len(sets)


# while True:
#     for event in pygame.event.get(): 
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 pygame.quit(); #sys.exit() if sys is imported
#             on_press(pygame.key.name(event.key))
#             if event.key == pygame.K_0:
#                 on_changing_set()


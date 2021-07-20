import pygame.mixer
from time import sleep
from pynput import keyboard, mouse
import time
import os
import board
import neopixel
import random

from threading import Thread

from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.color import PURPLE, WHITE, AMBER, JADE, MAGENTA, ORANGE, GOLD, PINK, AQUA, CYAN, TEAL, RED, YELLOW, GREEN

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 599

pixels = neopixel.NeoPixel(pixel_pin, 599, brightness=0.5, auto_write=False)

chase = Chase(pixels, speed=0.1, size=3, spacing=0, color=WHITE)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=3, spacing=2, step=8)

is_not_touched = True
first_touch = 0
set_idx = 0
sound_arr_a = ["clap.ogg","htom.ogg","mtom.ogg", "ltom.ogg","hbongo.ogg","lbongo.ogg","openhat.ogg", "kick.ogg", "snr.ogg","stick.ogg", "cymbal.ogg","gong.ogg"]
sets = ["family_guy","elctroset", "acoustic", "vinyl", "farts", "punch", "tank_drum", "marimba", "glockenspiel","80s_drum"]
keys_dict = {"w" : 4, "a" : 5,"s" : 3,"d" : 2,"f" : 1,"g" : 0,"up": 6,"down": 7,"left" : 8,"right" : 9,"click" : 10,"space" : 11}
sounds ={"family_guy": [],"elctroset": [], "acoustic":[], "vinyl":[] , "farts":[], "punch":[], "tank_drum":[], "marimba":[], "glockenspiel":[], "80s_drum":[]}
led_arr ={ 0:[0,60],1:[61,120],2:[121,180],3:[181,222],4:[223,300],5:[301,380],6:[381,425],7:[426,469], 8:[470,514],9:[515,558],10:[559,599]}
color_list = [PURPLE, WHITE, AMBER, JADE, MAGENTA, ORANGE, GOLD, PINK, AQUA, CYAN, TEAL, RED, YELLOW, GREEN]

def load_sounds():
    base_path = os.getenv("DRUM_HOME","/home/pi/projects/Everything-is-a-drum")
    for set in sets:
        for sound in sound_arr_a:
            path_exists = os.path.exists(base_path + "/" + set + "/" + sound)
            if(path_exists):
                sounds.get(set).append(pygame.mixer.Sound(base_path + "/" + set + "/" + sound))
          
def play_key(key):

    if(key in keys_dict and keys_dict[key] < len(sounds[sets[set_idx]])):
        #pygasdwame.mixer.Channel(keys_dict[key]).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
        global first_touch
        global is_not_touched
        first_touch = time.time()
        pygame.mixer.find_channel(True).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
        handle_blink(keys_dict[key])
        is_not_touched = False

def handle_blink(key):
    if(key == 11 or key == 7):
        pulse_all()
        return
    blink(led_arr[key][0],led_arr[key][1])
        
def pulse_all():
        pixels.fill((255,255,255))
        pixels.show()
     
def blink(first_led, last_led):

        pixels[first_led:last_led] = [random.choice(color_list)] * (len(pixels))
        pixels.show()
        time.sleep(0.001)
        pixels.fill((0,0,0))
        pixels.show()

def on_changing_set(key):
        global set_idx
        set_idx += 1
        set_idx %= len(sets) 
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
        while pygame.mixer.Channel(0).get_busy():
            chase.animate()
           # pixels.fill((0,0,0))
           # pixels.show()
        
def run_leds():
    global first_touch
    global is_not_touched
    
    if(is_not_touched):
            rainbow_chase.animate()
        
    time_elapsed_from_first_touch = time.time()
    total_time_elapsed = round(time_elapsed_from_first_touch - first_touch)
    if(total_time_elapsed < 10):
        is_not_touched = False
        pixels.fill((0,0,0))
        pixels.show()
            
    else:
        is_not_touched = True
      
        


def on_press(key):
    if hasattr(key, 'char'):
        key = '{0}'.format(key.char)
    else:
        key = '{0}'.format(key)[4:]
        if key == 'space':
            on_changing_set(key)
            return
    play_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Done!")
        # Stop listener
        return False
    
def on_click(x, y, button, pressed):
    if(pressed):
        play_key('click')
 #   if not pressed:
        # Stop listener
  #      return False
    
def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_click=on_click)
    listener.start()
    mouse_listener.start()
    
    listener.join() # wait for listener stop
    mouse_listener.join()

def main():
    pygame.mixer.pre_init(48000, -16, len(keys_dict), 1024)
    pygame.mixer.quit()
    pygame.init()
    pygame.mixer.init(48000, -16, len(keys_dict), 1024)
    load_sounds()

  
if __name__== "__main__":
    t1 = Thread(target = run_leds)
    t1.setDaemon(True)
    t1.start()
    t2 = Thread(target = wait_for_user_input)
    t2.setDaemon(True)
    t2.start()
    main()

    while True:
        run_leds()






   

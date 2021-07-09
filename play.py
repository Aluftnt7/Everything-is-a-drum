import pygame.mixer
from time import sleep
from pynput import keyboard
import time
import os
import board
import neopixel

from threading import Thread

from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbowchase import RainbowChase

from adafruit_led_animation.color import PURPLE, WHITE, AMBER, JADE, MAGENTA, ORANGE

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 300

pixels = neopixel.NeoPixel(pixel_pin, 300, brightness=0.5, auto_write=False)


chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=WHITE)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=3, spacing=2, step=8)

is_not_touched = True
first_touch = 0
set_idx = 0
sound_arr_a = ["kick.ogg","clap.ogg","hat.ogg", "openhat.ogg", "snr.ogg", "left.ogg", "right.ogg", "up.ogg","down.ogg"]
sets = ["family_guy","elctroset", "acoustic", "vinyl", "farts", "punch", "tank_drum"]
keys_dict = {"w" : 0, "a" : 1, "s" : 2, "d" : 3, "space" : 4, "right" : 5, "up" : 6, "left" : 7, "down" : 8}
sounds ={"family_guy": [],"elctroset": [], "acoustic":[], "vinyl":[] , "farts":[], "punch":[], "tank_drum":[]}



def load_sounds():
    base_path = os.getenv("DRUM_HOME","/home/pi/Desktop/burn_with_leds")
    for set in sets:
        for sound in sound_arr_a:
            path_exists = os.path.exists(base_path + "/" + set + "/" + sound)
            if(path_exists):
                sounds.get(set).append(pygame.mixer.Sound(base_path + "/" + set + "/" + sound))
          
def play_key(key):
    if(key in keys_dict and keys_dict[key] < len(sounds[sets[set_idx]])):
        #pygame.mixer.Channel(keys_dict[key]).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
        global first_touch
        global is_not_touched
        first_touch = time.time()
  
        pygame.mixer.find_channel(True).play(pygame.mixer.Sound(sounds[sets[set_idx]][keys_dict[key]]))
        handle_blink(keys_dict[key])
        is_not_touched = False
        t2 = Thread(target = check_key_touched)
        t2.setDaemon(True)
        t2.start()
        
        

        


def handle_blink(key):
    if(key == 0):
        pulse_all()
        return
    first_led , last_led = define_pixels(key)
    blink(first_led, last_led)
    

def define_pixels(key):
    first_led = 0
    last_led = 0

    if(key <= 2):
        first_led = 0
        last_led = 90
    elif(key > 2 and key <= 5):
        first_led = 90 saaw
        last_led = 180
    elif(key > 5 and key <= 8):
        first_led = 180
        last_led = 300
    
    return first_led, last_led
    
    
    
def pulse_all():
    
        pixels.fill((255,255,255))
        pixels.show()
        #time.sleep(0.00001)
        pixels.fill((0,0,0))
        pixels.show()

    
def blink(first_led, last_led):

        red = (225,0,0)
        pixels[first_led:last_led] = [red] * (len(pixels))
        pixels.show()
        time.sleep(0.001)
        pixels.fill((0,0,0))
        pixels.show()
        
def on_changing_set():
        global set_idx
        set_idx += 1
        set_idx %= len(sets) 
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('/home/pi/Desktop/burn_with_leds/general_sounds/change_preset.ogg'))
        while pygame.mixer.Channel(0).get_busy():
            chase.animate()
            pixels.fill((0,0,0))
            pixels.show()
        


def run_static_leds():
    global is_not_touched
    while True:
        if(is_not_touched):
            rainbow_chase.animate()
        
    
def check_key_touched():
    global first_touch
    global is_not_touched
    
    
    while True:
        time_elapsed_from_first_touch = time.time()
        total_time_elapsed = round(time_elapsed_from_first_touch - first_touch)
        if(total_time_elapsed < 10):
            is_not_touched = False
            pixels.fill((0,0,0))
            pixels.show()
            
        else:
            is_not_touched = True
            return False

      
        


def on_press(key):
    if hasattr(key, 'char'):
        key = '{0}'.format(key.char)
    else:
        key = '{0}'.format(key)[4:]
        if key == 'space':
            on_changing_set()
            return
    play_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Done!")
        # Stop listener
        return False
    
def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    run_static_leds()
    listener.join() # wait for listener stop
    

def main():
    print('inside main')
    pygame.mixer.pre_init(48000, -16, len(keys_dict), 1024)
    pygame.mixer.quit()
    pygame.init()
    pygame.mixer.init(48000, -16, len(keys_dict), 1024)
    load_sounds()
    wait_for_user_input()

  
if __name__== "__main__":
    main()
    #t2 = Thread(target = wait_for_user_input)
    #t2.setDaemon(True)
    #t2.start()
    #while True:
     #   pass





   

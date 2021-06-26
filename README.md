# Everything-is-a-drum

A cool burn project using makey makey, neopixel led strips and a button to switch sets. 

## Installation packages
Inorder to run neopixel we should use python3 as root

CircuitPython - https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

```
sudo python3 -m pip install --force-reinstall
```

CircuitPython Libraries LED lib and examples are taken from:
https://circuitpython.org/libraries  (Bundle Version py)

### LED settings in files

```
#Update to match the pin connected to your NeoPixels
`pixel_pin = board.D18`
#Update to match the number of NeoPixels you have connected
#5 meters neopixel strip
pixel_num = 300
```

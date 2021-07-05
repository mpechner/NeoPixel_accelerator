import board
import neopixel
import time
import busio
import adafruit_lis3dh




print(dir(board))

num_pixels = 30
blinkspeed = 0.1
pixels = neopixel.NeoPixel(board.D10, num_pixels)
def pixel_base():
    global blinkspeed, pixels


    for ii in range(0,30,3):
        pixels[ii] = (10,0,0)

    for ii in range(1,30,3):
        pixels[ii] = (0,10,0)

    for ii in range(2,30,3):
        pixels[ii] = (0,0,10)


    while(True):
        accel()
        for ii in range(len(pixels)):

            if pixels[ii]  == (10,0,0):
                pixels[ii] = (0,10,0)
            elif pixels[ii] == (0,10,0):
                pixels[ii] = (0,0,10)
            else:
                pixels[ii] = (10,0,0)

        time.sleep(blinkspeed)



def blink_colors():
    pixels = neopixel.NeoPixel(board.D10, num_pixels)
    pixels.fill(0x110000)
    time.sleep(.5)
    pixels.fill(0x0011000)
    time.sleep(.5)
    pixels.deinit()



lastrate=0
rate = 0
if hasattr(board, "ACCELEROMETER_SCL"):
        i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
        lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
elif hasattr(board, "ACCELEROMETER_INTERRUPT"):
        lis3dh = adafruit_lis3dh.LIS3DH_I2C(board.I2C(), address=0x19)
else:
        i2c = board.I2C()  # uses board.SCL and board.SDA
        lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Hardware SPI setup:
# spi = board.SPI()
# cs = digitalio.DigitalInOut(board.D5)  # Set to correct CS pin!
# lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs)

# PyGamer or MatrixPortal I2C Setup:
# i2c = board.I2C()  # uses board.SCL and board.SDA
# lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)


# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G

def accel():
    global lastrate, lis3dh, rate, blinkspeed
    # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
    # SPDX-License-Identifier: MIT
    # Hardware I2C setup. Use the CircuitPlayground built-in accelerometer if available;
    # otherwise check I2C pins.


    # Loop forever printing accelerometer values


    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
    # z axis values.  Divide them by 9.806 to convert to Gs.
    x, y, z = [
        value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration
    ]
    lastrate = rate
    rate = x + y + z
    print("Last: ", lastrate, "Rate: ", rate)
    #print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    # Small delay to keep things responsive but give time for interrupt processing.
    diff = lastrate - rate
    print("diff:",diff)
    if diff  > 0.1:
        if rate >6:
            blinkspeed  = 0.02
        elif rate > 4:
            blinkspeed = 0.01
        elif rate > 3:
            blinkspeed = 0.1
        elif rate > 1:
            blinkspeed = 0.3
        else:
            blinkspeed = 0.5

    print("b speed:", blinkspeed)

pixel_base()

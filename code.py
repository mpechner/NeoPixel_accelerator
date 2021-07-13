import board
import neopixel
import time
import busio
import adafruit_lis3dh

#
# Is actionally the main loop_num
# Initially sets the neopixels R, G, b
# Then on each loop R->G,  G->B, B->R
# Each call to accel sets the   time to sleep for each blink
# Also set the number of time to loop to run for 5 seconds
#
def pixel_base():
    global pixels, loop_num

    for ii in range(0, 30, 3):
        pixels[ii] = (10, 0, 0)

    for ii in range(1, 30, 3):
        pixels[ii] = (0, 10, 0)

    for ii in range(2, 30, 3):
        pixels[ii] = (0, 0, 10)

    while True:
        blinkspeed= accel()

        for doblink in range(int(5 * (1/blinkspeed))):
            for ii in range(len(pixels)):
                if pixels[ii] == (10, 0, 0):
                    pixels[ii] = (0, 10, 0)
                elif pixels[ii] == (0, 10, 0):
                    pixels[ii] = (0, 0, 10)
                else:
                    pixels[ii] = (10, 0, 0)
            time.sleep(blinkspeed)


#
# Pick the largest value, X, Y or Z then decindes to the sleep time.
#
def accel():
    # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
    # SPDX-License-Identifier: MIT
    # Hardware I2C setup. Use the CircuitPlayground built-in accelerometer if available;
    # otherwise check I2C pins.
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
    # z axis values.  Divide them by 9.806 to convert to Gs.
    x, y, z = [
        value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration
    ]

    rate = x
    if y > rate:
        rate = y
    elif z > rate:
        rate = z

    if rate >= 3.0:
        blinkspeed = 0.01
    elif rate > 2.0:
        blinkspeed = 0.05
    elif rate > 1.6:
        blinkspeed = 0.1
    elif rate > 0.6:
        blinkspeed = 0.3
    else:
        blinkspeed = 0.5


    # print("b speed:", blinkspeed)
    return blinkspeed

num_pixels = 30

pixels = neopixel.NeoPixel(board.D10, num_pixels)

if hasattr(board, "ACCELEROMETER_SCL"):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
elif hasattr(board, "ACCELEROMETER_INTERRUPT"):
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(board.I2C(), address=0x19)
else:
    i2c = board.I2C()  # uses board.SCL and board.SDA
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_4_G

pixel_base()

Right now just playing on a magtag.  Because it is the only board with the correct 3 pin connector for the neopixel strip I have.

# Requirements:
## Nopixel Library 
* https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
## Accelerometer Lib: 
* https://github.com/adafruit/Adafruit_CircuitPython_LIS3DH
* https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout
* https://www.st.com/content/st_com/en/products/mems-and-sensors/accelerometers/lis3dh.html#documentation

# Neopixel Transition
I figured out how to initilize a pattern and make it transition colors down the strip. From ...
* Red to Blue
* Blue to Green
* Green to Red

# Accelerometer
What I need to do is correctly write the code so the pixels will transition faster or slower depending on the speed of the skate board I hope to mount this on.
First crack at it was bad.  Add the x,y and z values and compare to previous reading.

I found this page https://www.smartconversion.com/unit_calculation/Acceleration_calculator.aspx
I will assume G at 2 max.  Long board cruising.

# It's a Secret
Sssshhhh making this for my neice to mount on her longboard.

import time
from datetime import datetime
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont, ImageDraw

# Initialize the I2C interface
serial = i2c(port=3, address=0x3C)

# Create the SH1106 OLED display device
device = sh1106(serial)

# Use a built-in font or specify a TTF font file
font = ImageFont.load_default()
# If you want to use a TTF font file, uncomment the next line and specify the font path
# font = ImageFont.truetype("path/to/font.ttf", size)

# Function to display the current time
def display_time():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        with canvas(device) as draw:
            draw.text((30, 20), current_time, font=font, fill=255)
        
        time.sleep(1)

try:
    display_time()
except KeyboardInterrupt:
    pass

print("Stopped displaying the clock.")


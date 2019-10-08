import time
import os.path
from PIL import Image
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1327


def main():
    serial = i2c(port=0, address=0x3C)
    device = ssd1327(serial, 128, 128)

    images = [
        "oled.qr.png",
        "oled.network.png",
        "oled.hardware.png"
    ]

    counter = 0
    while True:
        number = len(images)
        file = images[counter % number]

        img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', file))
        image = Image.open(img_path).convert("RGBA").rotate(180)

        background = Image.new("RGBA", device.size, "black")
        posn = ((device.width - image.width) // 2, 0)

        background.paste(image, posn)
        device.display(background.convert(device.mode))
        time.sleep(2)

        counter = counter +1
        continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
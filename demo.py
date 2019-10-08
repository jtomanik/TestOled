import os.path
from PIL import Image
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1327


def main():
    serial = i2c(port=0, address=0x3C)
    device = ssd1327(serial, 128, 128)
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'images', 'oled.network.png'))
    qr_code = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "black")
    posn = ((device.width - qr_code.width) // 2, 0)

    background.paste(qr_code, posn)
    device.display(background.convert(device.mode))

    while True:
        continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
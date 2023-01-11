import qrcode
from PIL import Image

qr = qrcode.QRCode()
qr.add_data("https://github.com/animeshg93")
qr.make(fit=True)
img = qr.make_image()

img.save("sample.png")
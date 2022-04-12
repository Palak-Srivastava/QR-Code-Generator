import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=2)

qr.add_data("www.google.com")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("newGoogle.png")
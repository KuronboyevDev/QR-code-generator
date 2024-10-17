import qrcode as qr
img = qr.make('https://www.instagram.com/leomessi/')
type(img)
img.save("my_insta.png")
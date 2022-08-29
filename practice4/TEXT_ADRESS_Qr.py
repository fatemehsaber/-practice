import qrcode

text_adress = input('enter the text and adress : ')


Qr = qrcode.make(text_adress)
Qr.save('test_adress.jpg')
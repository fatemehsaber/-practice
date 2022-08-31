import qrcode

text = input("Enter the text: ")
address = input("Enter the address: ")

qr1 = qrcode.make(text)
qr2 = qrcode.make(text)

qr1.save("qrcode1.jpg")
qr2.save("qrcode2.jpg")

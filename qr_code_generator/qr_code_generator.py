# Program to generate an QR Code from user entered text or URL
import qrcode

user_data = input("Enter the text or URL: ").strip()
qr_code_filename = input("Enter the filename: ").strip()

img = qrcode.make(user_data)
type(img)
img.save(qr_code_filename)
print(f"QR code saved as {qr_code_filename}")

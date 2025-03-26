import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image
from datetime import datetime

def generate_qr(data, filename, file_format):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{filename}_{timestamp}.{file_format}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)
    print(f"QR code saved as {filename}\n")

def read_qr(filename):
    if os.path.exists(filename):
        img = Image.open(filename)
        result = decode(img)

        if result:
            print("Decoded data:", {result[0].data.decode("utf-8")}, "\n")
        else:
            print("No QR code found in the image.\n")
    else:
        print(f"Error: File '{filename}' does not exist.\n")

while True:
    print("\nQR Code Generator & Reader")
    print("1. Generate a QR code")
    print("2. Read a QR code")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == "1":
        user_name = input("Enter a name for the QR code (file name): ").strip()
        data = input("Enter the data for the QR code: ").strip()
        file_format = input("Enter file format (png/jpg/jpeg): ").strip().lower()

        if file_format not in ["png", "jpg", "jpeg"]:
            print("Invalid format! Defaulting to PNG.")
            file_format = "png"

        generate_qr(data, user_name, file_format)

    elif choice == "2":
        user_name = input("Enter the file name (without extension or with .png/.jpg/.jpeg): ").strip()

        if "." in user_name:
            filename = user_name
        else:
            possible_files = [f"{user_name}.png", f"{user_name}.jpg", f"{user_name}.jpeg"]
            filename = next((f for f in possible_files if os.path.exists(f)), None)

        if filename and os.path.exists(filename):
            read_qr(filename)
        else:
            print(f"Error: No matching file found for '{user_name}' in PNG, JPG, or JPEG format.\n")

    elif choice == "3":
        print("Exiting program. Have a great day!")
        break

    else:
        print("Invalid option! Please enter 1, 2, or 3.\n")

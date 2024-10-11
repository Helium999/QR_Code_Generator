import qrcode as qr
from PIL import Image
from time import sleep
from sys import exit

#Designing the QR Code
qr_code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=3
)

#Taking input data for the QR Code
while True:
    text = input("Input the text/link you want to encode in your QR code: ").strip()

    if text:
        break
    else:
        print("This field cannot be left empty.\n")

qr_code.add_data(text)
qr_code.make(fit=True)

#Taking input for the colour of the QR Code and the background
colours = ["black", "white", "grey", "blue", "red", "green", "yellow", "pink"]
while True:
    qr_colour = input(f"Select the colour of your QR code: {colours}: ").lower().strip()
    if qr_colour:
        if qr_colour in colours:
            break
        else:
            print("Please enter a colour name among the options provided.\n")
    else:
        print("This field cannot be left empty.\n")

while True:
    qr_bg_colour = input(f"Select the colour of your QR code's background: {colours}: ").lower().strip()
    if qr_bg_colour:
        if qr_bg_colour in colours:
            break
        else:
            print("Please enter a colour name among the options provided.\n")
    else:
        print("This field cannot be left empty.\n")

#Generating the QR Code image
img = qr_code.make_image(fill_color=qr_colour, back_color=qr_bg_colour)

#Taking the input for file name of the image
i = 1
while i == 1:
    name = input("\nEnter the name of the QR code to save the image: ").strip()
    if name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".tiff"):
        if not name.endswith(".png"):
            print("\nOnly .png format supported")
        reverse_name = name[::-1]
        reverse_name = reverse_name.replace("gnp.", "", 1)
        reverse_name = reverse_name.replace("gpj.", "", 1)
        reverse_name = reverse_name.replace("gepj.", "", 1)
        reverse_name = reverse_name.replace("ffit.", "", 1)
        name = reverse_name[::-1]

#Confirmation for saving the file with the input name
    j = 1
    while j == 1:
        confirm_save = input(f"Are you sure you want to save your QR code image as {name}.png (y/n): ")
        if confirm_save == "y" or confirm_save == "yes":
            i = 0
            j = 0
        elif confirm_save == "n" or confirm_save == "no":
            print("\nThe image was not saved by the previously entered name.")
            k = 1
            while k == 1:
                choice = input("To provide a new name, enter \"n\".\nTo exit the program completely, enter \"e\": ")
                if choice == "n" or choice == "new":
                    j = 0
                    k = 0
                elif choice == "e" or choice == "exit":
                    exit()
                else:
                    print("\nInvalid input!")
        else:
            print("\nInvalid input! Enter \"y\" to confirm or \"n\" to cancel.")

#Saving the image
img.save(f"{name}.png")

#Displaying the image
print("\nThe QR code image was successfully saved.\nOpening the QR code image in...")
sleep(1)
print("3...", end=" ")
sleep(1)
print("2...", end=" ")
sleep(1)
print("1...")

open_img = Image.open(f"{name}.png")
open_img.show()
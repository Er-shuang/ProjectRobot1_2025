# Author: Yujin Nie
# Date: 24/6/25
# Description: Display face ID numbers received from K210 on LED matrix

# Import everything from the microbit library.
from microbit import *

uart.init(baudrate=9600, rx=pin1)

# Define number images
numbers = {
    "1": Image("09990:" "00900:" "00900:" "00990:" "00900"),
    "2": Image("99990:" "00900:" "09000:" "90090:" "09900"),
    "3": Image("09900:" "90090:" "09000:" "90000:" "09900"),
    "U": Image("90009:" "09090:" "00900:" "09090:" "90009"),
}

# Create a buffer to store the received characters
buffer = ""
display.scroll("WAIT")

# Main loop
while True:
    if uart.any():
        char = uart.read(1).decode("utf-8")
        print(char)
        if char == ",":
            if buffer == "N":
                display.show(Image.HAPPY)  # No face
                print("No face")
            # Whether the ID is valid
            elif buffer in numbers:
                # registered face id
                display.show(numbers[buffer])
                print("Display:", buffer)
            else:
                # no register face id
                display.show(numbers["U"])
                print("Unknown message:", buffer)
            buffer = ""
        else:
            buffer += char

    sleep(50)

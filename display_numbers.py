# Author: Yujin Nie
# Data: 21/6/25
# Description: Display different numbers(1、2、3) on led matrix

# Import everything from the microbit library.
from microbit import *

# Define 1,2,3 numbers
numbers = {
    "1": Image("00100:" "01100:" "00100:" "00100:" "01110"),
    "2": Image("00110:" "01001:" "00010:" "00100:" "01111"),
    "3": Image("01100:" "00010:" "00100:" "00010:" "01100"),
}

# Display 1,2,3 numbers in a circle
while True:
    for number in ["1", "2", "3"]:
        display.show(numbers[number])  # Display numbers
        print("Now displaying:", number)  # Display result in terminal
        sleep(1000)  # Each number display for 1 second

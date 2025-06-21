# Author: Yujin Nie
# Data: 21/6/25
# Description: Display different numbers(1、2、3) on led matrix

# Import everything from the microbit library.
from microbit import *

# Define 1,2,3 numbers
numbers = {
    "1": Image("09990:" "00900:" "00900:" "00990:" "00900"),
    "2": Image("99990:" "00900:" "09000:" "90090:" "09900"),
    "3": Image("09900:" "90090:" "09000:" "90000:" "09900"),
}

# Display 1,2,3 numbers in a circle
while True:
    for number in ["1", "2", "3"]:
        display.show(numbers[number])  # Display numbers
        print("Now displaying: ", number)  # Display result in terminal
        sleep(1000)  # Each number display for 1 second

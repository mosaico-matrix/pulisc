from mosaico import widget, config
import os
from datetime import datetime

# Load roommates from config
roommates = config["roommates"]
current_index=0

# Select the current roommate
current_roommate = roommates[current_index]

# Vacuum
vacuum = widget.createImage()
vacuum.setImage(widget.widgetAsset("vacuum.ppm"))
vacuum.moveTo(70, 30)
vacuum.animateTo(-40, 30, 4000)

# Name
name = widget.createText()
name.setFont("10x20")
name.setText(current_roommate)

# Called once each frame
flipped = False

def loop():
    name.centerHorizontally()
    global flipped
    if vacuum.isAnimating():
        return
    elif flipped:
        flipped = False
        vacuum.flipHorizontally()
        vacuum.animateTo(-40, 30, 4000)
    else:
        flipped = True
        vacuum.flipHorizontally()
        vacuum.animateTo(80, 30, 4000)


# # Files to store the current index and last date checked
# INDEX_FILE = "current_index.txt"
# DATE_FILE = "last_date.txt"
# 
# def load_index():
#     """Load the current index from the file."""
#     try:
#         if os.path.exists(INDEX_FILE):
#             with open(INDEX_FILE, "r") as file:
#                 return int(file.read().strip())
#     except Exception as e:
#         return 0
#     return 0
# 
# def save_index(index):
#     """Save the current index to the file."""
#     with open(INDEX_FILE, "w") as file:
#         file.write(str(index))
# 
# def load_date():
#     """Load the last date checked from the file."""
#     if os.path.exists(DATE_FILE):
#         with open(DATE_FILE, "r") as file:
#             return file.read().strip()
#     return None
# 
# def save_date(date_str):
#     """Save the current date to the file."""
#     with open(DATE_FILE, "w") as file:
#         file.write(date_str)
# 
# # Load the current index and last date checked
# current_index = load_index()
# last_date = load_date()
# 
# # Get today's date
# today_date = datetime.now().strftime("%Y-%m-%d")
# print("NOGG")
# today = datetime.strptime(today_date, "%Y-%m-%d")
# print("NOGG2")
# 
# # Calculate the number of days passed since the last check
# if last_date:
#     last_checked = datetime.strptime(last_date, "%Y-%m-%d")
#     days_passed = (today - last_checked).days
# else:
#     days_passed = 0
# 
# # Update the index based on the number of days passed
# if days_passed > 0:
#     current_index = (current_index + days_passed) % len(roommates)
#     save_index(current_index)
#     save_date(today_date)
        
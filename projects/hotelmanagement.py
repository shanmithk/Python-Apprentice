from tkinter import messagebox, simpledialog, Tk 
"""
Ask how many people, rooms. amd nights.
Maybe different types of rooms.
Give a price for the stay.
Add and delete people. 
track room number(s)
"""

room_nums = tuple(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15.16,17,18,19,20)   
checked_rooms = list()
rooms = {}
num_rooms = input("How many rooms would you like")
print(int(num_rooms) * 200)
def add_people():
    checked_rooms = ""
    name_people = input("What's your name? How many poeple would you like to check in?")
    rooms_want = input("How many rooms would you like?")
    room_got = input("Which rooms would you like?")
    for i in rooms.values():
        if i not in checked_rooms:
            







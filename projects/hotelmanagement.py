from tkinter import messagebox, simpledialog, Tk 
"""
Ask how many people, rooms. amd nights.
Maybe different types of rooms.
Give a price for the stay.
Add and delete people. 
track room number(s)
"""

room_nums = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15.16,17,18,19,20)   
checked_rooms = list()
rooms = {}
def add_people():
    name_people = input("What's your name?")
    room_got = input(f"Which rooms would you like? The rooms are{room_nums} and the checked out rooms are{checked_rooms}." )
    booked = room_got.split(",")
    price = int(len(booked)) * 200
    print("That will be $" + str(price))
    checked_rooms.extend([int(room)for room in booked])
    for room in booked:
        rooms[int(room)] = name_people
def remove_people():
    name_people = input("What's your name?")
    for room, name in rooms.items():
        if name == name_people:
            del rooms[room]
   


         
            


while room_nums:
    add_people()
    print(rooms)
    print(room_nums)



"""for key, value in rooms.items():
        if value not in checked_rooms:
            key_temp = key"""
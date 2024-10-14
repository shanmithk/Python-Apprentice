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
num_rooms = input("How many rooms would you like")
price = int(num_rooms) * 200
print("That will be $" + str(price))
def add_people():
    checked_rooms = ""
    name_people = input("What's your name?")
    room_got = input("Which rooms would you like? The available rooms are" )
    booked = room_got.split(",")
    for room in booked:
        rooms[int(room)] = name_people
            
 
         
            


add_people()
print(rooms)
print(room_nums)



"""for key, value in rooms.items():
        if value not in checked_rooms:
            key_temp = key"""
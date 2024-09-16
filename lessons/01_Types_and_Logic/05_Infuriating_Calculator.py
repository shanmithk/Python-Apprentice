"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
num1 = input("Enter a number.")
# Ask the user for the second number
num2 = input("Enter another number.")
# Ask the user for the math operation
opp = input("Would you like to add, subtract, divide, or multiply?")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if opp == "multiply":
    print(int(num1)*int(num2))
elif opp == "divide":
    print(int(num1)/int(num2))    
elif opp == "add":
    print(int(num1) + int(num2))
elif opp == "subtract":
    print(int(num1) - int(num2))
else:
    print("Make sure it was one of the options or check for any capitals or spelling errors.")    
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open

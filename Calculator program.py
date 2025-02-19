"""
Memory Calculator with Undo Functionality  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program simulates a **basic calculator** with additional **memory storage**  
and **undo functions** to track calculations. Users can perform addition,  
multiplication, and division, as well as store, recall, and undo values.  

How It Works:  
1. The user **inputs an initial value**.  
2. The user selects an **operation**:  
   - **"+"** to add a number.  
   - **"x"** to multiply by a number.  
   - **"/"** to divide by a number.  
   - **"undo"** to revert to the previous value.  
   - **"undo2"** to revert to an earlier saved value.  
   - **"mem"** to store the current value in memory.  
   - **"rec"** to recall the stored memory value.  
   - **"exit"** to quit the program.  
3. The calculator updates and displays the **current value** after each operation.  
4. Users can **undo changes** or **retrieve stored values** as needed.  

This program demonstrates variable management, function-based calculations,  
and interactive user-driven memory recall features in Python.  
"""

def display_current_value():
    print("Current value:", val)

def add(to_add):
    global val, recall, prev_value
    prev_value = recall
    recall = val
    val += to_add

def mult(to_mult):
    global val, recall, prev_value
    prev_value = recall
    recall = val
    val *= to_mult

def div(to_div):
    global val, recall, prev_value
    if to_div != 0:
        prev_value = recall
        recall = val
        val /= to_div
    else:
        print("Error: Division by zero is not allowed.")

def undo():
    global val, recall, memory
    memory = val
    val = recall
    recall = memory

def undo_2():
    global prev_value, val, recall
    val, recall = prev_value, val

def mem():
    global memory, val
    memory = val

def rec():
    global memory, recall, val
    recall = memory
    val = recall

if __name__ == '__main__':
    global val, recall, memory, prev_value
    val = 0
    recall = 0
    memory = 0
    prev_value = 0

    print("Welcome to the calculator program. Current value: 0")
    val = int(input("Enter initial value: "))
    display_current_value()
    
    action = input("Enter operation (+, x, /, undo, undo2, mem, rec, exit): ")
    
    while action != "exit":
        if action == "+":
            add(int(input("What do you want to add? : ")))
        elif action == "x":
            mult(int(input("What do you want to multiply by? : ")))
        elif action == "/":
            div(int(input("What do you want to divide by? : ")))
        elif action == "undo":
            undo()
        elif action == "undo2":
            undo_2()
        elif action == "mem":
            mem()
        elif action == "rec":
            rec()
        else:
            print("Invalid operation. Try again.")
            
        display_current_value()
        action = input("Enter operation (+, x, /, undo, undo2, mem, rec, exit): ")

    print("Calculator session ended.")

    

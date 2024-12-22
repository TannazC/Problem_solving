def display_current_value():
    print("current value:",val)
    
def add(to_add):
    global val,recall,prev_value
    prev_value=recall
    recall=val
    val+=to_add
    
def mult(to_mult):
    global val,recall, prev_value
    prev_value=recall
    recall=val
    val*=to_mult

def div(to_div):
    global val,recall, prev_value
    prev_value = recall
    recall=val
    val/=to_div

#rewrite with three : val, recall, prev_val 
def undo():
    global val, recall, memory
    memory = val
    val = recall
    recall = memory
    
def undo_2():
    global prev_value, val, recall, memory
    memory = val
    val = prev_value
   # recall = memory
    
def mem():
    global memory, val
    memory = val
    pass
   
#*** how to make it remain as a different function
def rec():

    global memory, recall,val
    recall = memory
    val = recall
    pass
    
    
#Pocket calculators usually have a memory and a recall button. The memory button saves the current value
#and the recall button restores the saved value. Implement this functionality.
    
if __name__ == '__main__':
    global val, recall, memory
    val=0
    recall=0
    memory = 0
    prev_value=0
    print (" welcome to the calculator program. current value: 0 ")
    val = int(input("enter value: "))
    display_current_value()
    action= input("what opperation (+,x,/,exit)")
    while action!= "exit":
        if action == "+":
            add(int(input("what do you want to add? : ")))
        elif action == "x":
            mult(int(input("what do you want to divide? : ")))
        elif action == "/":
            div(int(input("what do you want to divide? : ")))
        elif action == "undo":
            undo()
        elif action == "mem":
            mem()
        elif action == "rec":
            rec()
        elif action == "undo2":
            undo_2()
            
        display_current_value()
        action = input("what opperation (+,x,/,undo,exit,mem,rec,undo2)")
    
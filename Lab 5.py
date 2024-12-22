''' Problem 1 '''
#Here is a function that computes the sum of a list of numbers.
def sum_nums(L):
    s = 0
    for num in L:
        s += num
    return s

#Write a function with the signature def count_evens(L) that returns the number of even integers in
#the list L. Assume L only contains integers.

def count_evens(L):
    even_nums = []
    for num in L:
        if L%2 == 0:
            even_nums.append(num)
        else:
            pass
    return(even_nums)

''' Problem 2 '''

#write a function list_to_str(lis) which returns the string representation of the list lis. You may assume
#lis only contains integers

def list_to_str(lis):
    new_str = ""
    for element in lis:
        new_str+= element
        new_str+= " "
        
    return new_str

''' Problem 3 '''

#Without using the == operator to compare lists (you can still compare individual elements of the lists),
#write a function lists_are_the_same(list1, list2) which returns True iff list1 and list2 contain
#the same elements in the same order. You’ll need to use a loop (either while or for)


def lists_are_the_same(list1, list2):
    for elm in range(1,(len(list1)+1)):
        if list1[elm] != list2[elm]:
            return False
        
    return True

''' Problem 4 '''

#Write a function with the signature list1_start_with_list2(list1, list2), which returns True iff
#list1 is at least as long as list2, and the first len(list2) elements of list1 are the same as list2.
#Note: len(lis) is the length of the list lis, i.e., the number of elements in lis.
#First write the function without using slicing (“slicing” means saying things like list1[2:5] we haven’t
#covered that), and using a loop.

def list1_start_with_list2(list1, list2):
    if len(list1)>=len(list2):
        return True
    else:
        return False
    
''' Problem 5 '''
#Write a function with the signature match_pattern(list1, list2) which returns True iff the pattern list2 appears in list1. In other words, we return True iff there is an i such that 0 ≤ i ≤


#For example, if list1 is [4, 10, 2, 3, 50, 100] and list2 is [2, 3, 50], match_pattern(list1, list2)
#returns True since the pattern [2, 3, 50] appears in list1


def match_pattern(list1, list2):
    first = int(list1.index(list2[0]))
    new_list1 = list1[first:len(list1)]
    
    for elm in range(0,len(list2)):
        if new_list1[elm] == list2[elm]:
            if elm == len(list2)-1:
                return True

            else:
                continue
        else:
            return False
        
    
''' Problem 6 '''
#Write a function with the signature duplicates(list0), which returns True iff list0 contains at least
#two adjacent elements with the same value.
#Hint: you need to compare list[i] and list[i+1] for all i.

def duplicates(list0):
    for elm in range(0,len(list0)):
        if list0[elm] == list0[elm+1]:
            return True
        else:
            continue
    return False


''' Problem 7 '''

#a

t= [0,1,2,3,4,5,6]
x= [0,1,2,3,4,5,6]
i= 2
i = x.index(i)

def inst(t,x,i):
    x_pos = x.index(i)
    t_pos = t.index(i)
    
    if x_pos == 0 or t_pos == 0:
        print("no")
    else:
        
        # v1
        time_betwn = t[t_pos + 1] - t[t_pos-1]
        
        v1 = x[x_pos+1] - x[x_pos-1] / time_betwn
        
        #v2
        time_betwn = t[t_pos + 2] - t[t_pos-2]
        
        v1 = (x[x_pos+2] - x[x_pos-2]) / time_betwn
        
        avg = (v2 - v1) / 2
        
        return avg
    
    
#b
def randomize_coords(x):
      
    for j in x:
        new_x+= j + 0.1*random.random(1,11)
        
    return new_x
        
    
                
                

    
            
        

            
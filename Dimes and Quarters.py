#Unlimited supply of 3 and 4 cent coins
#Determine largest possible amount of money that cannot be made (combonations)
# 7 - one 3 cent and one 4 cent
# 6 - two 3 cent

for n in range(1,11):
    count_3c = 0
    count_4c = 0

    # Calculate the maximum number of 4 cent coins that can be used (quotient) and remainder
    Quo4 = n // 4
    for i in range(Quo4+1):
        remaining = n - 4*i

        # If the remaining amount can be evenly divided by 3, use all 4 cent coins and
        # add one 3 cent coin for each multiple of 3
        if remaining % 3 == 0:
            count_4c = i
            count_3c = remaining // 3
            break

        # If the remaining amount cannot be evenly divided by 3, use some 4 cent coins and
        # the remaining amount can be covered by 3 cent coins
        else:
            count_4c = i
            count_3c = remaining // 3

    # Return the total number of coins required
    print("'",n,"'")
    if count_3c==0 and count_4c>0:
        print(count_4c, "fourcent coins")
    elif count_3c>0 and count_4c==0:
        print(count_3c,"threecent coins")
    elif count_3c==0 and count_4c==0:
        print ("not possible")
    else:
        print( count_3c,"threecent and ", count_4c, "fourcent coins")
       
   
    

        
        
        
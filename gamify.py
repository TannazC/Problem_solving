import sys
sys.version



#This function returns the number of hedons that the user has accumulated so far.
def get_cur_hedons():
    global hedons
    return hedons

#This function returns the number of health points that the user has accumulated so far
def get_cur_health():
    global health
    return health

#the user is tired if they finished running or carrying textbooks less than 2 hours
#before the current activity started      
def tired():
    global prev_activity, prev_duration, activity_log_long, activity_log
    if (prev_activity == "textbooks" or prev_activity == "running") and prev_duration<=120:
        return True
    for i in range(1,121):
        if i==120 or i>=len(activity_log_long):
            break
        if activity_log_long[-i] == "running" or activity_log_long[-i] == "textbooks":
            return True
    else:
        return False 
        
#The function simulates the user’s performing activity for duration minutes. Assume duration
#is a positive int. If activity is not one of "running", "textbooks", or "resting", running the function
#should have no effect.
    
def health_calc(activity,duration):
    global health
    global prev_activity, activity_log_long
    global prev_duration, calc_duration, running_duration,use_run_total
   
    if prev_activity == activity:
        running_duration = duration
        activity_log_long.reverse()
        prev_duration = 0
        for i in (activity_log_long):
        
            if i == activity:
                prev_duration+=1
            else:
                break
        
        if activity == "running":
           
        #health 
            if prev_duration<=180: 
                health -= (3*prev_duration) #3 health points per minute up to 180
            elif prev_duration>180:
                health -= (3*180)+(1*(prev_duration-180)) #1 health point per minute after 180

                                
        elif activity == "textbooks":
        #health
            health-= (2*prev_duration) #always gives 2 health points / min

        running_duration+=prev_duration
        use_run_total = True
        activity_log_long.reverse()
   
#fix  
    if use_run_total == True:
            
        if activity == "running":
        #health 
            if running_duration<=180: 
                health += (3*running_duration) #3 health points per minute up to 180
            elif running_duration>180:
                health += (3*180)+(1*(running_duration-180)) #1 health point per minute after 180
                       
        elif activity == "textbooks":
            health+= (2*running_duration) #always gives 2 health points / min
        use_run_total = False
        running_duration = 0
        
    else:
        if activity == "running":
        #health 
            if duration<=180: 
                health += (3*duration) #3 health points per minute up to 180
            elif duration>180:
                health += (3*180)+(1*(duration-180)) #1 health point per minute after 180
                       
        elif activity == "textbooks":
            health+= (2*duration) #always gives 2 health points / min
          
       
        
 
#--------------------------------------


            
def perform_activity(activity,duration):
    
    global health
    global hedons
    global prev_activity, activity_log_long, activity_log
    global prev_duration
    global offer, time
    
#running
    if activity == "running":

    #health
        health_calc(activity,duration)
    #hedons with star
        if offer== True and star_can_be_taken(activity)== True:
    
            if tired()==True:
                if duration<=10:
                    hedons+= (-2*duration)+(3*duration)
                else:
                    hedons+=(-2*duration)+(3*10)
            else:
                if duration<=10:
                    hedons+= (2*duration)+(3*duration) # up to 10
                else:
                    hedons+= (1*(duration-10))+(10*2)+(3*10) #after 10
            offer == False
    #hedons normal
        else:
            if tired()==True: 
                hedons+= (-2*duration)
            else:
                if duration<=10:
                    hedons+= (2*duration) # 2 hedon / min up to 10 min
                else:
                    hedons+= (-2*(duration-10))+(10*2) # -2 per min after 10
#textbooks   
    elif activity == "textbooks":
        
    #health
        health_calc(activity,duration)
    #hedons with star
        if offer== True and star_can_be_taken(activity)== True:
        
            if  tired()==True:
                if duration<=10:
                    hedons+= (-2*duration)+(3*duration)
                else:
                    hedons+=(-2*duration)+(3*10)
            else:
                if duration<=20:
                    if duration<10:
                        hedons+= (1*duration)+(3*duration)
                    else:
                        hedons+= (1*duration)+(3*10)
                else:
                    hedons+= (-1*(duration-20))+(20*1)+(3*10) #after 20
            offer = False
    # hedons normal
        else:
            if  tired()==True: 
                hedons+= (-2*duration) #-2 per min if tired and NOT using star
            else:
                if duration<=20: #if NOT tired 1 hedon/ min up to 20
                    hedons+= (1*duration)
                else:
                    hedons+= (-1*(duration-20))+(20*1) # -1 / min after 20
#resting   
    elif activity == "resting": #0 hedons per min, no health
        if offer== True and star_can_be_taken(activity)== True:
            if duration<10:
                hedons+=(duration*3)
            else:
                hedons+=(3*10)
        else:
            pass
    else:
        pass

#recording activities and duration for future use 
    prev_activity= activity
    prev_duration= duration
    time+=duration
    for i in range(1,duration+1):
        activity_log_long.append(activity)
    activity_log.append(activity)
    duration_log.append(duration)

#The function returns True if a star can be used to get more hedons for activity activity. A star can only
#be taken if no time passed between the star’s being offered and the activity, and the user is not bored with
#stars, and the star was offered for activity activity.
def star_can_be_taken(activity):
    #no time passed between offer and activity, not bored, and offer activity stands
    global offer_time,time, offer_activity, first_offer_time, stars
    if time - offer_time == 0 and bored() == False and activity == offer_activity:
        return True
    else:
        return False
    

#This function simulates a offering the user a star for engaging in the exercise activity.
#Assume activity is a string, one of "running", "textbooks", or "resting". this records variables to do so
def offer_star(activity):
    global offer_time,time, offer_activity, first_offer_time, offer, stars
    offer_time = time
    
    offer_activity = activity
    offer = True
    stars+=1
    if first_offer_time == "i":
        first_offer_time = offer_time

#this function checks if the user is bored by the amount of stars
# The user becomes bored once a third star is offered within the span of two hours
def bored():
    global stars, first_offer_time
    if ((offer_time-first_offer_time) < 120) and (stars>=3):
        return True
    else:
        return False

#This simulates preforming activities without changing variables for the purpose of most_fun_activity_minute()
def simulate_activity(activity,duration):
    sim_hedons = 0
    global prev_activity, activity_log_long, activity_log
    global prev_duration
    global offer
        
    
    # running
    if activity == "running":
        

        #sim_hedons with star
        if offer== True and star_can_be_taken(activity)== True:
    
            if tired()==True:
                if duration<=10:
                    sim_hedons+= (-2*duration)+(3*duration)
                else:
                    sim_hedons+=(-2*duration)+(3*10)
            else:
                if duration<=10:
                    sim_hedons+= (2*duration)+(3*duration) # up to 10
                else:
                    sim_hedons+= (1*(duration-10))+(10*2)+(3*10) #after 10

        #reg sim_hedons
        else:
            if tired()==True: 
                sim_hedons+= (-2*duration)
            else:
                if duration<=10:
                    sim_hedons+= (2*duration) # up to 10
                else:
                    sim_hedons+= (-2*(duration-10))+(10*2) #after 10
    #textbooks   
    elif activity == "textbooks":
        
        #sim_hedons with star
        if offer== True and star_can_be_taken(activity)== True:
        
            if  tired()==True:
                if duration<=10:
                    sim_hedons+= (-2*duration)+(3*duration)
                else:
                    sim_hedons+=(-2*duration)+(3*10)
            else:
                if duration<=20:
                    if duration<10:
                        sim_hedons+= (1*duration)+(3*duration)
                    else:
                        sim_hedons+= (1*duration)+(3*10)
                else:
                    sim_hedons+= (-1*(duration-20))+(20*1)+(3*10) #after 20

        # sim_hedons normal
        else:
            if  tired()==True: 
                sim_hedons+= (-2*duration)
            else:
                if duration<=20:
                    sim_hedons+= (1*duration) # up to 20
                else:
                    sim_hedons+= (-1*(duration-20))+(20*1) #after 20
    #resting   
    elif activity == "resting":
        if offer== True and star_can_be_taken(activity)== True:
            if duration<10:
                sim_hedons+=(duration*3)
            else:
                sim_hedons+=(3*10)
        else:
            pass
    else:
        pass
    
    return sim_hedons


#The function returns the activity (one of "resting", "running", or "textbooks") which would give the
#most hedons if the person performed it for one minute at the current time. This simulates preforming the activities
#without changing variables
def most_fun_activity_minute():
    array=[simulate_activity("running",1),simulate_activity("textbooks",1),simulate_activity("resting",1)]
    if array[0] > array[1] and array[0]> array[2]:
        return "running"
    elif array[1] > array[0] and array[1] > array[2]:
        return "textbook"
    else:
        return "resting"

#The function initialize all the global variables in the program.
#The following code should run two independent simulations, with both SIMULATION 1 and SIMULATION 2
#starting from the beginning.
def initialize():

    global hedons,use_run_total, running_duration, duration_log, health, stars , offer, activity, activity_log_long, activity_log, duration_log, prev_activity, prev_duration, time, offer_time, offer_activity, first_offer_time
    hedons=0
    health=0
    stars=0
    duration_log=[]
    use_run_total = False
    activity = "resting"
    prev_activity="i"
    prev_duration=0
    activity_log_long= []
    activity_log=[]
    time=0
    offer_time= 0
    first_offer_time ="i"
    offer = False
    calc_duration = 0
    running_duration = 0


if __name__ == '__main__':
    initialize()
    """
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 =  10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2
    print(get_cur_hedons()) # -80 =  -20 + 30 * (-2) 
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health()) # 210 =  150 + 20 * 3
    print(get_cur_hedons()) # -90 =  -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health()) # 700 =  210 + 160 * 3 + 10 * 1
    print(get_cur_hedons()) # -430 =  -90 + 170 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())  """
    
    initialize()
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    print(star_can_be_taken("textbooks"))
    perform_activity("textbooks", 1)
    print(get_cur_health())
    print(get_cur_hedons())
    
    

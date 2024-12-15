import random
import time

def get_addition(difficulty):
    a = random.randint(1, int(100 * difficulty ** 2))
    b = random.randint(1, int(100 * difficulty ** 2))
    return [a,"+",b,a+b]    

def get_substraction(difficulty):
    a = random.randint(1, int(100 * difficulty ** 2))
    b = random.randint(1, a)
    return [a,"-",b,a-b]

def get_multiplication(difficulty):
    a = random.randint(2, int(10 * difficulty))
    b = random.randint(2, int(10 * difficulty))
    return [a,"*",b,a*b]

def get_division(difficulty):
    b = random.randint(2, int(10 * difficulty))
    a = b*random.randint(2, int(10 * difficulty))
    return [a,"/",b,a//b]
    
def get_modulo(difficulty):
    b = random.randint(2, int(10 * difficulty))
    a = random.randint(b, int(100 * difficulty))  
    return [a,"%",b,a%b]

def play(start_difficulty, difficulty_increase, timer_start, timer_add, timer_penalty):
    print("Welcome to quickmaths. You will be presented simple math expressions for calculation by using mental arithmetic. The timer, starting at", timer_start, "seconds, counts continously, with", timer_add, "seconds being added after every correct answer given and", timer_penalty, "seconds being substracted after every incorrect answer given. The tasks are randomly generated and will generally get harder as you progress. Press Enter to start.")
    input()
    current_difficulty = start_difficulty
    timer = timer_start
    solved = 0
    lost = False
    while not lost:
        operation = random.randint(1,5)
        if operation == 1:
            task = get_addition(current_difficulty)
        if operation == 2:
            task = get_substraction(current_difficulty)
        if operation == 3:
            task = get_multiplication(current_difficulty)
        if operation == 4:
            task = get_division(current_difficulty)
        if operation == 5:
            task = get_modulo(current_difficulty)
            
        print(task[0], task[1], task[2])
        task_time = time.time()
        user_solution = input()
        solution_time = time.time()
        t = solution_time - task_time
        timer -= t
        if user_solution == str(task[3]):
            timer += timer_add
            print("Solved in ", int(t), " seconds. You have ", int(timer), " seconds left. ( +", timer_add, ")")
            solved += 1
            current_difficulty += difficulty_increase           
        else:
            timer -= timer_penalty
            print("Correct answer is ", task[3], ". You have ", int(timer), " seconds left. ( -", timer_penalty, ")")
        
        if timer <= 0:
            lost = True    
    print("Thank you. You solved ", solved, " tasks.")


play(1,0.1,180,5,5)
input()








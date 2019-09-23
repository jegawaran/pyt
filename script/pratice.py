#!/usr/bin/python3

def first():
    animal,vegetable,mineral = 'cat','broccoli','gold'
    print("Here is an {0} a {1} a {2}".format(animal,vegetable,mineral))
    print(animal)
    print(vegetable)
    print(mineral)

first()

def prompt():
    val = raw_input("Enter something to repeat: ")
    print("You entered : {}". format(str(val)))

prompt()


def num():
    hostCharge = 0.51
    day = hostCharge * 24
    month = day * 30
    print("Server cost for per day in $: " + str(day))
    print("Server cost for per month in $: " + str(month))

num()

def conditionif():
    miles=input("How far would you like to travel in miles?: ")
    if miles < 3:
        print("Better take a walk, {} miles are not so heavy".format(miles))
    elif miles > 3 and miles < 300:
        print("{} miles are huge i guess , Better take a car".format(miles))
    else:
        print("{} miles are very very very huge , you can't drive , better take a flight".format(miles))
conditionif()        
            
    
def todoList():
    todo_list =[]
    finished = False
    while not finished:
        task = raw_input("Enter a task for your todo list. Press <enter> Once done: ")
        if len(task) == 0:
            finished = True
        else:
            todo_list.append(task)
            print("TaSK aDDed")

    print()
    print("your todo list: ")
    print('-' * 16)
    print(todo_list)
    for task in todo_list:
        print(task)

todoList()
        

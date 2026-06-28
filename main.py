lt=[]
while True:
    print("1. Add Task")
    print("2.View already added tasks")
    print("3.Exit")
    input_value=input("Enter the number to carry out the task:")
    input_value=int(input_value)
    if(input_value==1):
        task=input("Enter the task")
        lt.append(task)
    elif(input_value==2):
        print("Added tasks are:")
        if(len(lt)==0):
            print("No tasks added yet")
        for index,task in enumerate(lt):
            print(index+1,task)
    elif(input_value==3):
        break
    else:
        print("Invalid value")
    

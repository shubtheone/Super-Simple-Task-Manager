print("~"*80)
print("Welcome to Task Manager")
print("~"*80)
j=1
tasks=[]



while True:
    choice=int(input("\n1.Add a new task\n2.Remove a task\n3.Print the task list\n4.Exit\n"))


    if(choice==1):
        newtask=input("Enter the task name\n")
        tasks.append(newtask)
        continue
    elif(choice==2):
        num=int(input("Enter the task index\n"))
        tasks.pop(num-1)
    elif(choice==3):
        print("~"*80)
        print("Current Task list consists of:\n")
        print("~"*80)
        for i in tasks:
            
            print(f"{j}. {i}")
            j+=1
        print("~"*80)
    elif(choice==4):
        break



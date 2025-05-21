
todo = []
#Loop Continue Untill We Want To Exit
while True:
    print("\n ToDo App Menu")
    print("1: Add Task")
    print("2: View Task")
    print("3: View Your Task Status")
    print("4: Change Task Status")
    print("5: Exit")

    choice = input("Enter Your Choice From (1 - 5) : ")

#Add Task 
    if choice == "1":

        total_task = int(input("How Many Task You Want To Enter : "))

        for task in range(total_task):
            task_id = task + 1 
            task_title = input(f"Please Enter Title of Task {task_id}: ")
            detail = input("Enter Detail Of Your Task: ")
            # automatically assign initial status to each task.
            todo.append({"Task_id":task_id,"Title":task_title,"Detail":detail, "Status":"initial"}) #direct append to list no need to assign it to any variable it takes more memory  
            
# View Task
    elif choice == "2":

        if not todo: #here not means Check the list is empty
            print("Lis Of Task Is Empty")
        else:
            all_task = input("Do You Want To Show All Task! Enter (Yes/no) : ")
            if all_task == "yes":
                for task in todo:
                    print(task)
            else:
                task_count = int(input("Enter Ammount How Many Task You Want To Show: "))
                for task in todo[:task_count]:
                    print(task)
        

#Show Status By Id Or Title or By Status

    elif choice == "3":
        print("1 : Show tatus By Id : ")
        print("2 : Show Status By title : ")
        show = input("Enter Your Choice To Show Status : ")
        if show == "1":
            view_status = int(input("Enter Task Id To View Task Status :"))
            for task in todo:
                task["Task_id"] = view_status
                print(f"The Status of Task [{task["Title"]}] is : {task["Status"]}")
        elif show == "2":
            title_name = input("Enter Title Name : ")
            for task in todo:
                task["Title"] = title_name
            print(f"The Status of Title [{task["Title"]}] is : {task["Status"]}" )
        else:
            print("Enter only 1 ane 2 for Choice")              


#Now we Change Status Of Task    
    
    elif choice == "4":
        change_status_id =int(input("Enter Id To Change Status : "))
        for task in todo:
            if task["Task_id"] == change_status_id:
                print(f"Status Of Current Id {task["Task_id"]} Is : {task["Status"]}") 
                convert_status = input(" In Which Status You Want To Change \n Continue \n Finished \n ")
                if convert_status == "continue":
                    task["Status"] = "Continue"
                    print(task)
                elif convert_status == "finished":
                    task["Status"] = "Finished"  
                    print(task)
                else:
                    print("Enter Correct Status ")                   

#Ends The Loop        
    elif choice =="5":
        print("Exit From ToDo App")
        break            
    else:
        print("Invalid Choice :\n Please Enter Choice From(1 - 5 )")
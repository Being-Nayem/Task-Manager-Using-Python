from datetime import datetime
from random import randint
 
all_task = []
 
 
class Task:
 
   def __init__(self, task):
       self.task = task
       self.created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
       self.update_time = "NA"
       self.completed_time = "NA"
       self.task_done = False
       self.id = f"{self.created_time.replace('/', '-').replace(':','-').replace(' ','-')}-{randint(1,1000)}-{randint(1000,2000)}"
 
   def update_task(self, task_no, task):
       all_task[task_no]["task_name"] = task
       all_task[task_no]["update_time"] = datetime.now().strftime(
           "%d/%m/%Y %H:%M:%S")
 
   def complete_task(self, task_no):
       all_task[task_no]["complete_status"] = True
       all_task[task_no]["completed_time"] = datetime.now().strftime(
           "%d/%m/%Y %H:%M:%S")
 
 
def create_task():
   print()
   task = input("Enter New Task: ")
   TASK = Task(task)
   task_info = {"id": TASK.id, "task_name": TASK.task, "create_time": TASK.created_time,
                "update_time": TASK.update_time, "complete_status": TASK.task_done, "completed_time": TASK.completed_time}
   all_task.append(task_info)
   print()
   print("Task Created successfully")
 
 
def show_all_task():
   if len(all_task) == 0:
       print()
       print("No Task Available")
   else:
       for task_no in all_task:
           print()
           print(f"ID: {task_no['id']}")
           print(f"Task: {task_no['task_name']}")
           print(f"Created Time: {task_no['create_time']}")
           print(f"Updated Time: {task_no['update_time']}")
           print(f"Completed: {task_no['complete_status']}")
           print(f"Completed Time: {task_no['completed_time']}")
 
 
def show_incomplete_task():
   cnt = 0
   for task_no in all_task:
       if task_no["complete_status"] == False:
           print()
           print(f"ID: {task_no['id']}")
           print(f"Task: {task_no['task_name']}")
           print(f"Created Time: {task_no['create_time']}")
           print(f"Updated Time: {task_no['update_time']}")
           print(f"Completed: {task_no['complete_status']}")
           print(f"Completed Time: {task_no['completed_time']}")
           cnt += 1
   if cnt == 0:
       print()
       print("No Incompleted Task")
 
 
def show_complete_task():
   cnt = 0
   for task_no in all_task:
       if task_no["complete_status"] == True:
           print()
           print(f"ID: {task_no['id']}")
           print(f"Task: {task_no['task_name']}")
           print(f"Created Time: {task_no['create_time']}")
           print(f"Updated Time: {task_no['update_time']}")
           print(f"Completed: {task_no['complete_status']}")
           print(f"Completed Time: {task_no['completed_time']}")
           cnt += 1
   if cnt == 0:
       print()
       print("No Completed Task")
 
 
def Update_Task():
   cnt = 0
   for task in all_task:
       if task["complete_status"] == False:
           cnt = 1
   if cnt == 0:
       print()
       print("No Task To Update")
   else:
       print()
       print("Select Which Task To Complete")
       for task_no in range(all_task.__len__()):
           if all_task[task_no]["complete_status"] != True:
               print()
               print(f"Task No - {task_no+1}")
               print(f"ID: {all_task[task_no]['id']}")
               print(f"Task: {all_task[task_no]['task_name']}")
               print(f"Created Time: {all_task[task_no]['create_time']}")
               print(f"Updated Time: {all_task[task_no]['update_time']}")
               print(f"Completed: {all_task[task_no]['complete_status']}")
               print(f"Completed Time: {all_task[task_no]['completed_time']}")
       print()
       task_NO = int(input("Enter Task No: "))
       task = input("Enter New Task: ")
       new_task = Task(task)
       new_task.update_task(task_NO-1, task)
       print()
       print("Task Updated successfully")
 
 
def Complete_Task():
   cnt = 0
   for task in all_task:
       if task["complete_status"] == False:
           cnt = 1
   if cnt == 0:
       print()
       print("No Task To Complete")
   else:
       print()
       print("Select Which Task To Complete")
       for task_no in range(all_task.__len__()):
           if all_task[task_no]["complete_status"] != True:
               print()
               print(f"Task No - {task_no+1}")
               print(f"ID: {all_task[task_no]['id']}")
               print(f"Task: {all_task[task_no]['task_name']}")
               print(f"Created Time: {all_task[task_no]['create_time']}")
               print(f"Updated Time: {all_task[task_no]['update_time']}")
               print(f"Completed: {all_task[task_no]['complete_status']}")
               print(f"Completed Time: {all_task[task_no]['completed_time']}")
       print()
       task_NO = int(input("Enter Task No: "))
       com_task = Task(all_task[task_no-1]["task_name"])
       com_task.complete_task(task_NO-1)
       print()
       print("Task Completed successfully")
 
 
while (True):
   print("1. Add New Task")
   print("2. Show All Task")
   print("3. Show Incomplete Tasks")
   print("4. Show Completed Tasks")
   print("5. Update Task")
   print("6. Mark A Task Completed")
   option = int(input("Enter Option: "))
   if option == 1:
       create_task()
 
   elif option == 2:
       show_all_task()
   elif option == 3:
       show_incomplete_task()
   elif option == 4:
       show_complete_task()
   elif option == 5:
       Update_Task()
   elif option == 6:
       Complete_Task()
   print()

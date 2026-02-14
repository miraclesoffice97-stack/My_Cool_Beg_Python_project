#creating a class for the projects functions 
class todolist:
  def __init__(self): #creating a constructor 
    self.task = []
    
  def add_task(self): # creating bkend for add task option 
    task = input ("Enter task to add: ").lower()
    self.task.append(task)
    for index, task in enumerate(self.task, start=1):
      print ("New task added")
      print (f"{index} : {task}")
    
  def show_currTasks(self): # creating bkend for current tasks option
    if not self.task:
      add_task_alt = input ("Empty 🫙 + to add a new task: ").lower()
      
      if add_task_alt == "+":
        print (self.add_task())
      else:
        print("invalid input!")
        
    else:
      for index, task in enumerate(self.task, start=1):
        print (f"{index} {task}")
        
  def complete_task(self): 
    if not self.task:
      print ("No existing tasks")
      
    else:
      for index, task in enumerate(self.task, start=1):
        print (f"{index} : {task}")
      
      try:
        options = int(input("Select an option: "))
        options -= 1
        removed_item = self.task.pop(options)
        print (f"{removed_item} removed successfully!")
        
      except:
        print ("invalid!")
    

toDo_txk = todolist()
while True:
  
  options_t = f'''{"_" * 30} \nChoose an Option: 
  \n1. Add Task. 
  \n2. See current tasks 
  \n3. Remove Task's 
  \n4. Exit''' 
  print (options_t)
  
  selected_option = input("select an option: ")
  
  if selected_option == "1":
    toDo_txk.add_task()
    
  elif selected_option == "2":
    toDo_txk.show_currTasks()
  
  elif selected_option == "3":
    toDo_txk.complete_task()
    
  elif selected_option == "4":
    print ("good bye 👻")
    break
  
  else:
    print ("invalid! selection.")
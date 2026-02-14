#grade calculator project.

def grade(grade_cal):
  
    if grade_cal <= 50:
      return f"{grade_cal} --- D7 --- poor x!"
    
    elif grade_cal <= 60:
      return f"{grade_cal} --- C6 --- fair 🔆"
  
    elif grade_cal <= 70:
      return f"{grade_cal} --- C5 --- Good 👍"
    
    elif grade_cal <= 80:
      return f"{grade_cal} --- B2 --- great 😎"
  
    elif grade_cal <= 100:
      return f"{grade_cal} --- A1 --- Excellent🥳"
      
    else:
      return f"{grade_cal} exceeded score type"
      
    
while True:
  try:
    listed_values = [int(input ("Enter the Exam score: ")), 
    int(input("Enter the test Score: ")), 
    int(input("Enter the note score: "))]
    
    
    grader = sum(listed_values) / 3
    grade_score = grade(grader)
    
    if grade_score: 
      print(grade_score)
     
   
  except ValueError:
    print ("invalid input!")
    
  user_input = input("enyer x to quit: ")
  if user_input.lower() == "x":
      print ("program ended!")
      break
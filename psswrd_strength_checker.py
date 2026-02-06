
class password_strengthChecker:
    def __init__(self, password):
        self.password = password
      
    def pass_conditions(self):
        self.pwd = self.password
        self.password_req = [len(self.pwd) >= 8, #check password > 8
        any (char.isdigit() for char in self.pwd), #check number in password 
        any (char.upper() for char in self.pwd), #upper case in password 
           ]
           
          if all(self.password_req):
            print ("successfully created password Strong!!😡")
            return True
          else:
            print ("weak!! password 🔑 check password requirements")
            return False
    
password_req_line = "User Password Requirements: \n must be 8 letters or greater \n must include an upper case\n must include digits \n must include special characters #@=₦*"

while True:
  print (password_req_line)
  user_input = input("Enter a strong! password: ")
  
  pswrd_checker = password_strengthChecker(user_input)
  if pswrd_checker.pass_conditions():
    break
  else:
    continue 

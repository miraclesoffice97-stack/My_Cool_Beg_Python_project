
# __The ultimate Book Library 😎
class book_library_proj:
  def __init__(self):
    self.books = []
  
  def add_book (self):
    book_name = input("enter the name of the book: ")
    self.new_book = {"book": book_name}
    self.books.append(self.new_book)
    print(f"{self.new_book} added to library successfully!")
  
  def open_library (self): # open library function.
    
    print (self.books)
    
    if not self.books:
      print ("No current book in the library! ")
      option = input("no current books enter + to add a new book: ").lower()
      
      if option == "+":
         print (self.add_book())
      else:
         print ("invalid input!")
         
    for index, self.new_book in enumerate(self.books, start=1):
        print (f"{index} {self.new_book}")
        
    try:
      select_from_options = int(input("select an option from the numbers: "))
      select_from_options -= 1
      return self.new_book
    except:
      return "invalid selection! please choose from the above listed selections"
      
  def search_book(self):
    
      user_search = input("enter a book name to search: ").lower()
      for index, self.new_books in enumerate(self.books, start=1):
        if user_search  in self.new_books.values():
          print(f"{index} {self.new_book.values()}")
          
          try:
            select_from_options = int(input("select an option from the numbers: "))
            select_from_option -= 1
            print (self.new_book)
            
          except:
            print ("invalid selection! please choose from the above listed selections")
            
        else:
          print("No suggestions!")
    
  def delete_books(self):
      if not self.books:
        print ("Empty Library add book!!!📚📚➕")
      
      else:
        for index, self.new_book in enumerate(self.books, start=1):
          
           print (f"{index} {self.
           new_book}")
           
        try:
          select_from_options = int(input("select an option to delete: "))
          deleted_item = self.books.pop(select_from_options - 1)
          print(f"{deleted_item['book']} deleted successfully!")
          
        except:
          print ("invalid selection! please choose from the above listed selections: ")
        
book_store = book_library_proj()

while True:
  option_list = f'''{"-" * 40} \n         DC book store... \n{"-" * 40} \n1. Add a New book 
  \n2. View available books in library 
  \n3. Search up available books in library 
  \n4. Delete books from library 
  \n5. Exit program'''
  print(option_list)
  user_choice = input ("Choose an option: ")
  
  if user_choice == "1":
    print (f"{'-' * 40} \n Add a New Book to your Library 📚 \n{'-' * 40}")
    book_store.add_book()
    
  elif user_choice == "2":
     print (f"{'-' * 40} \n Veiw available books in library\n{'-' * 40}")
     book_store.open_library()
     
  elif user_choice == "3":
     print (f"{'-' * 40} \n Search up available books in library \n{'-' * 40}")
     book_store.search_book()
     
  elif user_choice == "4":
     print (f"{'-' * 40} \n Delete books from library \n{'-' * 40}")
     book_store.delete_books()
     
  elif user_choice == "5":
    print ("Good bye 👻")
    break
  else:
    print ("Invalid input!!!")
    continue
  ##$$DC DOC..................

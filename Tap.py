import random

def is_correct(computer, player):
  if computer == player:
    return True
  
  else:
    return False
    
    
sentence = '''python JavaScript java programming languages excellent condition typescript meatball noodles'''
print (sentence )
sent_words = sentence.split()

comp_chc = random.choice(sent_words)
hint = comp_chc[-2:]

lives = 3
while lives > 0:
  plyr_chc = input (f"choose a word from the sentence {hint}: ")
  #print(plyr_chc)
  
  if is_correct(comp_chc, plyr_chc):
   print ("you won baller")
   break
 
  else:
    lives -= 1
    if lives > 0:
      print ("wrong guess try again ")
      
    else:
      print (f"wrong guess! word is {comp_chc} ") 


import random
print("           *** Welcome to my game 'Lion or Twenty' ***")

mode1=random.randint(0,10)
mode2=random.random()

print("""There is two mode for playing :
1)-random.randint()
2)-random.random()""")
choose1=int(input("-Choose one of the mode '1 or 2' :"))
if choose1==1:
  if mode1<=5:
    computer='Twenty'
  else:
    computer='Lion'

elif choose1==2:
  if mode2<0.5:
    computer='Twenty'
  else:
    computer='Lion'

else:
  print("Please ,respect the game rules.")
  exit()  
choose2=input("-You choose 'Lion' or 'Twenty':\n").capitalize()
if choose2==computer:
  print(" Great ,you win.")


elif choose2 not in ["Twenty" , "Lion"]:
  print(" Your choice is false.")


else :
  print(f" You lost.\n The computer choice :'{computer}'")






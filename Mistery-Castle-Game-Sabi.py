print('''
*******************************************************************************


          <|
           A             
          /.\       
     <|  [""M#      
      A   | #             
     /.\ [""M#             
    [""M# | #  U"U#U                 
     | #  | #  \ .:/    
     | #  | #___| #     
     | "--'     .-"     
   |"-"-"-"-"-#-#-##    
   |     # ## ######     
    \       .::::'/     
     \      ::::'/      
   :8a|    # # ##      
   ::88a      ###       
  ::::888a  8a ##::.    
  ::::::888a88a[]::::
 :::::::::SUNDOGa8a::::. ..              
 :::::8::::888:Y8888:::::::::...      
::':::88::::888::Y88a______________________________________________________
:: ::::88a::::88a:Y88a                                  __---__-- __
' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
  :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
.::  :::::::::::::::::::Y88as88a...s88aa.
*******************************************************************************
''')
print("Welcome to ★ Mistery Castle ★. ")
print("Your mission is to find the exit.")

choice1 = input('You wake up out of nowhere and find yourself in the middle of a giant and weird Castle. It is very dark and the room you are in is made of stones that cannot be moved. You adjust your eyes and see two doors next to you. A blue one and a purple one.  Which door do you choose? Type "blue" or "purple" \n').lower()
if choice1 == "blue":
  choice2 = input('You\'ve passed the door and there is a room with a pool in front of you. You can see that there are another 3 doors crossing the pool. You can swim or you can try crossing the pool using an old bridge you see. Which one do you choose? Type "swim" to swim across. Type "bridge" to use the bridge. \n').lower()
  if choice2 == "bridge":
    choice3 = input("You arrive at the other side unharmed. You are now face to face with the 3 doors and realizes that each door has a symbol. The first door has an eye, the second one has a snake and the third one has a star. Which symbol do you choose? \n").lower()
    if choice3 == "eye":
      print("It's a room full of creatures you don't recognize, but they certainly want to eat you. Game Over. Better luck next time.")
    elif choice3 == "snake":
      print("You found the exit! The grass is green and the sky is blue! You Win! Congratulations! But be more careful next time.")
    elif choice3 == "star":
      print("You got eaten by a huge octopus. Game Over. Better luck next time.")
  else:
    print("You got attacked by sharks. Game Over. Better luck next time.")
else:
  print("You entered and the door closed behind you and cannot be open. You are lost in a labyrinth forever. Game Over. Better luck next time. ")

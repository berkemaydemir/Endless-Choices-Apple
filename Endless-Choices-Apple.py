print('''

        /)
   .-"".L,""-.
  ;       :.  :
  (       7:  )
   :         ;
    "..-"-.."    
''')
luck=0
print("Endless Choices Alpha test 0.0000000000 ")
print('"Welcome Human"')
print('"So you are hungry.I dont have any food with me but if you follow this road you will see one apple tree. There are enough apples on that tree to fill your stomach."')
first_select=input("You are moving in the direction you said. After a while, following the path in the forest, the road splits into two. Will you go right or left?\n")
first_select_lower=first_select.lower()
if first_select_lower=="left":
  print("After walking through the forest for a while, a snake bites you and you die by poisoning. Game over.")
  
elif first_select_lower=="right":
  crow=input("Before you come out of the forest, you see a baby crow that has fallen to the ground. The crow's nest is the tree next to you. Will you put the baby crow in its nest? Yes or No\n")
  crow_lower=crow.lower()
  if crow_lower=="yes":
    luck +=1
  elif crow_lower=="no":
    luck=luck
  
  mountain=input("After you deal with the crow, you continue walking. After a short while you come out of the forest. When you come out of the forest, you see the huge apple tree. You like it, but you also find it strange because it's your first time seeing an apple tree. There's a problem though. You lifted your head too much. As you slowly lower your head, you realize that the huge apple tree is on top of a mountain. Will you climb this mountain or wait for a miracle? Climb or Wait\n")
  mountain_lower=mountain.lower()
  if mountain_lower == "climb":
    print("You think how you ever thought of climbing a mountain. It was really ridiculous. How many mountains have you climbed in your life? Now you can't go back, and after a while you either starve or fall to death.")
  elif mountain_lower == "wait" and luck ==0 :
    print("Really? Did you do a thing or two about life and immediately started expecting miracles? You are a funny man, but waiting for a miracle when you are hungry was your last joke.")
  elif  mountain_lower == "wait" and luck==1 : 
    branch=input("A shadow has passed over your head, and for a moment it may indeed have been night. Yes, waiting for a miracle can sometimes work, but sometimes. This is one of those times. A giant crow comes by and thanks you for saving your child. He asks you what you're doing here and you tell him. He offers to drop you off near the tree. You accept this offer. He drops you near the tree and leaves. When you go a little further, you reach the bottom of the tree. I wish the crow hadn't gone, you can't grow apples so high. When he turned around, he was already gone. You see three branches to climb the tree.The first branch is very thin and has many apples at the tip of the branch. These apples are enough for you for a few days.The second branch is a little high, but it stands very solid and has ivy around it. There are enough apples at the end of the branch to fill your stomach and even take a few with you.The third branch is a bit risky to be at the top, but you believe you can do it. There are enough apples on the branch to fill your stomach.Which branch do you choose to climb? First, Second or Third ")
    branch_lower=branch.lower()
    if branch_lower=="first":
      print("Did you really pick the first branch? I wonder what you thought when making this choice? Is it because of your greed or because you believe that thin branch cannot be broken? Unfortunately I will not be able to know the answer. The branch breaks when you step on it and your head is shattered.")
    elif branch_lower=="second":
      print("So you choose the second branch. Yeah, maybe that was the best option, but ivy can be poisonous, haven't you thought about that? Fortunately, ivy is not poisonous. Because when you get on the branch, you realize that it wasn't a ivy, it was a snake. There are so many snakes around here for some reason. While you are on the branch, the snake snarls around you and starts to strangle you. You choke to death before you can take a bite of the apple.")
    elif branch_lower=="third":
      print("You climb the branch with the apple. You take a bite of the apple. There is no problem, it tastes very good. I forgot to say something. I'm sorry, but you should have guessed that too. Does this story sound familiar to you? These apples were all banned, but look on the bright side, at least you tasted it. Suddenly you feel your body rise and your eyes close. When you wake up you are in a desert and there are only grains of sand around you. What do you plan to do in an unfamiliar place? THANKS FOR PLAYING Endless Choices Alpha test 0.0000000000 VERSION. TO BE CONTINUED...or continues")
    
    
    


  



import ran
def gameWin(you):
	if comp == you:
		return None
	elif comp =='s':
		if you =='p':
			return True
		elif you =='ss':
			return False
	elif comp =='p':
		if you =='s':
			return False
		elif you =='ss':
			return True
	elif comp =='ss':
		if you =='p':
			return False
		elif you =='s':
			return True
print ("Computer's turn: Stone (s), Paper (p) or Scissors (ss)")
rn = random.randint(1,3)
if rn ==1:
	comp='s'
elif rn == 2:
	comp='p'
elif rn == 3:
	comp='ss'
you = input("Your turn: Stone (s), Paper (p) or Scissors (ss)\n")
if you != 's' or you !='p' or you !='ss':
	print ("Invalid input")
	you = input("Your turn: Stone (s), Paper (p) or Scissors (ss)\n")
else:
	pass
a = gameWin(comp, you)
print ("Computer chose ")
print ("You chose ")
if a == None:
	print ("Game is tie!")
elif a:
	print ("You won!")
else:
	print ("You")
	

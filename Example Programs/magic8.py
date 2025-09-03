#magic 8 ball in python
import random
question = input('Question:   ')
random_number=random.randint(1,9)
if random_number==1:
  print('Yes - definitely.')
elif random_number==2:
  print('It is decidedly so.')
elif random_number==3:
  print('Without a doubt.')
elif random_number==4:
  print('Reply hazy, try again.')
elif random_number==5:
  print('Ask again later.')
elif random_number==6:
  print('Better not tell you now.')
elif random_number==7:
  print('My sources say no.')
elif random_number==8:
  print('Outlook not so good.')
else:
  print('Very doubtful.')
  


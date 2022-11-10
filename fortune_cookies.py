import random

lucky_num = random.randint(1,100)

fortune_num = random.randint(1,3)
fortune_text = ''

if fortune_num == 1:
    fortune_text = 'You will have a great day!'
elif fortune_num == 2:
    fortune_text = 'Today will be tough... but worth it!'
elif fortune_num == 3:
    fortune_text = 'You will get married this year :)'

print(f"""{fortune_text}
Your lucky number is: {lucky_num}""")

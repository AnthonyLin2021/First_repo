
import random 

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
  results = random.choices(symbols,k=3)

  print(f'{results[0]} | {results[1]} | {results[2]} |')

  if results == results[1] == results[2] == '7️⃣':
    print('Jackpot! 💰')
  else:
    print('Thanks for playing!')

new_round = True
while new_round == True:
  play()
  keep_playing = input ('Do you want to keep playing? enter \'Y\' or \'N\' ')
  if keep_playing == 'Y':
    new_round = True
  else: 
    new_round = False
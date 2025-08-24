

class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry=entry
    self.name=name
    self.types=types
    self.description=description
    self.is_caught=is_caught

  def speak(self):
    print(f'{self.name} {self.name}')

  def display_details(self):
    print(f'Entry Number: {self.entry}')
    print(f'Name: {self.name}')
    print(f'Type: {self.types}')
    print(f'Description: {self.description}')
    if self.is_caught==True:
      print(f'{self.name} has already been caught!')
    else:
      print(f'{self.name} has not been caught!')

Bulbasaur = Pokemon(1,'Bulbasaur',['Grass','Poison'],'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.',True)
Ninetales = Pokemon(38,'Ninetales',['Fire'],'Some legends claim that each of its nine tails has its own unique type of special mystical power.',False)
Ponyta = Pokemon(77,'Ponyta',['Fire'],'About an hour after birth, Ponyta’s fiery mane and tail grow out, giving the Pokémon an impressive appearance.',True)

Bulbasaur.speak()
Bulbasaur.display_details()
Ninetales.speak()
Ninetales.display_details()
Ponyta.speak()
Ponyta.display_details()
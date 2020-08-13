import pyinputplus as pyip

choiceOfBread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
choiceOfProtein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
cheeseOrNot = pyip.inputYesNo(prompt='Would you like cheese?')

# If the user wants cheese on their sandwich
if cheeseOrNot == 'yes':
    choiceOfCheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
else:
    choiceOfCheese = 'no'

variousCondiments = pyip.inputYesNo(prompt='Would you like mayo, mustard, lettuce, or tomato?')
# If the user wants condiments
if variousCondiments == 'yes':
    choiceOfCondiments = input('Which condiments would you like? ')
else:
    choiceOfCondiments = 'no'

numberOfSandwiches = pyip.inputInt(prompt='How many sandwiches would you like?', min=1)

if numberOfSandwiches == 1:
    print(f'You would like {numberOfSandwiches} {choiceOfProtein} sandwich on {choiceOfBread} bread with {choiceOfCheese} cheese, and {choiceOfCondiments}.')
else:
    print(f'You would like {numberOfSandwiches} {choiceOfProtein} sandwiches on {choiceOfBread} bread with {choiceOfCheese} cheese, and {choiceOfCondiments}.')

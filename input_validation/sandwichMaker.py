import pyinputplus as pyip

# TODO: Ask the user if they want mayo, mustard, lettuce, or tomato

# TODO: Ask how many sandwiches they want. Make sure the number is one or more

choiceOfBread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
choiceOfProtein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
cheeseOrNot = pyip.inputYesNo(prompt='Would you like cheese?')

# If the user wants cheese on their sandwich
if cheeseOrNot == 'yes':
    choiceOfCheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
else:
    choiceOfCheese = 'no'

print(f'You would like a {choiceOfProtein} sandwich on {choiceOfBread} bread with {choiceOfCheese} cheese.')

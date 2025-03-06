import pyinputplus as pyip
bread_cost = {
		'wheat': 10,
		'white': 8,
		'sourdough': 7}
protein_cost = {'chicken': 2.0, 'turkey': 2.5, 'ham': 2.2, 'tofu': 1.8}
cheese_cost = {'cheddar': 1.0, 'Swiss': 1.2, 'mozzarella': 1.1}
topping_cost = {'mayo': 1,'mustard':1,'lettuce':1,'tomato':1}

cost = []
selecting =[]

#select bread
bread_choice = pyip.inputMenu(['wheat','white','sourdough'],prompt='Please select bread: \n', numbered=True)
cost.append(bread_cost[bread_choice])
selecting.append(f'Bread: {bread_choice}')

# Select protein
protein_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Please select protein: \n', numbered=True)
cost.append(protein_cost[protein_choice])
selecting.append(f'Protein: {protein_choice}')

# Ask if they want cheese
wants_cheese = pyip.inputYesNo('Would you like cheese? (yes/no)\n')

if wants_cheese == 'yes':
    cheese_choice = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='Please select cheese: \n', numbered=True)
    cost.append(cheese_cost[cheese_choice])
    selecting.append(f'Cheese: {cheese_choice}')

wants_toppings = pyip.inputYesNo('Would you like mayo, mustard, lettuce, or tomato? (yes/no)\n')

if wants_toppings=='yes':
	topping_choice = pyip.inputMenu(['mayo','mustard','lettuce','tomato'],prompt="Which topping do you want?",numbered=True)
	choice.append(topping_cost[topping_choice])
	selecting.append(f'Topping: {topping_choice}')

sandwich_number = pyip.inputInt('How many sandwich do you want?\n')
selecting.append(f'Sandwich: {sandwich_number}')

print('Your order: ')
for i in selecting:
	print(i)
print(f' Total cost: {sum(cost)*sandwich_number}')


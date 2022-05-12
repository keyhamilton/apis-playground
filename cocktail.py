file = open('drink.txt')

lined = ''


for line in file.readlines():
    if line.startswith('{'):
        lined += line
if lined == '{"drinks":null}':
    print("Não temos um drink")
else:
    print("\nTemos um drink\n")
    drink_index = lined.index('strDrink')
    end_drink = lined.index(',', drink_index)
    print("%s\n" % lined[drink_index+3:end_drink])
    how_to_index = lined.index('Instructions')
    end_how_to = lined.index('InstructionsES')
    print("%s\n" % lined[how_to_index:end_how_to-4])

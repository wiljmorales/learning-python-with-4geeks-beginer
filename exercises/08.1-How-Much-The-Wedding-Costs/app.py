user_input = input('How many people are coming to your wedding?\n')
parced_input = int(user_input)

if parced_input <= 50:
    price = 4000
elif parced_input <= 100:
    price = 10000
elif parced_input <= 200: 
    price = 15000
else:
    price = 20000

print('Your wedding will cost '+str(price)+' dollars')

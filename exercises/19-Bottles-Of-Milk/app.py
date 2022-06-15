def number_of_bottles():
  for i in range(99):
    if i < 98:
      print(f"{99 - i} bottles of milk on the wall, {99 - i} bottles of milk. Take one down and pass it around, {98 - i} bottles of milk on the wall.")
    else:
      print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
      print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()


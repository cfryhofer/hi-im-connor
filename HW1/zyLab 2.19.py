#Connor Fryhofer 1853826
lemon_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings_cups = float(input("How many servings does this make?\n"))
print("\nLemonade ingredients - yields {:.2f} servings".format(servings_cups))
print("{:.2f} cup(s) lemon juice".format(lemon_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar".format(nectar_cups))

required_servings = float(input("\nHow many servings would you like to make?\n"))

print("\nLemonade ingredients - yields {:.2f} servings".format(required_servings))
print("{:.2f} cup(s) lemon juice".format(lemon_cups*required_servings/servings_cups))
print("{:.2f} cup(s) water".format(water_cups*required_servings/servings_cups))
print("{:.2f} cup(s) agave nectar".format(nectar_cups*required_servings/servings_cups))

print("\nLemonade ingredients - yields {:.2f} servings".format(required_servings))
print("{:.2f} gallon(s) lemon juice".format(lemon_cups*required_servings/servings_cups/16))
print("{:.2f} gallon(s) water".format(water_cups*required_servings/servings_cups/16))
print("{:.2f} gallon(s) agave nectar".format(nectar_cups*required_servings/servings_cups/16))

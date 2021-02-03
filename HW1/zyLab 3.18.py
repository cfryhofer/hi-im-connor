#Connor Fryhofer 1853826
wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
area = wall_width*wall_height
print("Wall area: " + str(area) + " square feet")
gallon_paint = 350
paint_need = area/gallon_paint
print("Paint needed: {0:.2f} gallons".format(paint_need))
cans_need = round(paint_need)
print("Cans needed: " + str(cans_need) + " can(s)")
paintColors = {"red": 35, "blue":25, "green": 23}
color = input("\nChoose a color to paint the wall:\n")
print("Cost of purchasing " + color + " paint: $" + str(cans_need*paintColors[color]))







#Q6...Country times...

newHours = 0
newMinutes = 0

name = str(input("Enter Name of the Country: "))
italyHours = int(input("Enter Time - in Italy (Hours): "))
italyMinutes = int(input("Enter Time - in Italy (Minutes): "))

if name == "Mexico":
    newHours = italyHours - 7
    newMinutes = italyMinutes + 0
elif name == "India":
    newHours = italyHours + 4
    newMinutes = italyMinutes + 30
elif name == "New Zealand":
    newHours = italyHours + 11
    newMinutes = italyMinutes + 0
else:
    print("NAME INVALID")




newHours = 24 + newHours
while newMinutes >= 60:
    newMinutes = newMinutes - 60
    newHours = newHours + 1
while newHours > 24:
    newHours = newHours - 24

print("It is ", newHours,":",newMinutes, "in", name)

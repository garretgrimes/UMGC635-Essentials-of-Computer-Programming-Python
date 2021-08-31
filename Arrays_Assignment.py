# Ask for user input

name = ["",""]
print("Weight Loss Challenge Tracker")
name[0] = input("Enter the name of the first member?: ")
name[1] = input("Enter the name of the second member?: ")

weight = ["","","","","","","","","",""]

weight[0] = eval(input("How many pounds did " + name[0] + " lose in January?: "))
weight[1] = eval(input("How many pounds did " + name[1] + " lose in January?: "))

weight[2] = eval(input("How many pounds did " + name[0] + " lose in February?: "))
weight[3] = eval(input("How many pounds did " + name[1] + " lose in February?: "))

weight[4] = eval(input("How many pounds did " + name[0] + " lose in March?: "))
weight[5] = eval(input("How many pounds did " + name[1] + " lose in March?: "))

weight[6] = eval(input("How many pounds did " + name[0] + " lose in April?: "))
weight[7] = eval(input("How many pounds did " + name[1] + " lose in April?: "))

weight[8] = eval(input("How many pounds did " + name[0] + " lose in May?: "))
weight[9] = eval(input("How many pounds did " + name[1] + " lose in May?: "))

finalweight1 = weight[0] + weight[2] + weight[4] + weight[6] + weight[8]
finalweight2 = weight[1] + weight[3] + weight[5] + weight[7] + weight[9]

print(name[0]," lost a total of " ,finalweight1, " pounds over 5 months.")
print(name[1]," lost a total of " ,finalweight2, " pounds over 5 months.")





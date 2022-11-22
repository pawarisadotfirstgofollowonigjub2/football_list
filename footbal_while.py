football_team = []
repeat = "Y"
while repeat == "Y"
    name = input("Enter yhe player's name:")
    football_team.append(name)
    repeat = input("Do you want to enter another name(Y/N): ")
print(football_team)
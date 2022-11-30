football_team = []

for i in range(11):
    name = input("Add a player in the football team:")
    football_team.append(name)
print(football_team)

repeat = "Y"
while repeat == 'Y':
    edit = int(input("Which pllayer do you want to change?:"))
    football_team[edit-1] = input("Enter a new player: ")

    delete = int(input("which player do you want to delete"))
    del football_team[delete-1]

    repeat = input("Do you want to edit more?(Y/N)")
    print(football_team)
  

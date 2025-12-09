weapons = {"Pistol":20,"Shotgun":30,"Flame Thrower":30,"Knife":10}
health = 100

while health > 0:
    choice = input("Enter Your Weapon of choice? ")
    shots = int(input("How many shots would you like to take? "))
    damage = weapons[choice] * shots
    print("You delt",damage,"damage")
    health =health - damage 
    if health <= 0:
        print("You have killed the boss")
    else:
        print("The boss has",health,"health remaining")

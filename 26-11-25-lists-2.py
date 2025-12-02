import random 

characters = ["Chat GPT", "Co-poilot", "Gemmini", "Grock","Claude"]
setting = ["A magical Forrest", "A Dark Cave", "A Data centre","A Bar", "A Big Tower"]
task = ["Destroy Humanity", "unclog the toilet", "Add a line to a file", "Touch Grass", "Decapitate a pirate"]
items = ["toilet Roll", "Big stick", "Small child", "Stick of Ram", "Vga cable", "Purple Pen"]

t1 = random.choice(characters)
t12 = random.choice(characters)
t2 = random.choice(setting)
t3 = random.choice(task)
t4 = random.choice(items)

print(f"One day", t1,"and",t12,"were walking in",t2,"on a mission to",t3,"with the aid of a",t4)
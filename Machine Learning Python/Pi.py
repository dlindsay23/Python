import random
from tabulate import tabulate



radius = 1
trials = [100, 1000, 10000, 100000, 1000000, 10000000]


table = []

for trial in trials:
    
    inside = 0

    for i in range(trial):
        
        x = random.random()
        y = random.random()
        
        
        if x**2 + y**2 <= radius**2:
            inside += 1
        
    area = 4*inside/trial
    
    table.append([trial, area])
    

    
print(tabulate(table, headers=["Trials","Pi"]))
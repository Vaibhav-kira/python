def series(n):
    x = 0
    while x<n:
        print(x)
        x += 1 
series(3)
x = 10 
x //=3
# break continue
y = 1
while y<6:
    if y%2 == 0:
        y += 1
        continue
    if y%5 == 0:
        break
    print(y)
    y +=1
print("for")
for i in range(4):
    print(i)
print("moderated for")
for i in range(1,10):
    print(i)
print("new change")
for i in range(1,10,2): ## only interger 
    print(i)
print("nested loops")
for i in range(5):
    for j in range(i,5):
        print(str(i)+"|"+str(j),end="   ")
    print()
print("teams pairing")
teams = ["India","England","Bangladesh","New Zealand"]
for home_team in teams:
    for away_team in teams:
        if home_team == away_team:
            continue
        print(home_team+"(home)"+" vs "+away_team+"(away)")
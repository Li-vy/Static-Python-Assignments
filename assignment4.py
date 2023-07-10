# Demonstrate the use of loop manipulation statements.
# (break, pass, continue, for with else and while with else)

for i in range(1,12):
    if i == 2:
        pass
    elif i == 4:
        continue
    elif i == 11:
        break
    print(i)
else:
    print("In else block")

print()
n = int()

while n <= 12:
    if n == 2:
        n+=1
        pass
    elif n == 4:
        n+=1
        continue
    elif n == 11:
        n+=1
        break
    print(n)
    n+=1
else:
    print("In else block")

#sorry ma'am for today 🙂
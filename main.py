
strin = input("Enter your word here")
letter = input("Enter the alphabet you want to find in that word")

i = 0
sum = 0

for i in strin:
    if i == letter:
        sum = sum+1

print(sum)
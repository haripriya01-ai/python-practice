sentence="coding in python is fun"
vowels=['a','e','i','o','u']
sum=0
for char in sentence.lower():
    if(char in vowels):
        sum+=1
print(f"there are {sum} vowels in sentence")
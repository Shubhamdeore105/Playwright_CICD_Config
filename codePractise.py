text=input("Enter the text = ")

duplicates=[]

for char in text:
    if text.count(char) > 1 and char not in duplicates:
        duplicates.append(char)
print("duplicate char is = ",duplicates)
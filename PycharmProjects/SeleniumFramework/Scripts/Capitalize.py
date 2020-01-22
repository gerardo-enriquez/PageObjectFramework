string = 'chris alan'
string = string.split(" ")
for i in range(0,len(string)):
    string[i] = string[i].capitalize()
string = " ".join(string)

print(string)
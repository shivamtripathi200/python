# find the first non repetetive character
inp_str = "teeter"
for char in inp_str:
    if inp_str.count(char) == 1:
        print("Char is : ",char)
        break
row1=["0","0","0"]
row2=["0","0","0"]
row3=["0","0","0"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put treasure? ")
col = int(position[0])-1
row = int(position[1])-1

selected_row = map[row]
selected_row[col] = "*"
print(map)
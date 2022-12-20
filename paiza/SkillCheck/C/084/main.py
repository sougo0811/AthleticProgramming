S = input()
S_list = list(S)
S_list.insert(0,"+")
S_list.insert(110,"+")
frame = []
for i in range(len(S_list)):
    frame.append("+")
frame = "".join(frame)
S_list = "".join(S_list)
print(frame)
print(S_list)
print(frame)
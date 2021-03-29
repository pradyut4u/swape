src = input("Enter file scource")
des = input("Enter file destination")
with open(src, 'r') as a:
    data_a = a.read()
with open(des, 'r') as b:
    data_b = b.read()
with open(src, 'w') as a:
    a.write(data_b)
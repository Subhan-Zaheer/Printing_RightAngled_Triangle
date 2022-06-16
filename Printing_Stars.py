print("Enter Number of rows : ")
rows = int(input())
print("Enter a boolean 0 or 1\n",
      "If you will enter 1 than computer will print the star in increasing order from up to down ",
      "Other wise we will do vice versa in decreasing order from up to down.")
val = int(input())

if val == 1:
    for i in range(1, rows+1):
        for j in range(i):
            print("*", end=" ")

        print("\n")

if val == 0:
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print("\n")
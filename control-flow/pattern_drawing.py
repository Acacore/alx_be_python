size = int(input("Enter the size of the pattern: "))
n = size
while size != 0:
    for j in range(n):
        print("*", end="")
    size -= 1
    print()
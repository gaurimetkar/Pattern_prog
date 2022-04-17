# Python Program for print Floyd's Triangle

# Entry Point Function
def main():
    # input
    n = int(input("Enter the number of rows:"))
    # count variable
    c = 0

    # outer loop for each row
    for i in range(1, n+1):
        # inner loop for each elements in a particular row
        for j in range(0, i):
            c += 1
            # print space seperated elements in  each row
            print(c, end=' ')
        # prints new line for new row
        print()

# Code Starter
if __name__ == "__main__":
    main()
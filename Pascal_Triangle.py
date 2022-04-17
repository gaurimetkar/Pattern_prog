# Python Program to print Pascal’s Triangle

# Entry Point Function
def main():
    # input
    n = int(input("Enter the number of rows:"))
    #outer loop for each row
    for i in range(0, n):
        #coefficient variable
        c = 1
        #inner loop to print space in the row
        for j in range(1, n-i):
            #print blank space
            print(" ", end=" ")
        #inner loop to print number elemts in a particular row
        for k in range(0, i+1):
            #print space seperated elements in  each row
            print(" ", c, end=" ")
            #calculate c
            c = c*(i-k)//(k+1)
        #prints new line for new row
        print()

# Code Starter
if __name__=="__main__":
    main()
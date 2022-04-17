# Python Program for printing Palindromic Pyramid

# Entry Point Function
def main():
    # input
    n = int(input('Enter the number of rows:'))

    # outer loop for each row
    for i in range(0, n+1):

        # 1st inner loop for printing blank spaces in each row
        for j in range(i, n+1):
                print(' ', end=' ')
        # 2nd inner loop for printing increasing half in each row
        for j in range(1, i + 1):
            print(j, end=' ')
        # 3rd inner loop for printing decreasing half in each row
        for j in range(i - 1, 0, -1):
            print(j, end=' ')

        # print new line character for next row
        print()

# Code Starter
if __name__ == "__main__":
    main()
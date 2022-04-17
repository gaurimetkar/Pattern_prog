# Python Program to find out longest palindrome in a given array

# Function to check if a number is palindrome number
def isPalindrome(n):
    return(str(n)==str(n)[::-1])

# Entry point function
def main():
    n = int(input("Enter the size of array:"))
    arr1 = []
    for i in range(n):
        print("Enter number:", i+1)
        arr1.append(int(input()))
    print("The given array is:", arr1)
    arr1.sort(reverse=True)
    print("The sorted array is:", arr1)

    flag = 1
    for i in arr1:
        if isPalindrome(i):
            print("Largest palindrome in the array is", i)
            flag = 0
            break
    if(flag):
        print("There is no palindrome in the given array")

# Code starter
if __name__=="__main__":
    main()
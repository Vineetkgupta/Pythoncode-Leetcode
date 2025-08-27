class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (but not 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


def main():
    try:
        user_input = int(input("Enter an integer to check if it's a palindrome: "))
        solution = Solution()
        if solution.isPalindrome(user_input):
            print(f"{user_input} is a palindrome.")
        else:
            print(f"{user_input} is not a palindrome.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()

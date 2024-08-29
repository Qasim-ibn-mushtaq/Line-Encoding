import matplotlib.pyplot as plt
import numpy as np

def b8zs_encoding(bits):
    encoded_bits = []
    consecutive_zeros_count = 0

    for bit in bits:
        if bit == '1':
            encoded_bits.append(1)
            consecutive_zeros_count = 0
        elif bit == '0':
            consecutive_zeros_count += 1
            if consecutive_zeros_count == 8:
                encoded_bits.extend([0, 0, 0, 0, 0, 0, 0, 0])
                consecutive_zeros_count = 0
            else:
                encoded_bits.append(0)

    return encoded_bits

def longest_palindrome(s):
    longest_palindrome = ''
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrome = s[i]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if len(longest_palindrome) < len(s[i:j + 1]):
                        longest_palindrome = s[i:j + 1]
    return longest_palindrome

def main():
    binary_data = input("Enter the data: ")
    b8zs_data = b8zs_encoding(binary_data)
    palindrome = longest_palindrome(binary_data)
    
    print("Binary Data:", list(binary_data))
    print("B8ZS Encoded Data:", b8zs_data)
    print("Longest palindrome in dataStream: ", palindrome)

    def plot_b8zs_data(b8zs_data):
        plt.step(range(len(b8zs_data)), b8zs_data, where='post', color='blue', linewidth=4)
        plt.title('B8ZS Encoded Data')
        plt.xlabel('Bit Index')
        plt.ylabel('Voltage Level')
        plt.axhline(0, color='red')
        plt.ylim(-1.5, 1.5)
        for i in range(0, len(b8zs_data)):
            plt.axvline(i, color='grey', linestyle='--')
        plt.show()

    plot_b8zs_data(b8zs_data)

if __name__ == "__main__":
    main()

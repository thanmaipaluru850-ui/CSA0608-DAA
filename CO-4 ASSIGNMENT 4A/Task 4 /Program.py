Task 4: Word Break using Dynamic Programming
def word_break(text, dictionary):
    n = len(text)
    dp = [False] * (n + 1)
    dp[0] = True

    for end in range(1, n + 1):
        for start in range(end):
            if dp[start] and text[start:end] in dictionary:
                dp[end] = True
                break
    return dp[n], dp

if __name__ == "__main__":
    result, states = word_break("abc", {"bc"})
    print("Failing case: text='abc', dictionary={'bc'}")
    print("DP states:", states)
    print("Can segment:", result)
    result2, states2 = word_break("apple", {"app", "le", "apple"})
    print("Regression case: text='apple'")
    print("DP states:", states2)
    print("Can segment:", result2)

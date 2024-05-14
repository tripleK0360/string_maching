#!/usr/bin/env python3

string1 = input("Enter the correct string: ")
string2 = input("Enter the  wrong  string: ")
# string1 = "tsudanuma"
# string2 = "tsadanmda"

def matching(string1, string2):
    dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    match1 = ""
    match2 = ""
    judges = ""
    i = len(string1)
    j = len(string2)
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            match1 = string1[i - 1] + match1
            match2 = string2[j - 1] + match2
            judges = " " + judges
            i -= 1
            j -= 1
        elif string1[i - 2] == string2[j - 2] and string1[i] == string2[j]:
            match1 = string1[i - 1] + match1
            match2 = string2[j - 1] + match2
            judges = "S" + judges
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            match1 = string1[i - 1] + match1
            match2 = "_" + match2
            judges = "D" + judges
            i -= 1
        else:
            match1 = " " + match1
            match2 = string2[j - 1] + match2
            judges = "I" + judges
            j -= 1

    return match1, match2, judges

match1, match2, judges = matching(string1, string2)
print(" correct string:", match1)
print("   wrong string:", match2)
print("matching result:", judges)
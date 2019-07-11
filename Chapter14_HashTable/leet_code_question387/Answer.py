def first_unique_char(s):
    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1

    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
# Problem: Given two strings S and T,
# find out whether any anagram of T is a Substring of S.


def isAnagramOccured(s, t):
    len_s = len(s)
    len_t = len(t)
    if(len_s < len_t):
        return False
    
    s1 = sorted(t)

    for i in range(len_s - len_t):
        if(sorted(s[i:i+len_t]) == s1):
            return True

    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(isAnagramOccured(s, t))

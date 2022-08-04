# https://leetcode.com/problems/valid-anagram

def isAnagram(s, t) :
    chars = 256
    # since 's' and 't' consist of only lower case chars so,
    # we can also create a char array of 26 size.

    count1, count2 = [0]*chars, [0]*chars
    
    for i in s :
        count1[ord(i)] += 1         # count1[ord(i)-97]
    
    for i in t :
        count2[ord(i)] += 1         # count1[ord(i)-97]
    
    for i in range(chars) :
        if count1[i] != count2[i] :
            return False
    return True


s = "b"
t = "d"

print(isAnagram(s,t))

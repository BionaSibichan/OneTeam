def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagram" if is_anagram(s1, s2) else "Not an Anagram")
def remove(s):
    n = int(input())
    a = ""
    for i in range(len(s)):
        if i != n:
            a += s[i]
    return a

string_input = input()
print(remove(string_input))

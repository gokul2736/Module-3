s = "Hannah"
s_lower = s.lower()
if s_lower == s_lower[::-1]:
    print(f'The string "{s}" is a palindrome.')
else:
    print(f'The string "{s}" is not a palindrome.')
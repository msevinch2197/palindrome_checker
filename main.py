def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    
    return cleaned == cleaned[::-1]

matn = input("Matn kiriting: ")

if is_palindrome(matn):
    print("Bu palindrome ✅")
else:
    print("Bu palindrome emas ❌")

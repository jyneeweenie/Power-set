def substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

arr = input("Enter strings: ").split()

for s in arr:
    print(f"Substrings of '{s}':", substrings(s))

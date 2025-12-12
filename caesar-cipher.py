def encrypt(s: str, shift: int = 3) -> str:
    result = ""
    for c in s:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            offset = (ord(c) - base + shift) % 26
            result += chr(base + offset)
        else:
            result += c

    return result


def decrypt(s: str, shift: int = 3) -> str:
    result = ""
    for c in s:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            offset = (ord(c) - base - shift) % 26
            result += chr(base + offset)
        else:
            result += c

    return result


print(encrypt("I'm a robot!"))
print(decrypt("L'p d urerw!"))

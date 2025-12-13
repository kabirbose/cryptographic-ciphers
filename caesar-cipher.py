class CaesarCipher:
    def __init__(self, shift: int = 3):
        self.shift = shift

    def encrypt(self, s: str) -> str:
        result = ""
        for c in s:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                offset = (ord(c) - base + self.shift) % 26
                result += chr(base + offset)
            else:
                result += c

        return result

    def decrypt(self, s: str) -> str:
        result = ""
        for c in s:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                offset = (ord(c) - base - self.shift) % 26
                result += chr(base + offset)
            else:
                result += c

        return result


caesar = CaesarCipher(5)
encrypt = caesar.encrypt("I'm a robot!")
decrypt = caesar.decrypt("L'p d urerw!")

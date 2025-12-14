import string


class ViginereCipher:
    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key.upper()
        self.alphabet = string.ascii_uppercase

    # generate a matrix to map values
    def gen_matrix(self):
        matrix = []
        for i in range(len(self.alphabet)):
            row = self.alphabet[i:] + self.alphabet[:i]
            matrix.append(row)

        return matrix

    # generate a keystream to match the length of the plaintext
    def gen_keystream(self) -> str:
        keystream = ""
        if len(self.key) == len(self.text):
            keystream = self.key
        elif len(self.key) > len(self.text):
            return "Key cannot be larger than plaintext"
        else:
            while len(keystream) <= len(self.text):
                keystream += self.key
            keystream = keystream[: len(self.text)]

        return keystream

    # map plaintext and keystream characters to matrix
    def encrypt(self) -> str:
        result = ""

        # map the text and keystream characters to matrix
        for p_char, k_char in zip(self.text, self.gen_keystream()):
            if not p_char.isalpha() or not k_char.isalpha():
                result += p_char
            else:
                col_index = self.alphabet.index(p_char)
                row_index = self.alphabet.index(k_char)
                result += self.gen_matrix()[col_index][row_index]

        return result

    # map ciphertext and keystream characters to matrix
    def decrypt(self) -> str:
        result = ""

        for c_char, k_char in zip(self.text, self.gen_keystream()):
            if not c_char.isalpha() or not k_char.isalpha():
                result += c_char
            else:
                row_index = self.alphabet.index(k_char)
                col_index = self.gen_matrix()[row_index].index(c_char)
                plain_char = self.alphabet[col_index]
                result += plain_char

        return result


print(ViginereCipher("aTTACK1AT2DAWN3", "LEMON").encrypt())
print(ViginereCipher("LXFOPV1MH2OEIB3", "LEMON").decrypt())

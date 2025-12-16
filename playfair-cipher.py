import string


class PlayfairCipher:
    def __init__(self, key, text):
        self.key = key.upper()
        self.text = text.upper()
        self.alphabet = string.ascii_uppercase.replace("J", "")

    def gen_matrix(self):
        matrix = []
        used_chars = set()

        temp = []
        for i in range(len(self.key)):
            if self.key[i] not in used_chars:
                temp.append(self.key[i])
                used_chars.add(self.key[i])
                if len(temp) == 5:
                    matrix.append(temp[:])
                    temp.clear()

        for i in range(len(self.alphabet)):
            if self.alphabet[i] not in used_chars:
                temp.append(self.alphabet[i])
                used_chars.add(self.alphabet[i])
                if len(temp) == 5:
                    matrix.append(temp[:])
                    temp.clear()

        return matrix

    def format_text(self) -> str:
        text = self.text
        formatted = ""

        for i, char in enumerate(text):
            formatted += char

            if i < len(text) - 1 and char == text[i + 1]:
                formatted += "X"

        return formatted

    def text_pairs(self):
        formatted_text = self.format_text()

        if len(formatted_text) % 2 != 0:
            formatted_text += "X"

        pairs = []
        for i in range(0, len(formatted_text), 2):
            pairs.append(formatted_text[i : i + 2])

        return pairs

    def encrypt(self):
        pairs = self.text_pairs()
        matrix = self.gen_matrix()
        result = ""

        v1_row, v1_col = 0, 0
        v2_row, v2_col = 0, 0

        coords = []

        for i in range(len(pairs)):
            v1 = pairs[i][0]
            v2 = pairs[i][1]

            v1_row = v1_col = v2_row = v2_col = None
            for j in range(len(matrix)):
                if v1 in matrix[j]:
                    v1_row = j
                    v1_col = matrix[j].index(v1)
                if v2 in matrix[j]:
                    v2_row = j
                    v2_col = matrix[j].index(v2)

            coords.append([v1_row, v1_col])
            coords.append([v2_row, v2_col])

        i = 0
        while i < len(coords):
            v1_row, v1_col = coords[i][0], coords[i][1]
            v2_row, v2_col = coords[i + 1][0], coords[i + 1][1]
            # print(
            #     f"{i//2}) [{v1_row}, {v1_col}], [{v2_row}, {v2_col}] -> {matrix[v1_row][v1_col]}, {matrix[v2_row][v2_col]}"
            # )

            # case 1: v1_row == v2_row then replace both with letter on right (wrap around if needed)
            if v1_row == v2_row:
                if v1_col == 4:
                    coords[i][1] = 0
                if v2_col == 4:
                    coords[i + 1][1] = 0
                else:
                    coords[i][1] += 1
                    coords[i + 1][1] += 1

            # case 2: v1_col == v2_col then replace both with letter on bottom (wrap around if needed)
            if v1_col == v2_col:
                if v1_row == 4:
                    coords[i][0] = 0
                if v2_row == 4:
                    coords[i + 1][0] = 0
                else:
                    coords[i][0] += 1
                    coords[i + 1][0] += 1

            # case 3: else then v1col = v2col
            if v1_row != v2_row and v1_col != v2_col:
                temp1 = coords[i][1]
                temp2 = coords[i + 1][1]
                coords[i][1] = temp2
                coords[i + 1][1] = temp1

            i += 2

        k = 0
        while k < len(coords):
            v1_row, v1_col = coords[k][0], coords[k][1]
            v2_row, v2_col = coords[k + 1][0], coords[k + 1][1]
            # print(
            #     f"{i//2}) [{v1_row}, {v1_col}], [{v2_row}, {v2_col}] -> {matrix[v1_row][v1_col]}, {matrix[v2_row][v2_col]}"
            # )
            result += matrix[v1_row][v1_col] + matrix[v2_row][v2_col]
            k += 2

        return result


print(PlayfairCipher("HELLO", "PLAYFAIR").encrypt())

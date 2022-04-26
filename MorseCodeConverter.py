morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
}


def string_to_morse(text):
    letters_cap = text.upper()
    characters = list(letters_cap)
    convert = [morse_dict[char] for char in characters]
    out = " ".join(convert)
    return out


user_text = input("Please enter text convert to morse code: ")
answer = string_to_morse(user_text)
print(answer)

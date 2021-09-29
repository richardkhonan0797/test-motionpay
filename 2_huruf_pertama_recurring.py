from typing import List, Union


def huruf_pertama_recurring(chars: List[str]) -> Union[str, bool]:

    previous_chars = []

    for char in chars:
        if char in previous_chars:
            return char
        else:
            previous_chars.append(char)

    return False

print(huruf_pertama_recurring(chars=['A', 'B', 'C', 'B', 'A']))                 # B
print(huruf_pertama_recurring(chars=['A', 'B', 'C', 'D', 'E', 'C', 'F', 'Z']))  # C
print(huruf_pertama_recurring(chars=['A', 'B', 'C', 'X', 'Y', 'Z']))            # False
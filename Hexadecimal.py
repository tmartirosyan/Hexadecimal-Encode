def EncodeToHexadecimal(simple_text):
    def NumberToHexadecimal(number):
        number_more_than_10_value_in_char = ['A', 'B', 'C', 'D', 'E', 'F']
        text = ""
        while number >= 16:
            char = number % 16
            if (char >= 10):
                text += number_more_than_10_value_in_char[char - 10]
            else:
                text += str(char)
            number //= 16
        text += str(number)
        return text[::-1]

    text = ""
    for char in simple_text:
        text += NumberToHexadecimal(ord(char)) + " "
    return text


string_to_binary_from_user = "You must send answers to exercises 4 hours before the lesson."

print(EncodeToHexadecimal(string_to_binary_from_user))
# Python program to illustrate
# chr() builtin function

print(chr(71), chr(101),
      chr(101), chr(107),
      chr(115), chr(32),
      chr(102), chr(111),
      chr(114), chr(32),
      chr(71), chr(101),
      chr(101), chr(107),
      chr(115))


# chr() builtin function

numbers = [17, 38, 79]

for number in numbers:
    # Convert ASCII-based number to character.
    letter = chr(number)
    print("Character of ASCII value", number, "is ", letter)

    unicode_value = 8364
    character = chr(unicode_value)
    print(character)




    unicode_value = 128516

    unicode_values = range(256)
    characters = [chr(value) for value in unicode_values]
    print(characters)
    character = chr(unicode_value)
    print(character)

    # Python program to illustrate
    # chr() builtin function
    # if value given is
    # out of range

    # Convert ASCII-based number to character
    print(chr(400))
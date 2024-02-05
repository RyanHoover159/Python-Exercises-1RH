userInput = input("Enter a string: ")
lowercaseLetters = ''.join(c for c in userInput if c.islower())
uppercaseLetters = ''.join(c for c in userInput if c.isupper())

noSpacesString = userInput.replace(" ", "")
resultString = lowercaseLetters + uppercaseLetters
print("Modified string:", resultString)
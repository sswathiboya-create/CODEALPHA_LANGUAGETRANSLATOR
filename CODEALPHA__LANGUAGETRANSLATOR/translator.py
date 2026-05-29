from deep_translator import GoogleTranslator

print("🌐 LANGUAGE TRANSLATOR")

# User input
text = input("Enter text: ")

# Language options
print("\nSelect target language:")
print("1. Telugu")
print("2. Hindi")
print("3. Tamil")
print("4. French")

choice = input("Enter choice (1-4): ")

# Language dictionary
languages = {
    "1": "te",
    "2": "hi",
    "3": "ta",
    "4": "fr"
}

# Translation
if choice in languages:
    translated = GoogleTranslator(
        source='auto',
        target=languages[choice]
    ).translate(text)

    print("\nTranslated Text:", translated)

else:
    print("Invalid Choice")
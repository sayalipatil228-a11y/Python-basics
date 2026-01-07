letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

print(letter.replace("<|NAME|>", "Sayali").replace("<|DATE|>", "10th march 2026"))
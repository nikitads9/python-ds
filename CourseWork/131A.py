text = input()
if len(text) > 0:
    swapcase = True
    for i in range (1, len(text)):
        if text[i].islower():
            swapcase = False
    if swapcase:
        text = text[0] +text[1:].lower()
        if text[0].isupper():
            text = text[0].lower() + text[1:]
        elif text[0].islower(): 
            text = text[0].upper() + text[1:]
    print(text)
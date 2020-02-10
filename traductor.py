### TRAFADUCTORAFA ###

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "r":
            translation = translation + "rafa"
        else:
            translation = translation + letter
    return translation

print(translate(input("Introduce una frase que contenga la letra 'r': ")))

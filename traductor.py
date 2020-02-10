###########

# TRAFADUCTORAFA #

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "r":
            if letter.isupper():
                translation = translation + "Rafa"
            else:
                translation = translation + "rafa"
        else:
            translation = translation + letter
    return translation

print(translate(input("Introduce una frase que contenga la letra 'r': ")))

###########

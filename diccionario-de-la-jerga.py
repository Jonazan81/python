###########

# REAL DICCIONARIO DE LA JERGA ADOLESCENTE #

print("Bienvenido al Real Diccionario de la Jerga Adolescente.\n\n > ¿Ha puesto Lolo un mensaje críptico en el grupo con una palabra que desconoces?\n\n > ¿Te ha llegado un WhatsApp de Mateu con un mensaje indescifrable?\n\nSi tu respuesta es 'sí', este diccionario podría ayudarte.\n")

print(" INSTRUCCIONES >>> Escribe el acrónimo que quieras descifrar enteramente en minúscula y sin puntuaciones de ningún tipo.\n")

acronym_conversions = {
    "svyqm": "sí, va; y qué más",
    "uynmst": "una y no más, santo tomás",
    "avlvtdep": "a veces la vida te da esos palos",
    "tpctp": "te pongas como te pongas",
    "lqvelqh": "lo que ves es lo que hay",
    "nsyls": "no, si ya lo sé",
    "ancs": "algunos nacen con suerte",
    "bpt": "bien por ti",
    "bpe": "bien por él (ella/ ellos/ ellas)",
    "bj": "bien jugado",
    "wp": "well played",
    "wps": "well played, sir",
    "accllssm": "a cada cerdo le llega su san martín",
    "mlvadotlplalt": "me lo vas a decir o te lo piensas llevar a la tumba",
    "tldontld": "te lo digo o no te lo digo",
    "tlpontlp": "te lo paso o no te lo paso",
    "snldr": "si no lo dices revientas",
    "css": "correcto, sí señor",
    "ntnpnnqdar": "no tengo nada positivo ni negativo que decir al respecto",
    "escyhqr": "es su cultura y hay que respetarla",
    "eemvqet": "esto es más viejo que el tango",
    "emdyeqsmr": "es mi decisión y espero que se me respete",
    "amp": "aunque me pese",
    "atp": "aunque te pese",
    "alp": "aunque le(s) pese",
    "mg": "muy gracioso (con ironía)",
    "ys": "ya sabes",
    "anlaud": "a nadie le amarga un dulce",
    "kval": "qué va a llover (con ironía)",
    "caqns": "cuéntame algo que no sepa",
    "tdlm": "te deseo lo mejor",
    "ldlm": "le(s) deseo lo mejor",
    "pd": "pobre diablo",
    "tcqsg": "te crees que soy gilipollas (con ironía)",
    "nls": "no lo sé",
    "up": "una pena (con ironía)",
    "atpc": "a tomar por culo",
    "yyapel": "y yo aquí partiéndome el lomo",
    "mtqs": "me temo que sí",
    "mtqn": "me temo que no",
    "sdls": "sólo dios lo sabe",
    "uacn": "un altre cop no",
    "son": "sí o no",
    "tlpontlp": "te lo paso o no te lo paso",
    "vv": "venga, va",
    "byvn": "bueno ya vale, ¿no?",
    "nei": "no estarás insinuando",
    "epstyyee": "estos podríamos ser tú y yo en edimburgo",
    "yqn": "y quién no",
    "yenlps": "yo esto no lo puedo soportar",
    "ldcsfam": "lo dices como si fuera algo malo",
    "dicle": "da igual cuándo leas esto",
    "mpqp": "me pregunto qué pasará (con ironía)",
    "tlhm": "¿tú lo harías mejor? (con ironía)",
    "yeldo": "y encima lo dirás orgulloso",
    "otemloysmt": "o tú eres muy listo o yo soy muy tonto",
    "ecaa": "esta conversación acaba aquí",
    "ntlpj": "no te lo perdonaré jamás",
    "nslpj": "no se lo perdonaré jamás",
    "ctcy": "cuál tú, cuál yo",
    "eheeeo": "el hombre elige, el esclavo obedece",
    "ntj": "no te jode (con ironía)",
    "ytvua": "¿y tú? venga, un abrazo (con ironía)",
    "sttda": "si te tuviera delante ahora",
    "tqpae": "tendrás que preguntárselo a él/ ella/ ellos/ ellas",
    "nlvad": "no lo voy a decir",
    "bpn": "bueno, pues nada",
    "eppintg": "és per pixar i no treure gota",
    "leepade": "los errores están para aprender de ellos",
    "pewale": "petarle el whatsapp a la elena",
    "cocqeymls": "cuéntame otro cuento que ése ya me lo sé",
    "seg": "soñar es gratis",
    "hqsuhdlgppde": "hay que ser un hijo de la gran puta para decir eso",
    "qpelve": "qué puta es la vida, eh",
    "mgpc": "muy gracioso, pero correcto",
    "nedmrlc": "nunca está de más recordar los clásicos",
    "attlvad": "a ti te lo voy a decir (con ironía)",
    "addo": "a diferencia de otros",
    "csnqnmc": "cómo se nota que no me conoces",
    "fp": "fotopolla",
    "nsum": "no sea usted malpensado",
    
}

acronym = input("Por favor, introduce un acrónimo: ")

while acronym in acronym_conversions:
    print(acronym_conversions[acronym])
    if acronym in acronym_conversions:
        acronym = input("Por favor, introduce un acrónimo: ")

while acronym not in acronym_conversions:
    acronym = input("El acrónimo introducido no existe; por favor, vuelve a intentarlo: ")
    while acronym in acronym_conversions:
        print(acronym_conversions[acronym])
        if acronym in acronym_conversions:
            acronym = input("Por favor, introduce un acrónimo: ")
      
###########

# © 2020 Rafa Fernández Rivera #
#                              #
#          All Rights Reserved #

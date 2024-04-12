import random

def joke():
    chistes = [
        "¿Qué le dice un array a otro? ¿Me das tu posición?",
        "¿Por qué los programadores prefieren los gatos? Porque tienen purr-ogramación orientada a objetos.",
        "¿Cuál es el animal favorito de un programador? ¡El bucle!",
        "¿Qué le dice un booleano a otro? ¡No seas falso!",
        "¿Qué es un terapeuta para un HTML? ¡Un tag de cierre!",
        "¿Por qué fue el programa a terapia? ¡Porque tenía demasiados bugs!",
        "¿Qué hace un programador cuando se aburre? ¡Juega con su gato de datos!",
        "¿Qué le dice un cable de red a otro? ¡Tienes una conexión conmigo!",
        "¿Cuál es el animal más peligroso del mundo? El data-ware.",
        "¿Qué le dice un objeto a otro? ¿Quieres que te herede?",
        "¿Por qué los programadores no les gusta el verano? ¡Porque sale el sol y no hay nada que debuggear!",
        "¿Qué le dice un bit al otro? Me encantas a 1 y a 0.",
        "¿Qué hace un programador en la playa? ¡Cuenta BITS!",
        "¿Qué le dice una base de datos a otra? NoSQL, no party.",
        "¿Por qué los programadores odian el mar? ¡Porque solo saben contar hasta la playa!",
        "¿Cuál es el colmo de un programador? ¡Que le muerdan un byte!",
        "¿Cuál es la canción favorita de un programador? 99 bugs en el código, 99 bugs en el código, coges uno y lo parcheas, 127 bugs en el código...",
        "¿Por qué los programadores siempre confunden Halloween con Navidad? Porque oct(31) == dec(25).",
        "¿Cuál es el postre favorito de un programador? ¡El flan-ate!",
        "¿Por qué el programador siempre está frío? Porque siempre trabaja con Windows.",
        "¿Cómo se llama el pez más programador? ¡El DataFish!",
        "¿Por qué los programadores siempre están nerviosos? ¡Porque siempre están en estado binario!",
        "¿Qué le dice una impresora a otra? ¿Esa hoja es tuya o es una copia?",
        "¿Cuál es la comida favorita de un programador? ¡El archivo Mac 'n' Cheese!",
        "¿Por qué los programadores siempre confunden la Navidad con Halloween? ¡Porque Oct 31 = Dec 25!"
    ]
    frases_previas = [
        "Muy bien, aquí va un chiste:",
        "Este chiste te va a encantar... creo,",
        "¡Genial! Estaba esperando este momento,",
        "Apuesto a que no te sabes este,"
    ]
    chiste_seleccionado = random.choice(chistes)
    frase_previa = random.choice(frases_previas)
    return frase_previa + " " + chiste_seleccionado

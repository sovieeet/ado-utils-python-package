from num2words import num2words

def number_to_words(num):
    lang="es"
    words = num2words(num, lang=lang)
    
    return words

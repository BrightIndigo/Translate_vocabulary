import random

WORDS = {
    'suszarka do włosów': 'der Föhn',
    'zmywarka do naczyń': 'der Geschirrspüler',
    'ekspres do kawy': 'die Kaffeemaschine',
    'żelazko': 'das Bügeleisen',
    'kuchenka elektryczna': 'der Elektroherd',
    'czajnik elektryczny': 'der Wasserkocher',
    'pralka': 'die Waschmaschine',
    'blender': 'der Mixer',
    'odkurzacz': 'der Staubsauger',
    'koszula': 'das Hemd',
    'naczynia': 'das Geschirr',
    'włosy': 'die Haare',
    'espresso': 'den Espresso',
    'pranie': 'die Wäsche',
    'stek': 'das Steak',
    'pokój': 'das Zimmer',
    'woda': 'das Wasser',
    'śmietanka': 'Sahne',
    'ubić': 'schlagen',
    'gotować': 'kochen',
    'prasować': 'bügeln',
    'suszyć': 'trocknen',
    'przygotować': 'zubereiten',
    'myć': 'waschen',
    'smażyć': 'braten',
    'sprzątać': 'aufräumen',
    'płukanie': 'spülen',
    'der Föhn': 'suszarka do włosów',
    'der Geschirrspüler': 'zmywarka do naczyń',
    'die Kaffeemaschine': 'ekspres do kawy',
    'das Bügeleisen': 'żelazko',
    'der Elektroherd': 'kuchenka elektryczna',
    'der Wasserkocher': 'czajnik elektryczny',
    'die Waschmaschine': 'pralka',
    'der Mixer': 'blender',
    'der Staubsauger': 'odkurzacz',
    'das Hemd': 'koszula',
    'das Geschirr': 'naczynia',
    'die Haare': 'włosy',
    'den Espresso': 'espresso',
    'die Wäsche': 'pranie',
    'das Steak': 'stek',
    'das Zimmer': 'pokój',
    'Sahne': 'śmietanka',
    'schlagen': 'ubić',
    'kochen': 'gotować',
    'bügeln': 'prasować',
    'trocknen': 'suszyć',
    'zubereiten': 'przygotować',
    'waschen': 'myć',
    'braten': 'smażyć',
    'aufräumen': 'sprzątać',
    'spülen': 'płukanie',

}

points = 0

while True:
    chosen_word_pl = random.choice(list(WORDS.keys()))
    chosen_word_de = WORDS[chosen_word_pl]

    print(f"Wybrano słowo. Przetłumacz je (tutaj masz wybrane niemieckie litery do skopiowania: ü, ö, ß, ä): {chosen_word_pl}")

    while True:
        translation = input("Tłumaczenie: ")

        if translation == '!':
            print("Koniec programu. Twój wynik to:", points)
            exit()

        elif translation == chosen_word_de:
            points += 1
            print("Poprawne tłumaczenie! Gratulacje! Twój wynik to:", points)
            break

        else:
            print("Niepoprawne tłumaczenie. Spróbuj jeszcze raz.")

    if translation == chosen_word_de:
        continue
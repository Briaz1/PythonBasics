from random import choice, shuffle


def get_jokes(amount: int, repeat=True):
    """
    :param amount: number of jokes
    :param repeat: Repeat words in jokes, =True(optional) - yes, =False - no.
    :return: print list of jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []

    if repeat is True:
        for _ in range(amount):
            jokes_list.append(''.join(f'{choice(nouns).capitalize()} {choice(adverbs)} {choice(adjectives)}'))

    else:
        """shuffles the lists."""
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for num in range(amount):
            """Stop the program when all words have been used."""
            if num + 1 > len(nouns):
                print(f'Максимальное количество шуток: {len(jokes_list)}!')
                break
            jokes_list.append(''.join(f'{nouns[num].capitalize()} {adverbs[num]} {adjectives[num]}'))

    print(jokes_list)


get_jokes(6)
get_jokes(6, repeat=False)

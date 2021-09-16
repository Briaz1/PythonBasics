from random import choice, shuffle


def get_jokes(amount, repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []

    if repeat is True:
        for _ in range(amount):
            jokes_list.append(''.join(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'))

    else:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for num in range(amount):
            if num + 1 > len(nouns):
                print(f'Максимальное количество шуток: {len(jokes_list)}!')
                break
            jokes_list.append(''.join(f'{nouns[num]} {adverbs[num]} {adjectives[num]}'))

    print(jokes_list)


get_jokes(6)
get_jokes(6, repeat=False)

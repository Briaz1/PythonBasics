from collections import Counter


def spammers_finder(logs_file):
    with open(logs_file, 'rt') as fp:
        spammers = Counter(line.split()[0] for line in fp).most_common(5)
        for i, ip in enumerate(spammers, 1):
            yield f'Топ {i} по количеству запросов ip-адрес {ip[0]}. Количество запросов: {ip[1]}.'


for spammer in spammers_finder('nginx_logs.txt'):
    print(spammer)

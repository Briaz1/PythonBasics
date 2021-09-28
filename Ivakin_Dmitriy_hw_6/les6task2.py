from collections import Counter


def spammers_finder(logs_file):
    with open(logs_file, 'rt') as fp:
        spammers = dict(Counter(line.split()[0] for line in fp).most_common(5))
        for i, ip in enumerate(spammers):
            yield f'Топ {i + 1} по количеству запросов ip-адрес {ip}. Количество запросов:  {spammers[ip]}.'


for spammer in spammers_finder('nginx_logs.txt'):
    print(spammer)

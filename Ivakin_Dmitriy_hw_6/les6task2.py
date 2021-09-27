def get_key(val):
    for key, value in dct.items():
        if val == value:
            return key


dct = {}

with open('nginx_logs.txt', 'rt') as fp:
    for line in fp:
        ip = line.split()[0]
        dct.setdefault(ip, 0)
        dct[ip] += 1
print(dct)
print(get_key(max(dct.values())))

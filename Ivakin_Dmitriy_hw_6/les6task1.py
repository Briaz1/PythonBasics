with open('nginx_logs.txt', 'rt') as fp:
    request_list = ((line.split()[0], line.split()[5], line.split()[6]) for line in fp)
    for el in request_list:
        print(el)

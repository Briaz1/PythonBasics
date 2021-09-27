request_list = []

with open('nginx_logs.txt', 'rt') as fp:
    for line in fp:
        remote_ip = line.split()[0]
        request_type = line.split()[5]
        requested_resource = line.split()[6]
        request_list.append((remote_ip, request_type, requested_resource))
print(*request_list, sep='\n')

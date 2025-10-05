from collections import Counter
from .log_parser import parse_log_line

def analyze_log_file(path):
    logs = []
    with open(path, 'r') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                logs.append(parsed)

    ips = Counter(log['ip'] for log in logs)
    endpoints = Counter(log['path'] for log in logs)
    statuses = Counter(log['status'] for log in logs)

    print('\n📊 Log Analysis Results:')
    print('Top 5 IPs:')
    for ip, count in ips.most_common(5):
        print(f'  {ip}: {count} requests')

    print('\nTop 5 Endpoints:')
    for path, count in endpoints.most_common(5):
        print(f'  {path}: {count} hits')

    print('\nStatus Code Summary:')
    for code, count in statuses.most_common():
        print(f'  {code}: {count}')

import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) [^\"]+" (?P<status>\d{3}) (?P<size>\d+)'
)

def parse_log_line(line):
    match = LOG_PATTERN.search(line)
    if not match:
        return None
    data = match.groupdict()
    try:
        data['time'] = datetime.strptime(data['time'].split()[0], '%d/%b/%Y:%H:%M:%S')
    except Exception:
        data['time'] = data['time']
    return data

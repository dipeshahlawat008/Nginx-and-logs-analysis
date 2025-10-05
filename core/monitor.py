import time
from .log_parser import parse_log_line

def tail_log_file(path):
    try:
        with open(path, 'r') as f:
            f.seek(0, 2)
            print(f"Watching {path}... (Ctrl+C to stop)")
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                parsed = parse_log_line(line)
                if parsed:
                    print(f"[{parsed.get('time')}] {parsed.get('ip')} {parsed.get('method')} {parsed.get('path')} {parsed.get('status')}")
    except FileNotFoundError:
        print(f"Log file not found: {path}")

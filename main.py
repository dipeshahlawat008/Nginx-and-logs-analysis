#!/usr/bin/env python3
import argparse
from core.log_parser import parse_log_line
from core.analyzer import analyze_log_file
from core.monitor import tail_log_file

def main():
    parser = argparse.ArgumentParser(description="SentinelOps CLI")
    parser.add_argument('--log', default='sample.log', help='Path to access log')
    parser.add_argument('--analyze', action='store_true', help='Analyze existing log')
    parser.add_argument('--watch', action='store_true', help='Watch log live')
    args = parser.parse_args()

    if args.analyze:
        analyze_log_file(args.log)
    elif args.watch:
        tail_log_file(args.log)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

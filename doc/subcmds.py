import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
subparsers = parser.add_subparsers()

max_parser = subparsers.add_parser('max', description='Find the max.')
max_parser.set_defaults(accumulate=max)
max_parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='An integer for the accumulator.')

sum_parser = subparsers.add_parser('sum', description='Sum the integers.')
sum_parser.set_defaults(accumulate=sum)
sum_parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='An integer for the accumulator.')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.accumulate(args.integers))

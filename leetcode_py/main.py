import argparse
from solution import Solution

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        metavar='sub-commands     ',
        help='sub-command help')

    fib_parser = subparsers.add_parser('fib', help='[509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)')
    fib_parser.add_argument(dest='fib', metavar='n', type=int, help='int')

    climbStairs_parser = subparsers.add_parser('climbStairs', help='[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)')
    climbStairs_parser.add_argument(dest='climbStairs', metavar='n', type=int, help='int')

    args = parser.parse_args()

    if hasattr(args, 'fib'):
        result = Solution().fib(args.fib)
        print(result)
    elif hasattr(args, 'climbStairs'):
        result = Solution().climbStairs(args.climbStairs)
        print(result)

if __name__ == "__main__":
    main()
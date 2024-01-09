def fib(self, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    state = [0, 1]
    for i in range(n - 2):
        tmp = state[0] + state[1]
        state[0] = state[1]
        state[1] = tmp
    return state[0] + state[1]
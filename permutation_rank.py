MOD = 998244353


def solve():
    n = int(input())
    perm = list(map(int, input().split()))

    # 预处理阶乘
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    # 树状数组维护剩余数字中比当前数小的个数
    bit = [0] * (n + 1)

    def add(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & -idx

    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    # 初始化：所有数字都可用
    for i in range(1, n + 1):
        add(i, 1)

    rank = 1  # 排名从1开始
    for i in range(n):
        x = perm[i]
        # 比 x 小且还未使用的数字个数
        cnt = query(x - 1)
        rank = (rank + cnt * fact[n - i - 1]) % MOD
        # 标记 x 已使用
        add(x, -1)

    print(rank)


if __name__ == "__main__":
    solve()

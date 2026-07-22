"""
简单测试脚本：验证 permutation_rank.py 的正确性
用法: python test_permutation_rank.py
"""
import subprocess
import sys


def run_case(n, perm, expected):
    """运行程序并比对输出"""
    input_data = f"{n}\n{' '.join(map(str, perm))}\n"
    result = subprocess.run(
        [sys.executable, "permutation_rank.py"],
        input=input_data,
        capture_output=True,
        text=True,
    )
    output = result.stdout.strip()
    status = "PASS" if output == str(expected) else "FAIL"
    print(f"[{status}] n={n}, perm={perm}, expected={expected}, got={output}")
    return output == str(expected)


if __name__ == "__main__":
    cases = [
        # (n, 排列, 期望排名)
        (3, [1, 2, 3], 1),       # 最小的排列，排名1
        (3, [3, 2, 1], 6),       # 最大的排列，排名6
        (3, [2, 1, 3], 3),       # 213 排第3
        (4, [3, 1, 4, 2], 14),   # 之前讲解的例子
        (1, [1], 1),             # 只有1个元素
        (5, [1, 2, 3, 4, 5], 1), # 升序排列，排名1
        (5, [5, 4, 3, 2, 1], 120),  # 降序排列，排名5!=120
    ]

    all_pass = True
    for n, perm, expected in cases:
        if not run_case(n, perm, expected):
            all_pass = False

    if all_pass:
        print("\n所有测试通过!")
        sys.exit(0)
    else:
        print("\n存在失败的测试!")
        sys.exit(1)

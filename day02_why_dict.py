"""D2 实验：为什么 dict 查找比 list 快这么多？

直接运行，不用改任何东西：
    python day02_why_dict.py

看输出里的两个时间，差距会非常夸张。
"""

import time

N = 1_000_000          # 一百万个数据
REPEAT = 100           # 重复查找 100 次

print(f"正在准备 {N:,} 个数据，稍等两三秒...")

numbers = list(range(N))          # 一个列表
index = {i: i for i in range(N)}  # 一个字典，key 和 value 相同

target = N - 1   # 故意找最后一个，让 list 找得最久

# ---------- list：从头挨个比 ----------
start = time.perf_counter()
for _ in range(REPEAT):
    found = target in numbers
t_list = time.perf_counter() - start

# ---------- dict：直接跳过去 ----------
start = time.perf_counter()
for _ in range(REPEAT):
    found = target in index
t_dict = time.perf_counter() - start

# ---------- 输出 ----------
print()
print(f"同样查找 {REPEAT} 次，目标都藏在最后一位：")
print(f"  list 查找用了：{t_list:.4f} 秒")
print(f"  dict 查找用了：{t_dict:.6f} 秒")

if t_dict > 0:
    print(f"  dict 快了约 {t_list / t_dict:,.0f} 倍")

print()
print("为什么？")
print("  list 像一排没编号的柜子，只能从第一个开始一个个拉开看。")
print("  dict 像有编号的储物柜，你知道 999999 号在第几排第几列，直接走过去。")

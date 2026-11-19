"""D1 环境自检脚本

跑通它，说明 Python / numpy / pandas 三件套都正常。
运行方式（在终端里）：
    python day01.py
"""

import sys

import numpy as np
import pandas as pd

print("=" * 42)
print("Python :", sys.version.split()[0])
print("numpy  :", np.__version__)
print("pandas :", pd.__version__)
print("=" * 42)

# --- numpy 练手 ---
a = np.array([1, 2, 3, 4, 5])
print("数组求和 :", a.sum())
print("数组均值 :", a.mean())

# --- pandas 练手 ---
df = pd.DataFrame({
    "科目": ["高数", "英语", "专业课"],
    "分数": [88, 76, 92],
})
print()
print(df)
print("平均分 :", df["分数"].mean())

print()
print("环境跑通 OK")

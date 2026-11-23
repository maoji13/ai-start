"""D3 练习：函数 + 文件读写

你只需要填 TODO 1 —— 把昨天写过的那四行搬进函数里。
其余的我写好了。

运行：python day03.py
"""


# ==========================================================
# 第一件事：定义函数
# ==========================================================
# 函数就是给一段代码起个名字，以后叫名字就能反复用。
# def 是 define（定义）的缩写，括号里是「要传进来的东西」。

def count_chars(text):
    """统计 text 里每个字出现了多少次，返回一个字典。

    参数 text：一段字符串
    返回：{'人': 4, '工': 2, ...} 这样的字典
    """
    counts = {}

    # ---------- TODO 1：把昨天写过的循环搬到这里 ----------
    #
    #   for ch in text:
    #       if ch in counts:
    #           counts[ch] = ????
    #       else:
    #           counts[ch] = ???
    #
    # 跟昨天一模一样，只是 text 变成了函数的参数。
    # 在下面写（注意缩进，要比 def 那一行多 4 个空格）：
    for ch in text:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1


    return counts


# ==========================================================
# 第二件事：读文件
# ==========================================================
# open(路径, "r") 里的 r 表示 read（读）
# encoding="utf-8" 一定要写，否则中文会变成乱码
# with 的作用是：用完自动关文件，不用手动 close

with open("data/note.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(f"读到了文件，一共 {len(content)} 个字符")
print(f"开头 20 个字：{content[:20]}")
print()

# ==========================================================
# 第三件事：调用函数（用上面读到的 content）
# ==========================================================

counts = count_chars(content)

if not counts:
    print("counts 是空的 —— TODO 1 还没填，填完再跑一次")
    raise SystemExit

# 排序取前 10
top10 = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:10]

rows = []
for ch, cnt in top10:
    if ch.strip() == "":
        continue
    rows.append(f"{ch} {cnt}")

print("前 10 高频字：")
for r in rows:
    print(f"  {r}")
print()

# ==========================================================
# 第四件事：写文件
# ==========================================================
# "w" 表示 write（写），文件不存在会新建，存在会被覆盖

with open("data/result.txt", "w", encoding="utf-8") as f:
    f.write("高频字统计结果\n")
    f.write("=" * 24 + "\n")
    for r in rows:
        f.write(r + "\n")

print("结果已经写进 data/result.txt")

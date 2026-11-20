"""D2 练习：用 dict 统计字频

你只需要填 TODO 1 那四行，其余的（排序、打印）我写好了。

运行：python day02_wordcount.py
"""

text = """人工智能是计算机科学的一个分支，它企图了解智能的实质，
并生产出一种新的能以人类智能相似的方式做出反应的智能机器。
该领域的研究包括机器人、语言识别、图像识别、自然语言处理等。
人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大。"""

# counts 就是那个「有编号的储物柜」
counts = {}

# ================= TODO 1：把下面四行补完整 =================
#
# 目标：走过 text 里的每一个字，把它记进 counts
#
#   for ch in text:                  <- 已经给你了
#       if ch in counts:             <- 已经给你了
#           counts[ch] = ???         <- 你来填
#       else:                        <- 已经给你了
#           counts[ch] = ???         <- 你来填
#
# 提示：这两个问号，就是刚才你在窗口里敲过的 counts["人"] = 1
#       和 counts["人"] = counts["人"] + 1 里面的右边那部分

for ch in text:
    if ch in counts:

        counts[ch] = counts[ch] + 1          # <- 把 pass 删掉，换成你写的一行

    else:

        counts[ch] = 1          # <- 把 pass 删掉，换成你写的一行

# ================= 下面是排序和打印，已经写好 =================

if not counts:
    print("counts 还是空的，说明上面没填对")
else:
    top10 = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:10]
    print("出现次数最多的前 10 个字符：")
    for ch, cnt in top10:
        if ch.strip() == "":
            continue
        print(f"  {ch}   {cnt}")

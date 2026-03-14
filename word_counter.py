# 读取文件
with open('sample.txt', 'r') as f:
    text = f.read()

# 分割单词并统计
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 写入结果文件
with open('output.txt', 'w') as f:
    for word, count in word_count.items():
        f.write(f"{word}: {count}\n")

print("统计完成，结果已保存到 output.txt")
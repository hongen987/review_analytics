data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1#=count = count + 1
        if count % 100000 == 0:#{%}用來求餘數
            print(count)
print('已讀取完檔案, 總共有', len(data), '筆資料')
x = 0
for lines in data:
        x += len(lines)
print(x/len(data))
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))
print(new[1])

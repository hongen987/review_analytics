data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1#=count = count + 1
		if count % 100000 == 0:#{%}用來求餘數
		    print(count)
print(len(data))
print(data[0])#印出第0筆資料
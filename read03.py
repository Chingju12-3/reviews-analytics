data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # % = 是用來求餘數
			print(len(data))
print('檔案讀取完成，總共有', len(data), '筆資料') # len = 長度

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data: # for loop = 把清單中東西一個一個拿出來
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
# 將上面程式濃縮 good = [d for d in data if 'good' in d]
# print(good)
# bad = ['bad' in d for d in data]
# print(bad)
print(good[0])

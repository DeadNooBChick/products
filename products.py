products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = []
	# p.append(name) #小清單 P
	# p.append(price) #小清單 P
	p = [name, price] #呢個係上三行既coding 簡寫寫法
	products.append(p) #小清單 P 入 主清單 product
	# products.append([name, price]) 呢個係第7-11行最簡單寫法
#print(products)

products [0][0] #product 入面既第0格裡既第0格

for product in products:
	print(product[0], '的價格是', product[1])


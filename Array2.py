
def check(y):

	a = [1,3,9,11,15,23]
	
	guess_num = int(y)
	
	q = 0
	
	
	while q < len(a):
		check_val = guess_num - a[q]

		if check_val in a:
			print('Values found' , a[q] ,' ', check_val)
			break
		else:
			print('No Values found')
			
		q += 1
			

	
if __name__ == "__main__":
	x = input('Search: ')
	
	if x.isdigit():
		y = x
	else:
		raise systemexit
	check(y)
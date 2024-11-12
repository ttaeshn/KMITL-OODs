def bon(w):
	max_char = "";max_count = 0
	for i in w:
		if w.count(i) > max_count:
			max_char = i
			max_count = w.count(i)
	return (ord(max_char) - 96) * 4
secretCode = input("Enter secret code : ")
print(bon(secretCode))
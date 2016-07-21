my_list = [1,2,3,4]

for number in my_list:
	print(number)

print ("*********")

my_dict = {"Daniel": "first row", "Sid": "second row", "Zachery": "third row"}
for key in my_dict:
	if my_dict[key] == "first row":
		print("{}, you can go get lunch".format(key))
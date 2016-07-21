def fish_store(red_fish, cat_fish, megladon, magicarp, gyrados):
	#Calculate prices
	red_fish_price = 50 * red_fish
	cat_fish_price = 17 * cat_fish
	megladon_price = 2 * megladon
	magicarp_price = 100 * magicarp
	gyrados_price = .25 * gyrados

	#Calculate totals
	total_price = red_fish_price + cat_fish_price + megladon_price + magicarp_price + gyrados_price
	total_fish = red_fish + cat_fish + megladon + magicarp + gyrados

	#Output price and number of fish to user
	print("You bought {} fish for ${}.".format(total_fish, total_price))

#Call function
fish_store(5, 7, 4, 902, 51) 
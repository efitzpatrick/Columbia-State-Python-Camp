class Pokemon:
	def __init__(self, hp, species, attack, defense, attack1, attack2):
		#Strings
		self.species = species
		#Integers
		self.hp = hp
		self.attack = attack
		self.defense = defense
		#lists -> ["name", power]
		self.attack1_name = attack1[0]
		self.attack2_name = attack2[0]
		self.attack1_power = attack1[1]
		self.attack2_power = attack2[1]

	#Get and Set
	def get_species(self):
		return(self.species)

	def set_species(self, new_species):
		self.species = new_species
		return(self.species)

	def get_hp(self):
		return(self.hp)

	def set_hp(self, new_hp):
		self.hp = new_hp
		return(self.hp)

	def get_attack(self):
		return(self.attack)

	def set_attack(self, new_attack):
		self.attack = new_attack
		return(self.attack)

	def get_defense(self):
		return(self.defense)

	def set_defense(self, new_defense):
		self.defense = new_defense
		return(self.defense)

	#Attacks
	def take_damage(self, amount):
		self.hp = self.hp - amount
		return(self.hp)

	def attack1(self, victim):
		victim_hp = victim.take_damage(self.attack1_power)
		print("Victim's new hp is {}, it went down by {}.".format(victim_hp, self.attack1_power))

	def attack2(self, victim):
		victim_hp = victim.take_damage(self.attack2_power)
		print("Victim's new hp is {}, it went down by {}.".format(victim_hp, self.attack2_power))

infernate = Pokemon(207, "Fire", 175, 75, ["Fireball", 75], ["Flare Blitz", 120])
mewtwo = Pokemon(500, "Psychic", 388, 2, ["Confusion", 50], ["Shadow Ball", 82])

infernate.attack1(mewtwo)
class Ball:
	def __init__(self, color, shape, pattern, size, squish, texture):
		#Characteristics
		self.color = color
		self.shape = shape
		self.pattern = pattern
		self.size = size
		self.squish = squish
		self.texture = texture
		#Positions
		self.posx = 0
		self.posy = 0
		self.posz = 0

	#get/set attribute
	def get_color(self):
		return(self.color)

	def set_color(self, new_color):
		self.color = new_color
		return(self.color)

	def get_shape(self):
		return(self.shape)

	def set_shape(self, new_shape):
		self.shape = new_shape
		return(self.shape)

	def get_pattern(self):
		return(self.pattern)

	def set_pattern(self, new_pattern):
		self.pattern = new_pattern

	def get_size(self):
		return(self.size)

	def set_size(self, new_size):
		self.size = new_size
		return(self.size)

	def get_squish(self):
		return(self.squish)

	def set_squish(self, new_squish):
		self.squish = new_squish
		return(self.squish)

	def get_texture(self):
		return(self.texture)

	def set_texture(self, new_texture):
		self.texture = new_texture
		return(self.texture)

	#actions
	def drop(height):
		self.z = height
		print("The ball is being dropped from {} feet.".format(self.z))
		print("The ball is falling")
		self.z = 0
		print("The ball has hit the ground.")


my_ball = Ball("blue", "round", "zig zag", "small", True, "soft")
print(my_ball.set_color("orange"))
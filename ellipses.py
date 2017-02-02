import random, canvas, time

def coordinates(radius):
	w,h = canvas.get_size()
	x = random.uniform(0,w-radius*2)
	y = random.uniform(0, h-radius*2)
	return x, y

def radius():
	return random.uniform(0, min(*canvas.get_size())/5)

def color():
	r = random.random()
	g = random.random()
	b = random.random()
	return r, g, b

def add_ellipse(x,y,r, color):
	canvas.set_fill_color(*color)
	for alpha in range(256):
		canvas.set_alpha(alpha/256)
		canvas.fill_ellipse(x, y, r*2, r*2)
	

while True :
	c = color()
	r = radius()
	x,y = coordinates(r)
	add_ellipse(x,y,r,c)

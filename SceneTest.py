import scene
import sound
import ui
import random
import motion

class Particle:
  def __init__(self, position, speed, acceleration):
    self.position = position
    self.speed = speed
    self.acceleration = acceleration
   
  def setup(self, Scene): 
    path = ui.Path.oval(0,0,20,20)
    self.node = scene.ShapeNode(path)
    self.node.position = self.position
    self.node.color = (random.uniform(0.5,1), 0, random.uniform(0.5,1), 1)
    Scene.add_child(self.node)
    
  def update(self, bounds, gravity):
    self.acceleration = gravity
    self.position += self.speed
    self.speed += self.acceleration
    self.speed *= 0.99
    self.checkBounds(bounds)
    self.node.position = self.position
  #  print(self.speed, self.acceleration, self.position)
    
  def checkBounds(self, bounds):
    if self.position.x < 0:
      self.position.x = -self.position.x
      self.speed.x = -self.speed.x
    if self.position.x > bounds.x:
      self.position.x -= self.position.x - bounds.x
      self.speed.x = -self.speed.x
    if self.position.y < 0:
      self.position.y = -self.position.y
      self.speed.y = -self.speed.y
    if self.position.y > bounds.y:
      self.position.y -= self.position.y - bounds.y
      self.speed.y = -self.speed.y

N = 0

class MyScene (scene.Scene):
    def setup(self):
      random.seed()
      self.background_color = 'midnightblue'
      self.text = scene.LabelNode("")
      self.text.position = self.size/2
      self.add_child(self.text)
      self.particles = []
      for n in range(N):
        self.addParticle()
      motion.start_updates()
        
    def addParticle(self):
        pos= scene.Point(0,0)
        v = scene.Point(random.uniform(0,5), random.uniform(0,5))
        a = scene.Point(0, -0.03)
        particle = Particle(pos,v,a)
        self.particles.append(particle)
        particle.setup(self)

    def update(self):
      self.text.text = str(len(self.particles))
      (x,y,z) =motion.get_gravity()
      gravity = (-y/10, x/10)
      for particle in self.particles:
        particle.update(self.size, gravity)
      self.addParticle()

scene.run(MyScene(), scene.PORTRAIT, frame_interval = 1, show_fps=True)

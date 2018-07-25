import scene
import ui
import math


class MyScene (scene.Scene):
    def setup(self):
      self.background_color = 'black'
      self.add_circle()
      self.add_lines()
    
    def add_circle(self):
      radius = self.size.height/2
      oval = ui.Path.oval(-radius, -radius, radius, radius)
      node = scene.ShapeNode(path = oval, fill_color = 'none', stroke_color = 'lightblue')
      node.color = 'white'
      node.position = self.size / 2
      self.add_child(node)
      
    def add_lines(self):
      self.lines = []
      point = self.size / 2 + scene.Point(100, 0)
      self.add_child(scene.LabelNode('x', position = point))
      for angle in range(0, 360, 10):
        self.add_line(angle)
        
    def add_line(self, angle):
      p = ui.Path.rect(0,0, 1000, 1)
      line = scene.ShapeNode(p, stroke_color='white', fill_color= 'none')
      line.anchor_point = (0,0)
      line.rotation = math.radians(angle)
      line.position = self.size /2
      self.add_child(line)

    def update(self):
      pass

scene.run(MyScene(), scene.LANDSCAPE, frame_interval = 1, show_fps=True)

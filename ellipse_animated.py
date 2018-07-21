import scene
import ui


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
      
 #     for angle in range(0, 360, 10):
  #      add_line(angle)

    def update(self):
      pass

scene.run(MyScene(), scene.LANDSCAPE, frame_interval = 1, show_fps=True)

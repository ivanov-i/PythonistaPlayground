import numpy as np
import ui


field_size = 3
grass_growing_speed = 0.001
rect_size = 50
window_size = 512


class Field:

  def __init__(self, grass = np.zeros((field_size, field_size), np.double)):
    self.grass = grass

  def grass_grow(self):
    new_grass = self.grass + grass_growing_speed
    return Field(new_grass)

  def for_each(self, func):
    it = np.nditer(self.grass, flags=['multi_index'], op_flags=['readonly'])
    while not it.finished:
      x = it.multi_index[0]
      y = it.multi_index[1]
      value = it[0]
      func(x, y, value)
      it.iternext()


class Screen:

  def __init__(self):
  #       self.ctx = ui.ImageContext(window_size, window_size, window_size/field_size)
    #self.ctx.__enter__()
    pass

  def draw_field(self, field):
    with ui.ImageContext(window_size, window_size, window_size/field_size) as ctx:

      def draw_single_grass(x, y, value):
        red_and_green_color = 1.0 - value
        ui.set_color((red_and_green_color, 1, red_and_green_color))
        oval = ui.Path.oval(x, y, 1/field_size, 1/field_size)
        ui.set_color((red_and_green_color, 1, red_and_green_color))
        oval.fill()

      field.for_each(draw_single_grass)
      img = ctx.get_image()
      img.show()



  def clear(self):
    #       canvas.set_size(*canvas.get_size())
    pass

if __name__ == '__main__':
  s = Screen()
  s.clear()
  f = Field()
  number_of_iterations = int(1/grass_growing_speed)
  for i in range(number_of_iterations):
    s.draw_field(f)
    f = f.grass_grow()


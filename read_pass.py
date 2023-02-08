import settings
import buttons
import surface_pass

from pygame.draw import line
from pygame.font import SysFont
from pygame import Surface
from pygame import MOUSEBUTTONUP


class Main:
	def __init__(self, screen):
		self.screen = screen
		self.surface = Surface((settings.WIDTH, 150))
		self.screen.blit(self.surface, (0, 0))

		self.rect_btn = buttons.Rectangle(self.surface)
		self.surf_pass = surface_pass.Main(screen)
		
		self.font = SysFont(None, 50)
		self.input_txt = self.font.render('Введите платформу', True, settings.TEXT_COLOR)

		self.input_data = buttons.InputBox(250, 95, 500, 32)
		self.input_boxes = [self.input_data]

	def draw(self, pos=None):
		self.surf_pass.draw(pos)
		self.surface.fill(settings.BACKGROWND_COLOR)
		line(self.surface, (128,0,216), (0,149), (settings.WIDTH,149))

		self.rect_btn.draw(x=30, y=20, text='Главная', pos=pos)

		self.surface.blit(self.input_txt, (320, 50))

		for box in self.input_boxes:
			box.draw(self.surface)

		self.input_data.update(data='index')

		self.screen.blit(self.surface, (0, 0))

	def event(self, e, pos):
		self.surf_pass.event(e, pos)
		def exit():
			settings.main = True
			settings.new_pass = False
			settings.read_pass = False
			for box in self.input_boxes:
				box.delete()

		for box in self.input_boxes:
			box.handle_event(e)

		if e.type == MOUSEBUTTONUP:
			if e.button == 1:
				self.rect_btn.click(x=30, y=20, text='Главная', pos=pos, command=exit)

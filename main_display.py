from pygame import Surface
from pygame import MOUSEBUTTONUP

import settings
import buttons


class Main:
	def __init__(self, screen):
		self.screen = screen
		self.surface = Surface((settings.WIDTH, settings.HEIGHT))
		self.screen.blit(self.surface, (0, 0))

		self.rect_btn = buttons.Rectangle(self.surface)

	def draw(self, pos=None):
		self.surface.fill(settings.BACKGROWND_COLOR)

		self.rect_btn.draw(x=320, y=100, text='Добавить пароль', size_font=50, pos=pos)
		self.rect_btn.draw(x=320, y=250, text='Найти пароль', size_font=50, pos=pos)

		self.screen.blit(self.surface, (0, 0))

	def event(self, e, pos):
		def newpass():
			settings.main = False
			settings.new_pass = True
			settings.read_pass = False

		def viewpass():
			settings.main = False
			settings.new_pass = False
			settings.read_pass = True

		if e.type == MOUSEBUTTONUP:
			if e.button == 1:
				self.rect_btn.click(x=320, y=100, text='Добавить пароль', size_font=50, pos=pos, command=newpass)
				self.rect_btn.click(x=320, y=250, text='Найти пароль', size_font=50, pos=pos, command=viewpass)


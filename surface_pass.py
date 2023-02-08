import os
from pygame.draw import line
from pygame.font import SysFont
from pygame import Surface
from pygame import MOUSEBUTTONDOWN

import settings
import buttons
import write_and_read


class Main:
	def __init__(self, screen):
		self.screen = screen
		self.x_surface = settings.WIDTH
		self.y_surface = 350
		self.xpos_surface = 0
		self.ypos_surface = 150
		self.surface = Surface((self.x_surface, self.y_surface))
		self.screen.blit(self.surface, (self.xpos_surface, self.ypos_surface))
		self.read_file = write_and_read.WriteRead()
		self.font = SysFont(None, 35)

	def draw(self, pos=None ):
		self.surface.fill(settings.BACKGROWND_COLOR)

		self.list_files = []
		for root, dirs, files in os.walk("passwords\\"):  
			for filename in files:
				self.list_files.append(filename)
				# print(filename)

		if settings.text_index:
			key=settings.text_index
			xpos, ypos = 10, 10
			for x in range(len(self.list_files)):
				if key.lower() in self.list_files[x].lower():
					self.line_list = self.read_file.read(self.list_files[x])

					for line_data in self.line_list:
						self.data_txt = self.font.render(line_data[:-1], True, settings.TEXT_COLOR)
						self.surface.blit(self.data_txt, (xpos, ypos))
						ypos+=50
						if 'Password:' in line_data[:9]:
							line(self.surface, (128,0,216), (0,ypos-15), (settings.WIDTH,ypos-15), 5)
						if ypos >= self.y_surface:
							self.y_surface += 50
							self.surface = Surface((self.x_surface, self.y_surface))
					

		self.screen.blit(self.surface, (self.xpos_surface, self.ypos_surface))

	def event(self, e, pos):

		if e.type == MOUSEBUTTONDOWN:
			if self.ypos_surface + self.y_surface >= 501:
				if e.button == 5:
					self.ypos_surface -= 25

			if self.ypos_surface <= 149:
				if e.button == 4:
					self.ypos_surface += 25

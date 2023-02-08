import settings
import buttons
import write_and_read

from pygame.font import SysFont
from pygame import Surface
from pygame import MOUSEBUTTONUP


class Main:
	def __init__(self, screen):
		self.screen = screen
		self.surface = Surface((settings.WIDTH, settings.HEIGHT))
		self.screen.blit(self.surface, (0, 0))

		self.rect_btn = buttons.Rectangle(self.surface)
		self.write_file = write_and_read.WriteRead()
		
		self.font = SysFont(None, 50)
		self.platform_txt = self.font.render('Платформа', True, settings.TEXT_COLOR)
		self.mail_txt = self.font.render('электронная почта', True, settings.TEXT_COLOR)
		self.username_txt = self.font.render('Имя пользователя', True, settings.TEXT_COLOR)
		self.password_txt = self.font.render('Пароль', True, settings.TEXT_COLOR)

		self.input_platform = buttons.InputBox(350, 95, 500, 32)
		self.input_email = buttons.InputBox(350, 150, 500, 32)
		self.input_username = buttons.InputBox(350, 205, 500, 32)
		self.input_password = buttons.InputBox(350, 260, 500, 32)
		self.input_boxes = [self.input_platform, self.input_email, self.input_username, self.input_password]

	def draw(self, pos=None):
		self.surface.fill(settings.BACKGROWND_COLOR)

		self.rect_btn.draw(x=30, y=20, text='Главная', pos=pos)
		self.rect_btn.draw(x=280, y=350, text='Сохранить', size_font=50, pos=pos)

		self.surface.blit(self.platform_txt, (10, 100))
		self.surface.blit(self.mail_txt, (10, 155))
		self.surface.blit(self.username_txt, (10, 210))
		self.surface.blit(self.password_txt, (10, 265))
		for box in self.input_boxes:
			box.draw(self.surface)

		self.input_platform.update(data='title')
		self.input_email.update(data='mail')
		self.input_username.update(data='user')
		self.input_password.update(data='pass')

		self.screen.blit(self.surface, (0, 0))

	def event(self, e, pos):
		def exit():
			settings.main = True
			settings.new_pass = False
			settings.read_pass = False
			settings.Title = None
			settings.EMail = None
			settings.UserName = None
			settings.Password = None
			for box in self.input_boxes:
				box.delete()

		def save():
			self.write_file.write()
			settings.Title = None
			settings.EMail = None
			settings.UserName = None
			settings.Password = None
			for box in self.input_boxes:
				box.delete()

		for box in self.input_boxes:
			box.handle_event(e)

		if e.type == MOUSEBUTTONUP:
			if e.button == 1:
				self.rect_btn.click(x=30, y=20, text='Главная', pos=pos, command=exit)
				self.rect_btn.click(x=280, y=350, text='Сохранить', size_font=50, pos=pos, command=save)

import pygame

import settings
import new_pass
import read_pass
import main_display

def main():
	pygame.init()
	screen = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
	pygame.display.set_caption('PassManage')
	# img = pygame.image.load(set_game.icon_window)
	# pygame.display.set_icon(img)
	clock = pygame.time.Clock()

	main = main_display.Main(screen)
	new = new_pass.Main(screen)
	read = read_pass.Main(screen)


	while settings.run:
		screen.fill((0,0,0))
		clock.tick(settings.FPS)

		pos = pygame.mouse.get_pos()

		if settings.main:
			main.draw(pos=pos)
		elif settings.new_pass:
			new.draw(pos=pos)
		elif settings.read_pass:
			read.draw(pos=pos)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				settings.run = False

			if settings.main:
				main.event(e, pos)
			elif settings.new_pass:
				new.event(e,pos)
			elif settings.read_pass:
				read.event(e,pos)

		pygame.display.update()


if __name__ == '__main__':
	main()

pygame.quit()

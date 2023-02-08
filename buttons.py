from pygame.draw import rect, circle, line
from pygame.font import SysFont, Font
from pygame import Rect
from pygame import MOUSEBUTTONDOWN, KEYDOWN, K_RETURN, K_BACKSPACE, KMOD_CTRL, K_v
from pygame import key
import clipboard

import settings


class Rectangle:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, x=None, y=None, length=None, height=30, over_btn=settings.OVER_BTN_COLOR,
             not_over_btn=settings.NOT_OVER_BTN_COLOR, text=None, font=None, size_font=30, pos=None):

        if not length:
            length = x+(size_font/2)

        if not height:
            height = size_font

        font = SysFont(font, size_font)
        txt = font.render(text, True, over_btn)

        text_rect = txt.get_rect(center=(x+length/2, y+height/2))
        if text_rect[0] > x or text_rect[0] < x:
            x = text_rect[0]-2
            length = text_rect[2]+3
        elif text_rect[1] > y or text_rect[1] < y:
            y = text_rect[1]
            height = text_rect[3]
            
        if text_rect[0]<=pos[0]<=text_rect[0]+length and y<=pos[1]<=y+height:
            txt = font.render(text, True, over_btn)

        else:
            txt = font.render(text, True, not_over_btn)

        text_rect = txt.get_rect(center=(x+length/2, y+height/2))
        if text_rect[0] > x or text_rect[0] < x:
            x = text_rect[0]-2
            length = text_rect[2]+3
        elif text_rect[1] > y or text_rect[1] < y:
            y = text_rect[1]
            height = text_rect[3]

        self.screen.blit(txt, text_rect)

    def click(self, x=None, y=None, length=None, height=None, click_color=settings.CLICK_BTN_COLOR,
			  text=None, font=None, size_font=30, color_txt=settings.TEXT_COLOR, pos=None, command=None):

        if not length:
            length = x+(size_font/2)

        if not height:
            height = 30

        font = SysFont(font, size_font)
        txt = font.render(text, True, color_txt)

        text_rect = txt.get_rect(center=(x+length/2, y+height/2))
        if text_rect[0] > x or text_rect[0] < x:
            x = text_rect[0]-2
            length = text_rect[2]+3
        elif text_rect[1] > y or text_rect[1] < y:
            y = text_rect[1]
            height = text_rect[3]
            
        if text_rect[0]<=pos[0]<=text_rect[0]+length and y<=pos[1]<=y+height:
            command()

        self.screen.blit(txt, text_rect)


class InputBox:

    def __init__(self, x, y, w, h, text='', color_txt=settings.TEXT_COLOR, color_rect=settings.INPUTBOX_COLOR, color_inactive=settings.INPUTBOX_INACTIVE_COLOR, font=None, size_font=32):
        self.w = w
        self.FONT = Font(font, size_font)
        self.rect = Rect(x, y, w, h)
        self.color_rect = color_rect
        self.color_inactive = color_inactive
        self.color = self.color_rect
        self.text = text
        self.txt_surface = self.FONT.render(text, True, color_txt)
        self.active = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_rect if self.active else self.color_inactive
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_v:
                    mods = key.get_mods()
                    if mods & KMOD_CTRL:
                        self.text += clipboard.paste()
                elif event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self, data=None):
        # Resize the box if the text is too long.
        width = max(self.w, self.txt_surface.get_width()+10)
        self.rect.w = width

        if data == 'title':
            settings.Title = self.text
        if data == 'mail':
            settings.EMail = self.text
        if data == 'user':
            settings.UserName = self.text
        if data == 'pass':
            settings.Password = self.text
        if data == 'index':
            settings.text_index = self.text

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        rect(screen, self.color, self.rect, 2)

    def delete(self):
        	self.text = ''
        	self.txt_surface = self.FONT.render(self.text, True, self.color)


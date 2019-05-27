import pygame
class Ship():
	def __init__(self,ai_settings,screen):
		self.screen = screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False
	def update(self):
		if self.moving_right:
			self.center +=self.ai_settings.ship_speed_factor
		if self.moving_left:
			self.center -=self.ai_settings.ship_speed_factor
		#update target accordding to self.center
		self.rect.centerx = self.center
	def blitme(self):
		self.screen.blit(self.image, self.rect)

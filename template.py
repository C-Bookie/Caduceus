import threading

import pygame

import connection


class Screen:
	def __init__(self, client):
		self.client = client

		self.height = 300
		self.width = 400

		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))  # , pygame.FULLSCREEN)
		pygame.display.set_caption('template')

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0, 0, 0))

		self.lock = threading.Lock()

	def run(self):
		try:
			while True:
				self.loop()
		finally:
			self.client.close()

	def loop(self):
		events = pygame.event.get()
		self.lock.acquire()
		for event in events:
			if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
				self.client.send_data({
					"type": "broadcast",
					"args": [
						{
							"type": "key",
							"args": [
								event.key,
								event.type == pygame.KEYDOWN
							]
						},
						"show_host"
					]
				})
			if event.type == pygame.QUIT:
				return

		self.screen.blit(self.background, (0, 0))
		self.lock.release()
		pygame.display.flip()


class Template(connection.Client):
	def __init__(self):
		super().__init__()
		self.screen = None
		self.white_list_functions += []

	def connect(self):
		super().connect()
		self.send_data({
			"type": "register",
			"args": [
				"template",
				2077
			]
		})


if __name__ == "__main__":
	tem = Template()
	screen = Screen(tem)
	tem.screen = screen
	tem.start()
	screen.run()


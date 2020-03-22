import os
import time

import connection


class Screen:
	def __init__(self, client):
		self.client = client

	def run(self):
		try:
			while True:
				self.loop()
		finally:
			self.client.close()

	def loop(self):
		self.client.send_data({"type": "get_sessions"})  # todo add node utility functions
		time.sleep(1)


class Template(connection.Client):
	def __init__(self):
		super().__init__()
		self.screen = None
		self.white_list_functions += [
			"session_list"
		]

	def connect(self):
		super().connect()
		self.send_data({
			"type": "register",
			"args": [
				"terminal",
				2077
			]
		})

	def session_list(self, sessions):
		print("Sessions:")
		for session_alias, nodes in sessions.items():
			print("\t" + session_alias)
			i = 0
			for node_alias in nodes:
				print("\t\t" + ("\u251C" if i < len(nodes)-1 else "\u2514") + node_alias)
				i += 1


if __name__ == "__main__":
	tem = Template()
	screen = Screen(tem)
	tem.screen = screen
	tem.start()
	screen.run()


# A python socket manager.

Extend Session for server classes.
Extend Connection for client clasess.
To expose functions to RPC calling, add their name to the white_list_functions list.
To call a function, you can send JSON with the function name and arguments contained:

	{
		"type": "function_name",
		"args": [
			"argument 1",
			"argument 2"
		]
	}

You can register a new connection by sending the clients name and the name of the session they should be moved to:

	{
		"type": "register",
		"args": [
			"client_name",
			"session_name"
		]
	}

To send a message to other clients, you can call the broadcast message using the message and client name:
	
	{
		"type": "broadcast",
		"args": [
			"message",
			"client_name"
		]
	}

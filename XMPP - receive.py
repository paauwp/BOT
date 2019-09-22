from sleekxmpp import ClientXMPP

class ReceiveBot(ClientXMPP):

	def __init__(self, jid, password):
		ClientXMPP.__init__(self, jid, password)

		

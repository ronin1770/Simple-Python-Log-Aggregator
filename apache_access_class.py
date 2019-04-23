import json

class apache_access_class:
	m_clientip   = ""
	m_identity   = ""
	m_user	     = ""
	m_accesstime = ""
	m_request    = ""
	m_statuscode = ""
	m_objectsize = ""
	
	def create_json_string(self):
		jsonArr = { "client_ip" : self.m_clientip, "identity" : self.m_identity, "user" : self.m_user, "accesstime" : self.m_accesstime, "request" : self.m_request, "statuscode" : self.m_statuscode, "objectsize" : self.m_objectsize }
		
		return json.dumps(jsonArr)
		
	def set_object(self, lstAccessLog):
		self.set_clientip(lstAccessLog[0])
		self.set_identity(lstAccessLog[1])
		self.set_user(lstAccessLog[2])
		self.set_accesstime(lstAccessLog[3])
		self.set_request(lstAccessLog[4])
		self.set_statuscode(lstAccessLog[5])
		self.set_objectsize(lstAccessLog[6])
		
	def apache_access_class(self):
		print("Creating apache_access_class object")
		
	def set_clientip(self, clientip): 
		self.m_clientip = clientip
		
	def get_clientip(self):
		return self.m_clientip
		
	def set_identity(self, identity):
		self.m_identity = identity
		
	def get_identity(self):
		return self.m_identity
		
	def set_user(self, user):
		self.m_user = user
		
	def get_user(self):
		return self.m_user
		
	def set_accesstime(self, accesstime):
		self.m_accesstime = accesstime
		
	def get_accesstime(self):
		return self.m_accesstime
		
	def set_request(self, request):
		self.m_request = request
		
	def get_request(self):
		return self.m_request
		
	def set_statuscode(self, statuscode):
		self.m_statuscode = statuscode
		
	def get_statuscode(self):
		return self.m_statuscode
		
	def set_objectsize(self, objectsize):
		self.m_objectsize = objectsize
		
	def get_objectsize(self):
		return self.m_objectsize
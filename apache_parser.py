#Name: apache_parser.py
#Description: This code parses Apache Access and Error logs and produces json string for pushing it to elastic search
# TODO: Use log parser

import os.path
import re
from apache_access_class import *

class apache_parser:
	
	#Name of the apache server/ip_address
	m_server_name = "" 
	
	#Access log location
	m_access_log_location = ""
	
	#Error log location
	m_error_log_location  = ""
	
	#Default constructor
	def apache_parser(self):
		print("Object created")
		
	#method for parsing access log
	def parse_access_log(self, access_log_location):
		self.m_access_location    = access_log_location
		#check if file exists otherwise report error
		if not os.path.isfile(self.m_access_location):
			print ("ERROR: access log is not valid or found at the desired location")
			return
		with open(self.m_access_location) as f:
			line = f.readline()
			while line: #Change it to (while true - for reading file in real time)
				line = f.readline()
				if line:
					aac = apache_access_class()
					aac.set_object( self.chop_access_log(line) )
					print( aac.create_json_string() )
					return
		
	def chop_access_log(self, line):
		return list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))) 
		
		
	#method for parsing error log
	def parse_error_log(self, error_log_location):
		self.m_error_log_location = error_log_location
		#check if file exists otherwise report error
		if not self.m_error_log_location.is_file():
			print ("ERROR: error log is not valid or found at the desired location")
			return
		
if __name__ == "__main__":
	ap = apache_parser();
	
	ap.parse_access_log("access_log")
	
	
	
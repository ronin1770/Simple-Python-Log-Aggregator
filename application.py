### This is the main file
### Execution will start from this file

### We need to know which type of web server is installed
### 1. Apache / Nginx
### 2. Location of access logs
### 3. Location of error logs

### It will start two threads - one for reading access logs and another error logs
### Upon set-up - this will also create an index (name / IP address of the server) on Elastic Search
### types within the index will correspond to either access or error

### Simple log parsing 


"""
with open("/var/log/apache2/access.log") as f:
	while True:
		line = f.readline()
		if line:
			print (line)
"""
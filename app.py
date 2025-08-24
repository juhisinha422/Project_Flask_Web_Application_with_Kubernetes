from flask import Flask

import socket

app = Flask(__name__)

@app.route("/home")
def myhome():
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)
	
	return f"Welcome to my Flask app..., <br> My hostname is : {hostname}, <br>My ip : {IPAddr}  "

app.run(host="0.0.0.0", port=5000)

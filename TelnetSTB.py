#file to connect stb using telnet
import base64
import telnetlib

hostip = "192.168.1.1"
user = "root"

session = telnetlib.Telnet(hsotip)
session.read_until(b"login: ")
session.write(user.encode('ascii')+b"\n")

f = open("test2.py")
a=f.read()
encodedBytes = base64.b64encode(a.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

print(encodedStr)

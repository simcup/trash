import subprocess, time, sys
keystring = "www.google.com"
keylist = []
if len(sys.argv) > 1 and sys.argv[1] != "":
	keystring = sys.argv[1]
for k in keystring:
	if k == ".":
		keylist.append("period")
	elif k == ",":
		keylist.append("comma")
	elif k == " ":
		keylist.append("space")
	else:
		keylist.append(k)
time.sleep(5)
for i in keylist:
	
	subprocess.call(["xdotool", "key", i])
subprocess.call(["xdotool", "key", 'KP_Enter'])

import urllib2
import sys
import xml.etree.ElementTree as et
if len(sys.argv) > 1:
	with open(sys.argv[1], "r") as f:
		opml = et.fromstring(f.read())

	for outline in opml.find("body/outline"):
		a = urllib2.urlopen(outline.get("xmlUrl"))
		try:
			b = et.fromstring(a.read())
			c = b.find("channel/image/url")
			if c != None or False:
				fn = c.text.split("/")[-1]
				img = urllib2.urlopen(c.text)
				with open(fn, "wb") as d:
					d.write(img.read())
		except:
			pass

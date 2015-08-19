import urllib, urllib2, httplib, os, sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	cr, cg, cb, cp, cc, ce	= "\033[91m", "\033[92m", "\033[94m", "\033[95m", "\033[96m", "\033[0m"
	sys.stdout.write("\x1b]2;(*) 4chan downloader by JVM_\x07")
elif _platform == "darwin":
	cr, cg, cb, cp, cc, ce	= "", "", "", "", "", ""
	sys.stdout.write("\x1b]2;(*) 4chan downloader by JVM_\x07")
elif _platform == "win32":
	cr, cg, cb, cp, cc, ce	= "", "", "", "", "", ""
	os.system("title (*) 4chan downloader by JVM_")

print "\n\t-------------------------------------------"
print "\t-        "+cg+"4chan"+ce+" downloader by "+cr+"JVM_"+ce+"        -"
print "\t-                                         -"
print "\t- Linux  : Press Ctrl+Shift+V to paste :) -"
print "\t- Windows: Press Right-Button to paste :) -"
print "\t-------------------------------------------\n\n"
try:
	x=1
	if x == x:
		link	= raw_input("Link: ")
		folder	= raw_input("Download folder: ")

		board	= link.split("/")[3]
		tread	= link.split("/")[5]

		def status(host, path="/"):
		    try:
			conn = httplib.HTTPConnection(host)
			conn.request("HEAD", path)
			return conn.getresponse().status
		    except StandardError:
			return None


		if status("boards.4chan.org", "/"+board+"/res/"+tread) == 200:
			if folder == "":
				folder = board+"-"+tread
			if not os.path.exists(folder+"/"):
				os.makedirs(folder+"/")


			resp = urllib2.urlopen(link)
			data = resp.read()

			title	= (data.split("<title>"))[1].split("</title>")
			img1	= data.split("<a href=\"//images.4chan.org/"+board+"/src/")
			print "\n"+cc+"(*) "+cb+title[0]
			print cc+"(*) "+cb+"Downloading "+str(len(img1)-1)+" images to "+folder+ce+"\n"

			i, done=1, 0
			while not done == 1:	
				#Download (new)images
				while not i == len(img1):
					#Download image
					os.system("title (*) Downloading")
					img2	= img1[i].split("\"")
					img		= "http://images.4chan.org/"+board+"/src/"+img2[0]
					counter	= "("+str(i)+"/"+str(len(img1)-1)+")"
					print cp+counter+"\t"+ce+img
					#Set title: Downloading
					if _platform == "linux" or _platform == "linux2":
						sys.stdout.write("\x1b]2;"+counter+" - Downloading\x07")
					if _platform == "darwin":
						sys.stdout.write("\x1b]2;"+counter+" - Downloading\x07")
					if _platform == "win32":
						os.system("title "+counter+" - Downloading")
					
					file	= folder+"/"+img2[0]
					urllib.urlretrieve (img, file)
					i		+= 1
			
				if i == len(img1):
					#Set title: Done
					if _platform == "linux" or _platform == "linux2":
						sys.stdout.write("\x1b]2;(*) Done - JVM_\x07")
					if _platform == "darwin":
						sys.stdout.write("\x1b]2;(*) Done - JVM_\x07")
					if _platform == "win32":
						os.system("title (*) Done - JVM_")
					
					print cc+"\n(*) "+cb+"I stoped because the tread has no more than "+str(len(img1)-1)+" pic's.\n    Would you like me to check again for new images?"+ce
					repeat	= raw_input("Yes / No: ")
					if repeat == "y" or repeat == "Y" or repeat == "yes" or repeat == "Yes":
						if status("boards.4chan.org", "/"+board+"/res/"+tread) == 200:
							resp = urllib2.urlopen(link)
							data = resp.read()
							img1 = data.split("<a href=\"//images.4chan.org/"+board+"/src/")
							print cc+"\n(*) "+cb+"Found "+cg+str(len(img1)-i)+cb+" new images"+ce
						if status("boards.4chan.org", "/"+board+"/res/"+tread) == 404:
							print "\n"+cr+"Sorry Anon, tread 404d!"+ce
							print cg+"Goodbye!\n"+ce
							done = 1
					
					if repeat == "n" or repeat == "N" or repeat == "no" or repeat == "No":
						done = 1
						print "\n"+cg+"Goodbye Anon!"+ce+"\n"

						
			resp.close()


		if status("boards.4chan.org", "/"+board+"/res/"+tread) == 404:
			print "\n"+cr+"Sorry Anon, tread 404d!"+ce
except:
	print "\n\n"+cr+"Error, "+cg+"Goodbye Anon!\n"+ce

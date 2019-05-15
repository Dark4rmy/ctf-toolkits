
import os,random,sys,time,base64
	
colour=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m']
color=('\033[0;92m')
colo=('\033[0;96m')
normal=('\033[1;m')

#color and time 
c = random.choice(colour) 
n = normal
t= time.sleep(3)

try:
	#bannar display
	def top():
		print('#'*60)

	def topspace():
		for x in range(2):
			print('#'+' '*58+'#')
	
	def msg():
		print('#'+' '*19+random.choice(colour)+' Created by D4rk4rmy'+normal+' '*19+'#')
		print('#'+' '*20+random.choice(colour)+' 	CTF TOOL-KITS '+normal+' '*21+'#')
	def banner():
		top()
		topspace()
		msg()
		topspace()	
		top()
		print(c+'Make sure to ReadMe.md'+n)
	#gobuster
	def go_en():
		print('')
		url= raw_input(c+'['+n+'-'+c+']'+n+"Enter url: ")
		print(random.choice(colour)+'Scan about to begin'+normal)
		a="gobuster -u "+url+" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x sh,txt,php,html,htm,asp,aspx,js,xml,log,json,jpg,jpeg,png,gif,doc,pdf,mpg,mp3,zip,tar.gz,tar"
		b="gobuster -u "+url+" -w /usr/share/wordlists/dirbuster/apache-user-enum-1.0.txt -x sh,txt,php,html,htm,asp,aspx,js,xml,log,json,jpg,jpeg,png,gif,doc,pdf,mpg,mp3,zip,tar.gz,tar"
		os.system(a)
		os.system(b)
	#dirbuster
	def dir_b():
		print('')
		url= raw_input(c+'['+n+'-'+c+']'+n+"Enter url: ")
		print(random.choice(colour)+'Scan about to begin'+normal)
		a="dirb "+url+" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e sh,txt,php,html,htm,asp,aspx,js,xml,log,json,jpg,jpeg,png,gif,doc,pdf,mpg,mp3,zip,tar.gz,tar"
		b="dirb "+url+" -w /usr/share/dirb/wordlists/common.txt -x sh,txt,php,html,htm,asp,aspx,js,xml,log,json,jpg,jpeg,png,gif,doc,pdf,mpg,mp3,zip,tar.gz,tar"
		os.system(a)
		os.system(b)
	#rot13
	def rot_13():
		print('')
		txt= raw_input(c+'['+n+'-'+c+']'+n+"Enter hash: ")
		print(c+'['+n+'+'+c+']'+n+"Decrypted: "+random.choice(colour)+txt.decode('rot13')+normal)
	#base64	
	def base_64():
		print('')
		txt= raw_input(c+'['+n+'-'+c+']'+n+"Enter hash: ")
		print(c+'['+n+'+'+c+']'+n+"Decrypted: "+random.choice(colour)+base64.b64decode(txt)+normal)
	#jpg
	def jp_g():
		print('')
		fiLe=raw_input('Drag jpg image here:')
		t
		print(c+'['+n+'*'+c+']'+n+'working on jpg file now')
		t
		print(c+'['+n+'+'+c+']'+n+'working')
		t
		print('')
		#file
		os.system('file '+fiLe)
		print('')
		#strings
		print(c+'['+n+'+'+c+']'+n+'strings')
		os.system('strings '+fiLe)
		print ('')
		os.system('strings '+fiLe+' | head -n 10') 
		print ('')
		os.system('strings '+fiLe+' | tail -n 10')
		print('')
		#zsteg
		print(c+'['+n+'*'+c+']'+n+'working')
		t
		os.system('zsteg '+fiLe)
		#exif
		print(c+'['+n+'+'+c+']'+n+'grabbing image metadata')
		t
		os.system('exiftool '+fiLe)
		#binwalk
		print(c+'['+n+'+'+c+']'+n+'binwalk')
		t
		print('')
		os.system('binwalk '+fiLe)
		print('')
		#zip extract
		print(c+'['+n+'+'+c+']'+n+'extracting zip')
		t
		print ('')
		os.system('binwalk -Me '+fiLe)
		print(random.choice(colour)+'Possible files extracted. Check folder'+normal)
		print('')
	
	#dd FAT USB	
	def d_d():
		print('')
		fiLe=raw_input('Drag FAT here:')
		t
		print(c+'['+n+'*'+c+']'+n+'working on FAT file now')
		t
		os.system('foremost '+fiLe)
		print(c+'['+n+'+'+c+']'+n+'Output Extracted. Check folder')
		print('')
	#zip
	def zep():
		print('')
		fi=raw_input("Drag file path here:")
		fiLe=fi[1:-2]
		print('')
		print("Crack about to start")
		t
		os.system("fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt "+fiLe)
	#pdf
	def pd_f():
		print('')
		fi=raw_input("Drag file path here:")
		fiLe=fi[1:-2]
		print('')
		print("Crack about to start")
		t
		os.system("pdfcrack -f "+fiLe+" -w /usr/share/wordlists/rockyou.txt")
	#wipe memory
	def wi_pe():
		print('')
		fiLe=raw_input('Drag file to wipe here:')
		t
		print(c+'['+n+'*'+c+']'+n+'wiping clean file now')
		os.system('dcfldd of='+ fiLe +' pattern=00 bs=4096')
		print('wipe complete')
		
		
		
		
	#print bannar
	banner()
	while True:
		print("")
		#selection
		print("		Web Enumeration		")
		print(c+'['+n+'1'+c+']'+n+"Gobuster Enum"+'		'+c+'['+n+'2'+c+']'+n+"Dirbuster Enum\n")
		print("		crypto		")
		print("")
		print(c+'['+n+'3'+c+']'+n+"rot13 decoder"+'			'+c+'['+n+'4'+c+']'+n+"base64 decoder\n")
		print("		stegano		")
		print(c+'['+n+'5'+c+']'+n+"jpeg/jpg/png\n")
		print("		Forensics		")
		print(c+'['+n+'6'+c+']'+n+'dd USB [FAT]'+'			'+c+'['+n+'7'+c+']'+n+"zip crack\n")
		print(c+'['+n+'8'+c+']'+n+'pdf crack\n')
		print("		Wipe Clean		")
		print(c+'['+n+'9'+c+']'+n+"wipe your file\n")
		
		print("")
		#input here
		ask=input(random.choice(colour)+"Choose Decryption Type 0 => exit]:"+normal)
		
		#gobuster
		if (ask == 1):
			go_en()
		#dirbuster
		elif (ask == 2):
			dir_b()
		#rot13
		elif (ask==3):
			rot_13()
		#base64
		elif (ask ==4):
			base_64()
		#image
		elif (ask ==5):
			jp_g()
		#dd USB FAT
		elif (ask ==6):
			d_d()
		#zip
		elif (ask ==7):
			zep()
		#pdf
		elif (ask ==8):
			pd_f()
		#memory wipe
		elif (ask ==9):
			get = raw_input(c+"Are you sure you want to wipe memory [y/n]: "+n)
			if get== 'y':
				wi_pe()
			else:
				break

		elif ask == 0:
			os.system('clear')
			sys.exit()

except KeyboardInterrupt:
	os.system('clear')
	sys.exit()



	

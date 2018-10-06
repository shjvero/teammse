import os, sys, ctypes
import win32com.shell.shell as shell

#eventlog 파일 이름, 전체 경로 수집
objpaths = ["C:\\Windows\\System32\\Winevt\\logs"]

def uac_require():
	asadmin = 'Administrator'
	try:
		if sys.argv[-1] != asadmin:
			script = os.path.abspath(sys.argv[0])
			params = ''.join([script]+sys.argv[1:]+[asadmin])
			shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
		return True
	except Exception:
		print("uac Failed")
		return False

def getDirList(objpath):
	pathisexist = os.path.exists(objpath)
	return pathisexist

def getFullPath(objpath):
	c = 0
	for (path, dirs, files) in os.walk(objpath):
		for f in files:
			if os.path.splitext(f)[-1] == '.evtx' : 
				print(path+"\\"+f)
				print(f)
				c = c+1
			else : 
				pass
	print("\n")
	print("%d files are finded" %c)

	if c==0:
		print("Empty Folder\nNo File Exists\n")
		return False
	return True

if __name__ == '__main__':

	try:
		if ctypes.windll.shell32.IsUserAnAdmin():

			for i in objpaths:
				if getDirList(i):
					print(i+" Exist the Folder\n")
					getFullPath(i)
				else:
					print(i+" is Failed\n")
		else:
			print("\nPlease Excute Administrator")			

	except Exception as e:
		print(e)
		print("\n Please Excute Administrator")


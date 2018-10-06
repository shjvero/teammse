import os, sys, ctypes
import win32com.shell.shell as shell


def uac_require():
	asadmin = 'Administrator'
	try:
		if sys.argv[-1] != asadmin:
			script = os.path.abspath(sys.argv[0])
			params = ''.join([script]+sys.argv[1:]+[asadmin])
			shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
			#print(ctypes.windll.shell32.IsUserAnAdmin())
			#sys.exit()
		return True
	except Exception:
		print("uac Failed")
		return False

def getDirList(werpath):
	pathisexist = os.path.exists(werpath)
	return pathisexist

def getFullPath(werpath):
	c = 0
	for (path, dirs, files) in os.walk(werpath):
		for f in files:
			print(path+"\\"+f)
			if os.path.splitext(f)[-1] != '.wer':
				print(f)
			else:
				print(path.split("\\")[-1])
			c = c+1
	print("\n")
	if c==0:
		print("Not Exists Wer Files\nEmpty Folder\n")
		return False
	return True

		#파일 폴더명이랑 wer파일 풀패스 가져오기

		#만약에 시간이 되면 wer 파일 읽어서 폴더명으로 wer 이름 바꿔서 저장하기.

if __name__ == '__main__':


	try:
		if ctypes.windll.shell32.IsUserAnAdmin():
			werpaths = ["C:\\ProgramData\\Microsoft\\Windows\\WER", "C:\\Users\\vero\\AppData\\Local\\Microsoft\\Windows\\WER", "C:\\$WINDOWS.~BT\\Sources\\Rollback\\WER"]
			#werpaths = ["C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportArchive"]

			
			for i in werpaths:
				if getDirList(i):
					print(i+" Exist the Wer Folder\n")
					getFullPath(i)
				else:
					print(i+" is Failed\n")
		else:
			print("\nPlease Excute Administrator")			

	except Exception as e:
		print(e)
		print("\n Please Excute Administrator")


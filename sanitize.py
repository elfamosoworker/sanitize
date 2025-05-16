import subprocess


text = str(input("url : "))  #l'url qu'on veut sanitize
modified = text.replace('.', '[.]')  #l'url qu'on modifie

cmd='echo '+modified.strip()+'|clip'
subprocess.check_call(cmd, shell=True)


#pyinstaller --clean
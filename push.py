import os
import sys

commit_message = " ".join(sys.argv[1:]) or "Auto_Commit"

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push -u origin master")
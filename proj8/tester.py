import subprocess
from subprocess import PIPE

Cproc = subprocess.Popen("./tester", stdin = PIPE, stdout = PIPE, stderr = PIPE, universal_newlines = True)
MIPSproc = subprocess.Popen(['java', '-jar', 'mars.jar', 'out.asm'], stdin = PIPE, stdout = PIPE, stderr = PIPE, universal_newlines = True)

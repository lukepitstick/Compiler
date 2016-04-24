import os
from compiler import compiler
import subprocess
from traceback import print_exc

projtestfilename = "proj%dtester/test.%d.%d.ml"
testcases = {"proj5":[5,14,6,3,4],
             "proj6":[11,5,6,5,6,12,1,7,9,1,6],
             "proj7":range(1,7),
             "tester":[4,9,3,3]}
tokfile = 'tokens.txt'
outfile = 'outputdump/out%d.asm'
mars = ['java', '-jar', '../mars.jar']
pycall = '/usr/bin/python3'
testfile = 'test.%d.%d.ml'

if __name__ == "__main__":
    mode = "tester"
    j = 0
    projid = 0
    if mode == 'proj7':
        pass
    elif mode == 'tester':
        for first in range(1, testcases[mode][0]):
            for second in range(1, testcases[mode][first]):
                print("Test %d %d" % (first, second))
                args = testfile % (first, second)
                output = outfile % j
                try:
                    arglst = [pycall, 'compiler.py', '-t', tokfile, args, output]
                    subprocess.call(arglst)
                except Exception:
                    print_exc()
                execute = list(mars)
                execute.append(output)
                subprocess.call(execute)
                j += 1
    else:
        projid = int(mode[-1])
        for first in range(1, testcases[mode][0]):
            for second in range(1, testcases[mode][first]):
                print("Test %d %d" % (first, second))
                args = projtestfilename % (projid, first, second)
                output = outfile % j
                try:
                    arglst = [pycall, 'compiler.py', '-t', tokfile, args, output]
                    subprocess.call(arglst)
                except Exception:
                    print_exc()
                execute = list(mars)
                execute.append(output)
                subprocess.call(execute)
                j += 1
                input("Press <ENTER> to continue")

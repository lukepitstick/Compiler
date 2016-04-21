from compiler import compiler
import subprocess
from traceback import print_exc

projtestfilename = "proj%dtester/test.%d.%d.ml"
testcases = {"proj5":[5,14,6,3,4],
             "proj6":[11,5,6,5,6,12,1,7,9,1,6],
             "proj7":range(1,7)}
tokfile = 'tokens.txt'
outfile = 'outputdump/out%d.asm'
mars = 'java -jar ../mars.jar '

if __name__ == "__main__":
    mode = "proj6"
    j = 0
    projid = 0
    if mode == 'proj7':
        pass
    else:
        projid = int(mode[-1])
        for first in range(1, testcases[mode][0]):
            for second in range(1, testcases[mode][first]):
                print("Test %d %d" % (first, second))
                args = projtestfilename % (projid, first, second)
                output = outfile % j
                passfail = False
                try:
                    passfail = compiler(args, tokfile, output)
                except Exception:
                    print_exc()
                if passfail:
                    execute = mars + output
                    subprocess.call(execute)
                    j += 1
                input("Press <ENTER> to continue")

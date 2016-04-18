from compiler import compiler
import subprocess
from traceback import print_exc

test1 = range(1,4)
tesr2 = range(

if __name__ == "__main__":
    mode = "proj6"
    j = 0
    if mode == "proj6"
        print("Test 1")
        for i in test1:
            filename = "proj6tester/test.1.%d.ml" % i
            ofile = 'outputdumper/out%d.asm' % j
            try:
                compiler(filename, 'tokens.txt', ofile)
            except Exception:
                print_exc()
            oargs = 'java -jar ../mars.jar ' + ofile
            subprocess.call(oargs)
            j += 1
            input()
        
        print("Test 2")
        for i in test2:
            filename = "proj6tester/test.2.%d.ml" % i
            ofile = 'outputdumper/out%d.asm' % j
            try:
                compiler(filename, 'tokens.txt', ofile)
            except Exception:
                print_exc()
            oargs = 'java -jar ../mars.jar ' + ofile
            subprocess.call(oargs)
            j += 1
            input()

        print("Test 3")
        for i in test3:
            filename = "proj6tester/test.3.%d.ml" % i
            ofile = 'outputdumper/out%d.asm' % j
            try:
                compiler(filename, 'tokens.txt', ofile)
            except Exception:
                print_exc()
            oargs = 'java -jar ../mars.jar ' + ofile
            subprocess.call(oargs)
            j += 1
            input()

        print("Test 4")
        for i in test4:
            filename = "proj6tester/test.4.%d.ml" % i
            ofile = 'outputdumper/out%d.asm' % j
            try:
                compiler(filename, 'tokens.txt', ofile)
            except Exception:
                print_exc()
            oargs = 'java -jar ../mars.jar ' + ofile
            subprocess.call(oargs)
            j += 1
            input()

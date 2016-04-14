from compiler import compiler
import subprocess
from traceback import print_exc

expl = range(1, 7)
test1 = range(1, 14)
test2 = range(1, 6)
test3 = range(1, 3)
test4 = range(1, 4)

if __name__ == "__main__":
    mode = "proj6"
    j = 0
    if mode == "example":
        for i in expl:
            filename = "example%d.txt" % i
            ofile = "out%d.asm" % j
            try:
                compiler(filename, 'tokens.txt', ofile)
            except Exception:
                print_exc()
            oargs = 'java -jar ../mars.jar ' + ofile
            subprocess.call(oargs)
            j += 1
            input("Press enter to continue...")
            
    elif mode == "proj5":
        pass
    else:
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
            input("Press enter to continue...")
        
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
            input("Press enter to continue...")

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
            input("Press enter to continue...")

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
            input("Press enter to continue...")

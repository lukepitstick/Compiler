import sys
from os import system
import traceback
from codegenerator import CompilerError

argv = 'java -jar mars.jar '
POSIX = 'python3 compiler.py -t tokens.txt '
WIN32 = 'python compiler.py -t tokens.txt '

class TestError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def compileTest(source, outfile, testtype = True):
    global POSIX
    global WIN32

    ccommand = ''
    
    if sys.platform.startswith('win'):
        ccommand = WIN32
    else:
        ccommand = POSIX
    ccommand += source + ' ' + outfile

    k = system(ccommand)
    if testtype:
        assert(k == 0)
        print("'%s' successfully compiled into '%s'." % (str(source), str(outfile)))
    else:
        assert(k != 0)
        return False
    
    return True

def runTest(argstr):
    global argv

    argstr = argv + argstr
    k = system(argstr)
    if (k != 0):
        raise TestError('Test failed due to interanl error')

    pass

if __name__ == "__main__":
    # global argv
    # global WIN32

    if sys.platform.startswith('win'):
        test = system('python hello.py')
        if (test != 0):
            print('If you see the message above, the program will automatically finds where Python interpreter is.')
            WIN32 = 'C:\\Python34\\' + WIN32

    good = 0
    bad = 0
    error = 0

    goodbad = 0
    badbad = 0
    errbad = 0
    
    print('Test for good..')
    for i in range(1, 16):#15):
        try:
            print('Test ' + str(i))
            source = 'sample' + str(i) + '.txt'
            outfile = 'out' + str(i) + '.asm'
            compileTest(source, outfile)
            runTest(outfile)
            print('...ok')
            good += 1
            pass
        except AssertionError:
            print('>>> traceback <<<')
            traceback.print_exc()
            print('>>> end of traceback <<<')
            print('...FAIL')
            bad += 1
            pass
        except Exception:
            print('>>> traceback <<<')
            traceback.print_exc()
            print('>>> end of traceback <<<')
            print('...ERROR')
            error += 1
            pass

    print('\n\n==================================')
    print('\n\nTest for bad..')
    for i in range(1, 8):#15):
        try:
            print('Test ' + str(i))
            source = 'semanticerror' + str(i) + '.txt'
            outfile = 'outerr' + str(i) + '.asm'
            compileTest(source, outfile, False)
            print('...ok')
            goodbad += 1
            pass
        except AssertionError:
            traceback.print_exc()
            print('...FAIL')
            badbad += 1
            pass
        except Exception:
            print('>>> traceback <<<')
            traceback.print_exc()
            print('>>> end of traceback <<<')
            print('...ERROR')
            errbad += 1
            pass
        

    print('================= Summary of result =================')
    print('Test for good:')
    print('PASS: ' + str(good))
    print('FAIL: ' + str(bad))
    print('ERROR: ' + str(error))
    print('\n')
    print('Test for bad:')
    print('PASS: ' + str(goodbad))
    print('FAIL: ' + str(badbad))
    print('ERROR: ' + str(errbad))
    
    input('Press enter to continue...')

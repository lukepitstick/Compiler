REMEMBER: MLparser.py (except dict) and lexer_sol.py SHOULD NEVER BE TOUCHED!!

Few things to know:
1. We should never tamper with MLparser.py file at this point.
(But some amendments should be done for 'dict' only)
(No other code should be changed)
2. We have to make another module, for example called 'codegenerator.py' to handle the code generation independently from compiler.py file. The 'compiler.py' file only gets the argument and prints out.
3. One more thing I forgot to mention, we need traverse function which traverses all the nodes in the tree. We hit the tree, look at the corresponding pattern, and generate the code. We should not touch the tree structure itself or how it represents.


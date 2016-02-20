# Project 3: Parsing a Language
Implement a parsing algorithm for our micro-language, as specified below.

## Detailed Description
 The initial token set and grammar for our language are given below; these will be augmented later.   Your parsing code should be encapsulated in a library with an interface that, when invoked on a file, verifies if the file is syntactically correct. (At this point, all we are doing is verify syntactical correctness -- but keep in mind in your design that that will change later.) You may halt of the first error found, but error messages should be informative -- including file line numbers.
 
### Other requirements, details, and comments:
* We will be augmenting the grammar in future assignments, so design with an eye to being able to augment your parsing algorithm. (You may assume that you will be dealing with an LL(1) language the entire project – so you can safely employ an LL(1) parsing algorithm without requiring major revisions later.)
* For your sanity, encapsulation is important. Your lexical analyzer deals with tokenization; your parser parses. Do not mix them or you will regret it later.
* The standard convention is to name your functions or methods after the non-terminal (e.g. having a program function for applying program productions, a statement_list function for applying statement list productions, etc…). This convention exists for a good reason – it is strongly recommended that you follow it.

The grammar for the language looks like this:

    <program>	→	begin <statement list> end
    <statement list>	→	<statement>; { <statement>; }
    <statement>	→	<assignment>
    read( <id list> ) |
    write( <expr list> )
    <assignment>	→	<ident> := <expression>
    <id list>	→	<ident> {, <ident>}
    <expr list>	→	<expression> {, <expression> }
    <expression>	→	<primary> {<arith op> <primary> }
    <primary>	→	( <epxerssion> ) | <ident> | INTLITERAL
    <ident>	→	ID  (that is, an ID token)
    <arith op>	→	+ | -

## Submission
Your group submission is the committed content of the part3 directory of your group repository as of the deadline.   All source code and files needed for compilation must be in (or under) that directory.

* Your final submission should be in a sub-directory called MLparser. The (unmodified) parser_tester.py and parser_tester2.py files should be in that directory, and I should be able to run them in that directory and see that you pass all tests.
* Your final submission should be tagged parser.  (The timestamp on this tag will be used as the time of submission.)
* You must put all names of the member of the group at the top of the MLparser.py file.

## Grading
Grading of this project is based on unit-testing.  The unit tests provided to you are not guaranteed to be comprehensive, but they should be fairly complete.  You will be penalized if your code is excessively slow, and will receive a 0 if the program does not run.

## Extra credit
And group who can demonstrate to me code that passes all unit tests but is still wrong in some way will receive 5 points extra credit on the assignment.

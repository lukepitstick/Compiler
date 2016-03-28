# Overview
In this lab you will modify your lexer (or tokens file), parser, and code generator to add several new variables types, new operators, and static type declarations. With the expanded language you will also need to start enforcing new static semantic rules that are not reflected in the.

# Detailed Description
In the following is a description of how we are augmenting the micro-language. You will need to augment the token definitions and language grammar, and modify your lexer, parser, and code generator to compile any program correctly written in this new, modified language. In addition to lexical and syntactic errors, new semantic errors are now possible (probably caught during code-generation). Semantic errors that can be caught at compile time should result in an appropriate error message (nd the halting of the compiler.

# For this assignment
* Add C-like variable declarations to your language.
  * Make the micro-language statically typed by requiring variable declarations for all variables. You will need modify your syntax to allow for the declaration, but ensuring that a variable is declared before it is used is a semantic issue.
  * Add a bool type.
  * bool literals should be called True and False (note capitalization).
  * This should allow for both bool-typed variables and bool literals.  The built in write function should be able to print a Boolean value; the read function does not have to be able to take Booleans as arguments.
* Add a string type.
  * Strings will be static – the length of a string must be known at compile time.
  * This should allow for both string-typed variables and string literals.
  * No operators will be defined on strings, nor will the built-in read (The write function will work with strings.)
* Add the following operators:
  * Remainder: operates on integers.
  * multiplication, integer division: operates on integers.
  * unary negation (e.g. “-x”)
  * Numerical relational operators (equal, not-equal, less-than, less-than-equal, greater-than, greater-than-equal): operates on integers.  Uses the standard Java symbols (< , <=, ==, etc...)
  * Boolean operators (and, or, not): operates on bools.

The grammar should enforce standard precedence and associative rules on the operators (both for the integer and Boolean operators), and allow for parenthesized expressions. Hence your compiler should be able to correctly calculate both x+y*z and (x+y)*z.

Note the following semantic rules:
* The micro-language is statically typed. A variable name cannot be used before it is declared, nor can it be declared twice[1].
* The micro-language is strongly typed. No type coercion or implicit type casting (see below exception for 574 submissions).
* The arithmetic operators are only defined on int types; the boolean operators are only defined on bool types.  Any type mismath (e.g. 5 or 7, or True + False) should result in a semantic error.
* The read function cannot take string or a bool as an argument.
* The write function should be able to take int, string, and bool types as arguments.

~CSE 574 only (not for us):~
~Your variable declarations should allow for (optional) initialization for all types (e.g. “int x := 10;”) Add a (32-bit) float type and float literal, and make it work with all arithmetic operators, relational operators, and the read and write Allow for mixed-type arithmetic expressions, implicitly casting int to float when necessary.~

# Submission
Standard submission instructions, using part6 for both directory and tag name. 

# Sample
Here are a few sample programs you should be able to compile:

    begin
    string s := "I never could get the hang of Thursdays.";
    string s2 := s;
    write(s2);
    end


    begin
    write(5*6/2);
    write(6/2*5);
    end


    begin
    write(True or True);
    write(True and False);
    write(False or True);
    write(False and False);
    end


    begin
    write(5 >= 10);
    write(5 <= 10);
    write(5 == 10);
    end


    begin
    int x;
    int y;
    int z;
    x := 1;
    y := 2;
    z := 3;
    write ( (x+y)*z );
    end


[1] We will need to change this later to account for scope. But since we have not defined any notion of scope, that’s not yet an issue.
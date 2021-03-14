# C compiler
---


### Implemented features:
---
### project 1:
---

##### Mandatory

* [x] Binary operations +, -, *, and /. 
* [ ] Binary operations >, <, and ==. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (soon)
* [x] Unary operators + and -.
* [x] Brackets to overwrite the order of operations.
* [x] Abstract Syntax Tree
* [x] Dot visualization

##### Optional

* [x]  Binary operator %.
* [ ]  Comparison operators >=, <=, and !=.
* [ ]  Logical operators &&, ||, and !.
* [x] Constant Folding

### project 2:
---
##### Mandatory
* [x] Types (int, char, float, pointers).
* [x] Reserved words: const and types
* [x] Variables
* [x] Pointer Operations
* [x] Syntax Errors
* [x] Semantic Errors (line number does not print)

##### Optional
* [ ] Identifier Operations
* [x] Implicit conversions

### project 3:
---
##### Mandatory
* [x] Support for single line comments and multiline comments.
* [ ] Printf. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (soon)
* [x] LLVM code generation &nbsp;&nbsp; (for the most part)
    * we still need to implement poiter support, printf() and fix some small problems like information loss when adding int with float.     

#### how to run:
---
To create the GrammarLexer, GrammarParser, GrammarListener,... This uses Python2.
```
./build.sh
```
then run
``` 
python main.py input1.c
```
If input.c code is valid This should create:
* A png file in the root directory named treeGraph.png that contains the dot visualization of our abstract syntax tree.
* A ll file that contins the generated llvm code. 

Otherwise an error should be thrown (syntax or semantics)
### Tests
---
The tests are written in the directory testInputs.
* input1.c
    * declarations
* input2.c
    * definitions
* input3.c
    * assignments (+ operations with variables)

All these tests are made to compare the generated llvm code output with the output we expected it to generate.
to run the tests:
```
./test.sh
```
# C compiler
---

Compiler for a subset of C into LLVM/MIPS
### Implemented features:
---
### Project 1:
---

##### Mandatory

* [x] Binary operations +, -, *, and /. 
* [x] Binary operations >, <, and ==. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
* [x] Unary operators + and -.
* [x] Brackets to overwrite the order of operations.
* [x] Abstract Syntax Tree
* [x] Dot visualization

##### Optional

* [x]  Binary operator %.
* [x]  Comparison operators >=, <=, and !=.
* [ ]  Logical operators &&, ||, and !.
* [x] Constant Folding

### Project 2:
---
##### Mandatory
* [x] Types (int, char, float, pointers).
* [x] Reserved words: const and types
* [x] Variables
* [ ] Pointer Operations
* [x] Syntax Errors
* [x] Semantic Errors (line number does not print)

##### Optional
* [ ] Identifier Operations
* [x] Implicit conversions

### Project 3:
---
##### Mandatory
* [x] Support for single line comments and multiline comments.
* [x] Printf.
* [x] LLVM code generation &nbsp;&nbsp;

### Project 4:
---
##### Mandatory
* [x] reserved words (if, else, while, for, break, continue)
* [x] scopes (global, loops, unnamed)

##### Optional
* [ ] reserved words (switch, case, default)

### Project 5:
---
##### Mandatory
* [x] reserved words (return, void)
* [x] scopes (functions)
* [x] local and global variables
* [x] functions (only definition)
* [x] unreachable code and dead code

##### Optional
* [ ] return path

### project 6:
---
##### Mandatory
* [x] arrays
* [x] import studio.h

##### Optional
* [ ] multy dimensional and dynamic arrays

#### How to run:
---
To create the GrammarLexer, GrammarParser, GrammarListener,... This uses Python2.
```bash
./build.sh
```
then run

LLVM:
``` bash
python llvm main.py input1.c llvm.ll
```
MIPS:
``` bash
python mips main.py input1.c mips.asm
```
If input.c code is valid This should create:
* A png file in the root directory named treeGraph.png that contains the dot visualization of our Abstract Syntax Tree.
* A llvm/asm  file that contains the generated llvm/mips code. 

Otherwise an error should be thrown (syntax or semantics)

### Tests
---
The test inputs are written in the directory testInputs.
* input1.c
    * declarations
* input2.c
    * definitions
* input3.c
    * assignments (+ operations with variables)

All these tests are made to compare the generated llvm/mips output with the expected output.
To run the tests:
```bash
./test.sh
```

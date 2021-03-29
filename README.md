# Reverse Polish Notation Calculator

David Warshaw

david.warshaw@gmail.com

https://www.davidwarshaw.com

### Installation

Python 3 is required.

```
tar -zxvf rpn.tar.gz
cd rpn-package
python setup.py install
```

### Usage

Launch in interactive mode. Exit with ctrl-d or \'exit\':

```
rpn
```

Evaluate expression from command line, outputting top stack operand:

```
rpn [expression]
```

Evaluate expression from each line of stdin, outputting top stack operand:

```
cat expressions.list | rpn
```

Print the help screen:

```
rpn --help
```

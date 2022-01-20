## Notes on MYPY library

Unlike Java and C++. Python is a dynamically typed language meaning you do not need to specify the typo of objects in run time. 

Mypy is a static type checker for Python. Thus, if you sprinkle your code with type annotations, mypy can type check your code and find common bugs. 

- run mypy with particular program: 
```
mypy tutorial.py
```
This command makes mypy type check your tutorial.py file and print out any errors it finds. Mypy will type check your code statically: this means that it will check for errors without ever running your code, just like a linter.

- You must add type annotations to your code to take full advantage of mypy. By default, mypy will not type check dynamically typed functions. This means that with a few exceptions, mypy will not report any errors with regular unannotated Python.

- to force annotation on all variables run: 
```
mypy tutorial.py --disallow-untyped-defs
```

- You run mypy on your codebase like a linter, and it reports errors in a nice compiler-style format.

- If you’re curious how to annotate something, check out the mypy syntax cheat [sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet.html)

- Static type annotations improve readability

- You can also use a mypy configuration file, which is convenient if there are a large number of errors to ignore. Then run:
```
mypy --config-file mypy.ini tutorial.py
```
 
### Questions
- why do I have error when importing pandas?

- do you have existing codebase without many type annotations

- cts integration with mypy, how?
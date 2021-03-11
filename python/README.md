## Python Note

### List
List Comprehensions - One line for loop

`value_list = [1, 2, 3, 4, 5]`

`value_list_modified = [2*value for value in x if value % 2 == 1]`

Remove first element of the list

`x = [1, 2, 3]`

`x.pop(0)`

Insert value to the first element of the list

`x = [1, 2, 3]`

`val = 0`

`x.insert(0, val)`


### Running shell with Python

`subprocess.call("cd SOME_DIRECTORY_PATH")` will not work!!
You will have to use `os.chdir("SOME_DIRECTORY_PATH")` or some other methods such as subprocess.Popen,
subprocess.call ,etc. In short, using bash shell is much easier but limited operarations. Using Python will allow more complex operarations but more complexities in code.

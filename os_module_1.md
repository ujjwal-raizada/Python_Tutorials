# Part 1: Python OS Module (import os)

The OS module in Python provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.

Lets see features of this module:

## 1. To find the current directory we are in.

```
print(os.getcwd())  # getcwd: get Current Working Directory
```

## 2. To change your current working directory
```
os.chdir('dir1')  # chdir: change Directory
print(os.getcwd())
```

## 3. Listing all files and directories in current directory (cwd).
```
print(os.listdir())  # listdir: List Directory
```

## 4. Create a new Directory
```
os.mkdir("hello_python")  # mkdir: Make Directory
os.makedirs("hello/python")
```

**Note:**

 makedirs() creates all the intermediate directories if they don't exist (just like mkdir -p in bash).

 mkdir() can create a single sub-directory,
         and will throw an exception if intermediate directories that don't exist are specified.

 Either can be used to create a single 'leaf' directory (dirA):

     os.mkdir('dirA')
     os.makedirs('dirA')

 But makedirs must be used to create 'branches':

     os.makedirs('dirA/dirB') will work [the entire structure is created]

 mkdir can work here if dirA already exists, but if it doesn't an error will be thrown.

 Note that unlike mkdir -p in bash, either will throw an error if the leaf already exists.

 In Python3, os.makedirs has a default parameter exist_ok=False.
 If you set it to True, then os.makedirs will not throw any exception if the leaf exists.
 (While os.mkdir doesn't have this parameter.)

 Just like this:
```
os.makedirs('dirA', exist_ok=True)
```
## 5. Delete a directory
```
os.rmdir("hello_python")  # rmdir: remove directory
os.removedirs("hello/python")
```
**Note:** rmdir will not remove intermediate directories but removedirs will.


## 6. Rename a file
```
syntax: os.rename(<older name>, <new name>)
os.rename('test.txt', 'demo.txt')
```

## 7. Details of a file

```
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_mtime)  # Modified time-stamp
```
<br>

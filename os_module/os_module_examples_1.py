import os

print("Example 1")
# 1 to find the current directory we are in.

print(os.getcwd())  # getcwd: get Current Working Directory

print("Example 2")
# 2 To change your current working directory

os.chdir('dir1')  # chdir: change Directory
print(os.getcwd())

print("Example 3")
# 3  Listing all files and directories in current directory (cwd).

print(os.listdir())  # listdir: List Directory

print("Example 4")
# 4 Create a new Directory

os.mkdir("hello_python")  # mkdir: Make Directory
os.makedirs("hello/python")

# Note:

# makedirs() creates all the intermediate directories if they don't exist (just like mkdir -p in bash).

# mkdir() can create a single sub-directory,
#         and will throw an exception if intermediate directories that don't exist are specified.

# Either can be used to create a single 'leaf' directory (dirA):

#     os.mkdir('dirA')
#     os.makedirs('dirA')

# But makedirs must be used to create 'branches':

#     os.makedirs('dirA/dirB') will work [the entire structure is created]

# mkdir can work here if dirA already exists, but if it doesn't an error will be thrown.

# Note that unlike mkdir -p in bash, either will throw an error if the leaf already exists.

# In Python3, os.makedirs has a default parameter exist_ok=False.
# If you set it to True, then os.makedirs will not throw any exception if the leaf exists.
# (While os.mkdir doesn't have this parameter.)

# Just like this:

# os.makedirs('dirA', exist_ok=True)


print("Example 5")
# 5 Delete a directory

os.rmdir("hello_python")  # rmdir: remove directory
os.removedirs("hello/python")

# Note: rmdir will not remove intermediate directories but removedirs will.

print("Example 6")
# 6 rename a file

# syntax: os.rename(<older name>, <new name>)
os.rename('test.txt', 'demo.txt')

print("Example 7")
# 7 Details of a file

print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_mtime)  # Modified time-stamp

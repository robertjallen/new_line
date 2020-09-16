"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

from git import Repo,remote

rw_dir = '\new_line_generator'
repo = Repo(rw_dir)

new_line = "This new line will be added.\n"

with open("bar.txt", "a") as a_file:
  a_file.write("\n")
  a_file.write(new_line)

'''Enter code to commit the repository here.
After commit run the following code to push the commit to remote repo.
I am pushing to master branch here'''

origin = repo.remote(name='origin')
origin.push()






# add_line()
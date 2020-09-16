# add new line
from datetime import datetime
now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

new_line = "This new line will be added.\n"

with open("lines.txt", "a") as a_file:
  a_file.write("\n")
  a_file.write(date_time)





# commit and push

from git import Repo

PATH_OF_GIT_REPO = 'https://github.com/robertjallen/new_line.git' 

COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()

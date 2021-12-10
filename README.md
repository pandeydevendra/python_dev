steps to setup virtual environment::

virtualenv -p python3.6 venv

source venv/bin/activate 

pip install -r requirements.txt

## After every restart
ssh-add ~/.ssh/dev_git
 
# updated on 16/9/21:

Install python, pip package

create virtualenv, activate virtualenv

virtualenv venv 

env=>  name of venv

(linux/unix)

source  venv/bin/activate 

(windows)

source venv/Scripts/activate

git working:-

create new branch from dev branch,
    new branch name should reflect your work,
        like .. pandas_ex_1
make your changes in new branch,
raise pull request from new branch to dev

now merge dev branch into main

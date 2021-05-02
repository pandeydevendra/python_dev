local pc

STEP 1
git status
git checkout dev
git pull origin dev
git checkout master
git pull origin master
git checkout dev
git merge master

-------------

naya code in dev
----------
git add -A OR git add -p OR git add filename
git commit -m "message you want to put"
git push origin dev


----
create a PR => Pull request (github)

merge code
---------

local pc

git status
REPEAT step1

make single commit:

git checkout main 
git pull origin main
git checkout dev
git pull origin dev
git rebase -i origin/main
git push origin -f dev
=== for 1 commit in PR =====


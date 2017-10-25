# CHEAT SHEETS

## ADDING ENVIORNMENT VARIABLES
```pwd
ls-a
nano .bash_profile
source ~/.bash_profile
printenv```

## GIT COMMANDS
```
git commit -m 'my notes' path/to/my/file.ext, 
git status
git push
git stash

git pull [remote] [branch] [branch]
git pull upstream develop master
```

**For a list of files to be pushed, run:**
```git diff --stat --cached [remote/branch]```
example:
```git diff --stat --cached origin/master```

**For the code diff of the files to be pushed, run:**
```git diff [remote repo/branch]```
To see full file paths of the files that will change, run:
```git diff --numstat [remote repo/branch]```

## GIT WORKFLOW
### Pushing to Personal Repo
1.	Commit to local Repo on the development branch
``` git commit -m 'my notes' path/to/my/file.ext ```

2.	Check local Repo git status to ensure all files have been committed
git status

3.	Push to development branch on Origin (in repo Personal/Skyze )
git push

### Pushing to Organizational Repo (Pull Request)
1.	From Personal/Skyze Repo: Send a pull request to Skyze Org Repo on development branch
www.github/ … personal repo URL

2.	Admins: Process the pull request in Skyze Org Repo
https://github.com/SkyzeTrading/Skyze/pulls

Questions … when to Push to Master on personal and on organizational?

### Before Pushing to organisational repo
When doing a Pull Request from github.com/PERSONAL/skypz to github.com/skypeTrading/skypz

Do the following commands in this order:
```
git pull upstream develop master

#check git status for any issues
git status

# Fit any merge issues, and re-run test suite.
# Commit any changes

# Then (pushes to mikenew/origin)
git push origin develop master

# Pull request in gitbut from personal to to Skyze repo
RUN FROM SHELL
```

## GIT Stuff

```git log``` ..... look at the last few commits

### GIT stash
https://www.tutorialspoint.com/git/git_stash_operation.htm
```git stash```

`git stash list`

`git stash pop`

## Removing confidential files from GIT

https://help.github.com/articles/removing-sensitive-data-from-a-repository/

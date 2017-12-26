# GIT



## COMMANDS
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

##  Submodules
https://chrisjean.com/git-submodules-adding-using-removing-and-updating/

##  LOG
```git log``` ..... look at the last few commits

## GIT stash
https://www.tutorialspoint.com/git/git_stash_operation.htm
```git stash```

`git stash list`

`git stash pop`

## Removing confidential files from GIT

https://help.github.com/articles/removing-sensitive-data-from-a-repository/

## Branching and Merging
https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches

In your github fork, you need to keep your master branch clean, by clean I mean without any changes, like that you can create at any time a branch from your master. Each time that you want to commit a bug or a feature, you need to create a branch for it, which will be a copy of your master branch.

When you do a pull request on a branch, you can continue to work on another branch and make another pull request on this other branch.

Before creating a new branch, pull the changes from upstream. Your master needs to be up to date.

Create the branch on your local machine and switch in this branch :

$ git checkout -b [name_of_your_new_branch]
Change working branch :

$ git checkout [name_of_your_new_branch]
Push the branch on github :

$ git push origin [name_of_your_new_branch]
When you want to commit something in your branch, be sure to be in your branch. Add -u parameter to set upstream.

You can see all branches created by using :

$ git branch
Which will show :

* approval_messages
  master
  master_clean
Add a new remote for your branch :

$ git remote add [name_of_your_remote]
Push changes from your commit into your branch :

$ git push [name_of_your_new_remote] [name_of_your_branch]
Update your branch when the original branch from official repository has been updated :

$ git fetch [name_of_your_remote]
Then you need to apply to merge changes, if your branch is derivated from develop you need to do :

$ git merge [name_of_your_remote]/develop
Delete a branch on your local filesystem :

$ git branch -d [name_of_your_new_branch]
To force the deletion of local branch on your filesystem :

$ git branch -D [name_of_your_new_branch]
Delete the branch on github :

$ git push origin :[name_of_your_new_branch]
The only difference is the : to say delete, you can do it too by using github interface to remove branch : https://help.github.com/articles/deleting-unused-branches.

If you want to change default branch, it's so easy with github, in your fork go into Admin and in the drop-down list default branch choose what you want.

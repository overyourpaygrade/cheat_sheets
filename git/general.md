### From [Git Codecademy](https://www.codecademy.com/learn/learn-git)

Git

In Git, the commit you are currently on is known as the HEAD commit. In many cases, the most recently made commit is the HEAD commit.

###### The commit you are currently on is known as the HEAD commit. Most recent in green. 
`git show HEAD`

###### Make changes then checkout the the last file:
`git checkout HEAD filename`

###### Remove file from staging area:
  This command resets the file in the staging area to be the same as the HEAD commit. It does not discard file changes from the working directory, it just removes them from the staging area.
  
`git reset HEAD filename`

###### Reset to a point in time from the log
`git reset (First 7 SHA Chars)`

###### Check the branch
`git branch`

###### Create a branch
`git branch new_branch`

###### Move to branch
`git checkout branch_name`

Git fast forwards master to match the branch. It knows that fencing has the most recent commit. 

To resolve a conflict you need to delete the markings of the one you dont want then you add and commit

###### Delete a branch
`git branch -d fencing`

###### Clone a remote into a local of your choosing
`git clone remote local_dir`

###### Get any changes that have been made since pull
`git fetch`

Changes are put in a remote branch and not merged to the local master.
To merge these you will need to merge

###### Integrate origin/master to the local master
`git merge origin/master`

###### Push local branch to origin
`git push origin branch_name`

```
General
git init creates a new Git repository
git status inspects the contents of the working directory and staging area
git add adds files from the working directory to the staging area
git diff shows the difference between the working directory and the staging area
git commit permanently stores file changes from the staging area in the repository
git log shows a list of all previous commits
git checkout HEAD filename: Discards changes in the working directory.
git reset HEAD filename: Unstages file changes in the staging area.
git reset SHA: Can be used to reset to a previous commit in your commit history.
git branch: Lists all a Git project's branches.
git branch branch_name: Creates a new branch.
git checkout branch_name: Used to switch from one branch to another.
git merge branch_name: Used to join file changes from one branch to another.
git branch -d branch_name: Deletes the branch specified.
git clone: Creates a local copy of a remote.
git remote -v: Lists a Git project's remotes.
git fetch: Fetches work from the remote into the local copy.
git merge origin/master: Merges origin/master into your local branch.
git push origin <branch_name>: Pushes a local branch to the origin remote.
```

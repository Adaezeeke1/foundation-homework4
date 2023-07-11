### Question 1:
Git is an example of a *version control* system

### Question 2:
Github

### Question 3:
* Committed: The committed state signifies that the changes made to a file have been saved in the Git repository. When a file is committed, it becomes a part of the project's history, and the changes are safely stored in the repository.


* Modified: When a file is modified, it means that changes have been made to the file since the last commit. Git tracks these modifications, and the file is considered to be in the modified state.


* Staged: Staging refers to the process of preparing modified files to be included in the next commit. When a file is staged, it means that the changes made to the file have been added to the staging area, and Git is aware of them. 


### Question 4:
* Pull request
* Repository

### Question 5:
git pull

### Question 6:
git fetch

### Question 7:
git push

### Question 8:
* Modified Files: Before committing, you need to have one or more modified files in your Git working directory. 
These files contain the changes you want to include in the commit.


* Staging Area: Git has a staging area, also known as the index, where you select and prepare the changes you want to include in the commit. 
Before committing, you need to stage the modified files using the **git add** command. 
This adds the changes to the staging area, marking them for inclusion in the next commit.


* Commit Message: Every commit should have a commit message that provides a concise and meaningful description of the changes made in the commit. 
The commit message helps you and others understand the purpose and content of the commit. 
When you run git commit, you need to provide a commit message along with the command.
To provide a commit message directly in the command, you can use the -m flag followed by the commit message: git commit -m "Commit message here". 


* Author Information: Git requires author information to associate with each commit. This information includes your name and email address.
Git uses the author information to track who made the changes and to maintain an accurate commit history.
Git uses the global configuration for authorship, which you can set using the following commands: 

> *git config --global user.name "Your Name"*

> *git config --global user.email "your@email.com"*

* An edit to help with pull request



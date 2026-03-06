# common commands

initialize repository
```bash
git init
```
clone repository
```bash
git clone <remote_repository_URL>
```
If clone it then you must be in the repository path in the terminal.
Example, for Linux/Windows:
```bash
cd <repository_path>
```
Display the current state of the working directory and the staging area
```bash
git status
```
Set your local username, you provide the name as an argument within quotes:
```bash
git config user.name "Your Name"
```
set your local email 
```bash
git config user.emaIl "youremail@example.com"
```
Create a branch and switch to it immediately 
```bash
git checkout -b <new-branch-name>
```
Switch to an existing branch:
```bash
git switch <existing-branch-name>
```
Add files to the staging area
```bash
git add <README.md>
```
Add all files to the staging area
```bash
git add .
```
Recording a snapshot of your repository at a specific moment in time
```bash
git commit -m "A brief description of the changes"
```
Links your local Git repository to a remote server, with "origin" used as a conventional shortcut name for that URL.
	This enables pushing and pulling changes between your local machine and the cloud-based repository
```bash
git remote add origin <remote_repository_URL>
```
Change the name of the current branch
```bash
git branch -M <branch_name>
```
Clear user from global config
```bash
git config --global --unset user.email
git config --global --unset-all user.name
```
push your local changes to your online repository.
```bash
git push -u origin <branch_name>
```
Fetch changes (but don't change any of your local branches):
```bash
git fetch origin main
```
Fetch changes and then merge them into your current branch:
```bash
git pull
```
Fetch changes and then rebase your current branch:
```bash
git pull --rebase
```
Caches credentials for 1 hour (3600 seconds)
```bash
git config --global credential.helper 'cache --timeout=3600' 
```
remove the credential helper setting specifically for the current local Git repository
```bash
git config --local --unset credential.helper
```
push the branch
```bash
git push origin branch_name
```
Create a pull request with specific parameters
```bash
gh pr create --base <target-branch-name> --head <source-branch-name> --title "PR Title" --body "PR description"
```
merge a pull request using the GitHub CLI
```bash
gh pr merge
```
More:

https://git-scm.com/cheat-sheet

+++
date = '2025-08-21'
draft = false
title = 'GitHub'
+++


#### GitHub is a platform that allows software developers to store, share, and manage their code. It also enables collaboration with other developers.
&nbsp;
&nbsp;

### Some features of GitHub:
1. You can upload your code and store it securely.  
2. You can host static websites directly from your repositories.  
3. You can share your code with other developers.  
4. Other developers can contribute to your repositories (if you allow it), and you can do the same for theirs.  

*(These are just some of the features. GitHub is constantly adding more.)*

&nbsp;
&nbsp;

### Steps to upload your project to GitHub
#### First, open your project directory in the terminal, VS Code, or any other code editor.  
&nbsp;

```bash
cd your_project_directory
git init
git remote add origin https://github.com/your_username/your_repo_name.git
git add .
git commit -m "Your commit message here"
git branch -M main
git push -u origin main
```

&nbsp;
&nbsp;
&nbsp;
### Steps to host your static website using GitHub Pages
1. Make sure your project is uploaded to GitHub.
2. Open your repository in a web browser.
3. Ensure it contains an `index.html` file and is a **static website** (no backend servers like Node.js, Flask, or Django).
4. Go to the **Settings** tab of your repository.
5. Navigate to **Pages** (Settings → Pages).
6. Under the **Branch** section, select `main` from the drop-down menu.

Your site will be live in a few minutes at:
`https://your_username.github.io/your_repo_name`

&nbsp;

---

### 1. Check which repo your directory is linked to
```bash
git remote -v
```
> Shows the remote URLs linked to your project (usually `origin`).  

&nbsp;

---

### 2. Change the remote repo (if you want to link to another one)
```bash
git remote set-url origin https://github.com/your_username/new_repo.git
```
> Use this if you want to push your local project to a **different repo** without reinitializing Git.

&nbsp;


---

### 3. Check your current branch
```bash
git branch
```
> Shows all branches. The one with `*` is your active branch.

&nbsp;


---

### 4. Create a new branch
```bash
git checkout -b new_branch_name
```
> Creates and switches to a new branch in one command.

&nbsp;


---

### 5. Switch to another branch
```bash
git checkout branch_name
```
> Use this to move between branches.

&nbsp;


---

### 6. See commit history (with nice one-liner view)
```bash
git log --oneline --graph --decorate --all
```
> Shows commit history in a clean, visual way.

&nbsp;


---

### 7. Undo last commit (but keep changes)
```bash
git reset --soft HEAD~1
```
> Use this if you messed up the commit message or forgot to add a file.

&nbsp;


---

### 8. Undo last commit (and delete changes completely)
```bash
git reset --hard HEAD~1
```
 **Warning:** This will wipe your last commit + changes permanently.

&nbsp;


---

### 9. Stash your changes (save work temporarily without committing)
```bash
git stash
```
> Hides your current work. You can bring it back later.

To reapply:
```bash
git stash pop
```


&nbsp;


---

### 10. Pull the latest code from GitHub
```bash
git pull origin main
```
> Fetches the latest updates from the remote repo and merges them into your branch.


&nbsp;


---

### 11. Clone a repo
```bash
git clone https://github.com/username/repo.git
```
> Makes a full local copy of an existing repo.

&nbsp;


---

### 12. View file changes before committing
```bash
git status
git diff
```
> Shows what has been modified and what’s staged for commit.


&nbsp;


---

### 13. Remove a file from Git (but keep it locally)
```bash
git rm --cached filename
```
> Useful when you accidentally added `node_modules` or `.env` by mistake.


&nbsp;


---

### 14. Ignore files in Git
Create a `.gitignore` file in your project and add patterns:
```
node_modules/
*.log
.env
```


&nbsp;


---

### 15. Rename a branch
```bash
git branch -m old_branch_name new_branch_name
```


&nbsp;


---

### 16. Delete a branch
```bash
git branch -d branch_name     # delete local branch
git push origin --delete branch_name   # delete remote branch
```


&nbsp;


---

### 17. Fix “main” vs “master” confusion
If your repo uses `master` but you want to rename it:
```bash
git branch -M main
git push -u origin main
```

&nbsp;


---

### 18. Force push (overwrite remote)
```bash
git push origin main --force
```
Dangerous. This **overwrites remote history** — only use when absolutely necessary.

&nbsp;


---

### 19. See who made what changes (blame feature)
```bash
git blame filename
```
> Shows line-by-line who last modified each part of a file.


&nbsp;


---

### 20. Create a new repo directly from command line
```bash
gh repo create
```
> Requires **GitHub CLI** (`gh`) installed. Lets you create repos without opening GitHub in a browser.

&nbsp;


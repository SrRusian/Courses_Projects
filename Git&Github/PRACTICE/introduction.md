INFO FROM https://www.codedex.io/git-github

1.  INTRODUCTION

In 2005, a Finnish software engineer named Linus Torvalds ran into a problem while building the Linux operating system. With so many versions of the code, managing everything became a nightmare. So he created Git, a version control system that tracks changes to a project's code.
git --version

A few years later, the web platform GitHub launched, founded by Tom Preston-Werner, Chris Wanstrath, and PJ Hyett in San Francisco. Often called the "Google Drive for code," it quickly became the standard way for developers to store, share, and collaborate on code online, with 150 million users.

2.  REPOSITORIES

# GitHub Repos

Git is the tool that allows software engineers to track changes, while GitHub is the website that hosts Git repositories. Simply put, GitHub was built on top of Git, so we cannot use GitHub without Git.

Code is stored in repositories or repos on GitHub, which are like folders for your files and assets (e.g. images, videos, audios, fonts).

3.  GIT COMMANDS

# Remote & Local

Think of something that you can share online, it could be some code (like a .html, .css, .js, .py, .cpp, .java file) from one of our courses, a personal project, or a homework assignment.

To get our code online, we have to work with two types of repos that connect with one another:
Remote repository: a GitHub repo stored somewhere on the internet (for the latest version).
Local repository: a Git repo that lives on your own computer (for drafts).

# Git Init

The git init command initializes a new Git repo (local repo). It's the first command you run when you have a new project and want to start tracking changes. The history of your project starts here!
git init

When you run this command, Git will create a new directory named .git in your project folder. This directory contains all the information about your project's history and configuration.

The terminal will return something like this once done successfully:
Initialized empty Git repository in /Users/username/Desktop/python/.git

# Git Remote

Local repo? Check. Remote repo? Check. Now, we can connect our local repo with our remote repo.

The git remote command manages connections to remote repos. We can add a connection by:
git remote add origin <repository_url>
add: Add a new remote connection.
origin: Give a nickname for the remote repo's URL (origin is a common one).
<repository_url>: Placeholder for the remote repo's URL.
Our example would be:
git remote add origin https://github.com/repo/first-repo.git
Here we're telling Git: "Connect my local repo to the first-repo remote repo, and I’ll call the URL origin."

# Git Branch

Let's now rename the branch to main. This will be the branch we push code to, and will be default branch.
git branch -M main
The uppercase -M flag means "move" (or "rename"). We'll discuss what branches are later in the chapter.

4.  Git Workflow

# Remote & Local

Now that we've connected our local & remote repos, let's turning the project folder into the local repo.
The two main Git commands that we will use are git add and git commit.
But first, we have to make a distinction between the working directory and the staging area:
-Working directory is the project folder on your computer! When you make changes to the files, Git tracks them, and you can move selected changes to the staging area using the git add command.
-Staging area is where we prep changes, like "I'm almost ready! One more min!" It's a temporary area where you choose what files you want to "commit" to the local repo with git commit.

# Git Add

The git add command tells Git which changes you want to include in the next commit. Think of it like packing your suitcase before a trip – it's choosing what to bring.

Here are three variations...
1️⃣ Add one file

To add a single file to the staging area:

git add example.txt

Here, the command will only add the example.txt file.

🔡 Add all files

To add all the changed files to the staging area:

git add .

Here, any new file added or changed to the working directory will be included.

\*️⃣ Add all files with an extension

To only stage files with a specified extension:

git add \*.html

Here, the command will only add .html files.

## Git Commit

Committing files are about saving a "snapshot" of the current code. 💾 Each commit captures a moment in time and includes a helpful message to explain what changed. This helps you track your progress and separate different actions in your code.

Now that we are ready to commit your staged files, use the following command:

git commit -m 'Your commit message here!'

The lowercase -m flag means "message".

Here's what some commit messages might look like for a typical project:

'Initial commit'
'Add pics to homepage'
'Fixed again fr this time!!'
Note: Commit messages get silly when you're working on your own for a while 😛, but short, clear, and descriptive messages are needed when working on a team! We want messages to help you (and your team) understand what changed and why.

If the commit is succesful, you should see a message appear in the terminal, something like:

git commit -m 'Updated index.html with a new line'

[main 09f4acd] Updated index.html with a new line
1 file changed, 1 insertion(+)

Pretty useful, right? Commit messages are almost like journal entries.

Let's continue and get our project to the local repo!

5.  Local Push

# Finally...

We are almost done! It's time to move our code from the local repo to the remote repo on GitHub.

But before we push our code to GitHub, we need to make sure we have the correct files commited!

## Git Status

The git status command is used to check the status of your files. It is a handy command that will show you which files are staged, unstaged, and untracked.

Staged files are ready to be committed.
Unstaged files are not yet ready to be committed.
Untracked files are new files that Git has not seen before.
Simply run the following command to check the status of your files:

git status

In short, you are saying, "Hey Git, what's the situation right now?"

An example response would be:

On branch main

No commits yet

Untracked files:
.DS_Store
test.py
output.gif

Use git status anytime you're confused about the state of your repo.

## Git Push

Let's now use the command we'll use to finally "push" or publish our code! This is the last step.

working directory vs staging area vs repo

The git push command is used to send your locally committed changes to your remote repository. You'll see all the changes you've made on GitHub.

1️⃣ First time

The very first time you push to a branch, the command usually looks like this:

git push -u origin main

The -u flag stands for "upstream". This links your local branch to the remote branch so that future push commands will automatically apply to this branch without needing to specify it each time. ✨

2️⃣ Every other time

Once that's set, any commits you push to this branch will just require:

git push

When that's done, you'll be able to refresh your GitHub repository URL, and see your changes online!

6.  Git Clone

# Working with a Team

Codédex has teammates around the world in different time zones. But how the heck do we (and countless other tech companies and open-source projects) manage to work on the same codebase without stepping on each other's toes?

In this chapter, we'll dive into how Git and GitHub make collaboration possible. We'll cover all the bases to understand how something like this works!

First thing first, cloning... And no, we are not talking about cloning DNA in Jurassic Park, we are talking about repo cloning!

# Cloning

Consider this: you want to work on a project that someone else has already started. You need a way to get a copy of their work onto your own computer so you can make changes, add features, or fix bugs.

This is where cloning comes into play! Cloning happens when a repository is already made on GitHub, and you copy that remote repository to your local machine.

We're able to clone a repository using the git clone command, like this:

git clone https://github.com/YOUR_USERNAME/EXAMPLE_REPO.git

Where YOUR_USERNAME is your GitHub username and EXAMPLE_REPO is the name of the repository you want to clone.

Note: You don't need to write anything in the terminal yet! This is just an example of the command you'll use later.

This link is quickly accessible to copy from the button labeled “Code” on a GitHub repository!

Once cloned, there's a folder named after the repository now saved on your computer. You can use the cd command to access all the files inside of it and you'll be able to open the folder in a code editor (like VS Code) to start adding your changes!

# Permissions

You're able to clone any repository, but to see changes reflected on the repositories, you'll need what's called, "write access".

Write access is granted by the owner of the repository to allow you to make commits, create branches, and overall change the remote repository.

Here are the common types of permissions that GitHub offers for repositories:

Access Type Description
👀 Read Users can view the repository and clone it.
📝 Write Users can read the repository and make changes, create branches, and push modifications.
👑 Admin Full control: manage settings, access permissions, and delete repo.

# Forking

Wait… What if you don't have write access or you're not allowed to make changes? There's forking!

Forking is a process where you create a personal copy of someone else's repository on GitHub. 🍴

Think of it as copying down your grandma's cherry pie recipe. If you're making a change to the recipe, you'll make the changes on your own copy, not the original recipe. Similarly, a "fork" from a repository allows you to freely experiment with changes without affecting the original project!

Cherry pie sprite

To fork a repository, you'll notice that the top of the repository may look something like this:

Clicking on the "Fork" button, and following the steps, creates and moves a copy to your GitHub account.

You'll then have ownership access to the copied repository.

7.  Branch Out

# Branches

Whereas forks are copies of the code made outside the repository, branches are copies of the code made inside the repository. 🌿

On GitHub, you may notice the word “main” (sometimes “master”) as the default branch name on a repository:

Branch dropdown on GitHub repo page, currently set to main

The main branch if your "main timeline", or your primary branch. From this branch, we're able to create versions of the code within the same repository without changing the main branch.

Now, let's take a look at exactly what branching looks like:

Branch diagram featuring changes inside and between different Git branches

Branches can stem from either the main branch or other existing branches, and later lead back to the main branch with a "PR" (Pull Request). This allows you to work on different features or fixes without affecting the main code until you're ready to merge your changes.

This is especially useful when working in a team, as it allows multiple people to work on different features simultaneously without interfering with each other's work.

## Working on a Branch

By default, you'll be on the main branch unless specified otherwise on GitHub. You'll typically want to branch out from the main branch to work on your desired feature or version.

We do so by using the following command:

git branch new-branch-name

The git branch command creates a new branch from the branch you're currently on. You can switch to that branch with git switch:

git switch new-branch-name

You can also create and switch to a new branch in a single command:

git checkout -b <new-branch-name>

This branch now becomes your coding playground, where you can switch around and change code as needed and to your liking!

8.  Git & Teams

# Maintaining Your Local Repo

When working with other developers on the same project, the code may frequently change from commits being made to the repository. Therefore, the repository you initially cloned might have changes to the main branch others made that you'll want to reflect on your branch.

To keep your repository up to date, you're going to use the git pull command. This command updates the branch that you are currently working on, whether that be the default main branch, or a branch that you created. To help understand the uses of the git pull command, let's walk through a scenario where git pull will be helpful for us to use, and you may find yourself in.

# Teamwork in Action

Teamwork makes the dream work!

Melody is working on a hackathon project with her team. She is working in a branch called feature, where she is in charge of adding a feature to the app she's working on.

She runs into an issue that her teammate, Emily, has already fixed before, so she asks her for help. Emily switches into Melody's branch using git checkout feature, and identifies the bug.

Emily changes a couple of lines of code on the feature branch and pushes her changes. Melody now wants to see these changes reflected on her version of the repository on her computer, so she uses the git pull command. Melody sees the lines of code Emily changed and continues to work on the feature.

9.  Merges

# Merging Branches

Emily and Melody are further along in their hackathon project. Melody has finished writing some code, and she wants to merge her branch to the main branch. Once merged, their project is almost complete!

Emily now wants to make sure that another feature she's working on for the project is working properly with Melody's code that she just finished.

Emily switches from her branch to the main branch. She uses the git pull command to update her local repository.

git checkout main
git pull

The changes are reflected, and to use the new version of the main branch on Emily's branch, she switches back to her own branch.

git checkout emily-feature-branch

Emily now wants to bring in the changes from the main branch into her own branch so that she can continue working with the latest code.

She does this by merging the main branch into her current branch.

git merge main

Melody's changes from the main branch are now in her branch!

Emily can now continue working on her feature, knowing that it is up to date with the latest changes from the main branch.

The scenario above describes how we can bring in changes from one branch to another, using the following command:

git merge <branch-name>

The git merge command keeps our development workflow combined and up to date! We maintain a structured project history so we're able to avoid messy merge conflicts!

# Merge Conflicts

A merge conflict happens when:

Changes are made to the same part of a file.
One branch has deleted a file while the other branch has modified it. 😐
Git doesn't know which changes it should keep, and it signals a conflict in the code as shown below. This can happen when using the git pull or git merge commands.

// Changes from the branch being merged

To fix the conflicts, your code editor usually has shortcuts or highlighting for conflicts that make it easier for you to pick and choose which changes you want to keep. You'll have a few types of options to choose from when dealing with conflicts:

Accept Incoming Changes: Overwrites changes on the current branch with changes from the branch being merged in.
Accept Current Changes: Keeps changes on the current branch, and ignores changes from the branch being merged in.
Accept Both Changes: Keeps both branch versions of the changed lines or files.
Once all of your changes are resolved, you can continue with committing your code and making a commit message that lets your team know that you have made a merge! After using the git add ., git commit -m 'message', and git push workflow, you can continue with development!

10. Pull Requests

# Proposing Changes

During development or open source contribution, you're going to want to add changes from your created branches to the main branch.

Pull request diagram

A Pull request (PR) allows you to suggest changes to the repository and allows you to create edits from one branch to another. PRs are just merges, but instead of just allowing you to merge branches in the same repository, they also allow you to merge branches across repositories.

A pull request will show you what parts of the code you are comparing, changes made, and a list of your commit history, which helps you identify what exactly you'll be changing.

Once the team successfully reviews your suggested code and approves any necessary changes, this pull request will be merged into the default branch!

## Creating a PR

To create a pull request,

You should have pushed changes to the repository itself or a forked version of that repository.
You don't have any merge conflicts. You can make sure of this by having your local repository up to date with your remote repository.
You can locate the pull requests at the top of the repository.

'Pull Request' tab located between 'Issues' and 'Actions' tabs on GitHub repo page

Click the “New Pull Request” button.

Green 'New pull request' button

Here, you can choose the branches you'll be comparing. Note that you'll also sometimes see a “Compare and Pull Request” button that can also take you to make a PR.

Once you take a look at any necessary code changes, you can add a title for your pull request and a description. Some repositories will have specific guidelines for you to follow in your description to add any necessary information, while others, or even your own may not follow any particular structure.

A PR “merge” will act like any other commit to a branch, so your title should be as descriptive as you can, similar to a commit message! This helps other developers know and understand what code is being changed from a glance.

Form for creating a new pull request

Once created, you or your code approvers, depending on your repository permissions, can approve, request changes, or add comments to your code! This allows you to merge your branch.

## The PR Checklist

Pull requests are essential to the Git development workflow, and once you know you're ready to create a PR, review the following steps to ensure a smooth integration! ✅

Pull the latest changes from the main, or default branch.
git pull origin main

Test your code! Make sure that everything works or shows up as intended.
Review your code! Make sure that when committing, everything is as you wrote, your code is polished, and anything not needed is removed (for example, console.logs or print statements)
Fix any merge conflicts!

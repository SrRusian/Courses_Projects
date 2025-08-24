1.  In The Beginning...

# A Brief History

The command line interface is a text-based program that lets you do all sorts of stuff with your computer system, like navigate it or move files and folders.

Since the 1970s, command line interfaces (CLI) have let us interact with our computers via commands typed on a keyboard. While graphical user interfaces (GUI) became mainstream in the 80s and 90s, the command line remains popular within the developer community.

Terminal and our three characters

They are known by different names:

On Mac, the command line is known as the Terminal.
On Windows, it is known as the Command Prompt.
Even today, working on the command line has some advantages over working with GUI applications:

Automating common tasks can be done with 1 or 2 commands.
They use less of the computer's processing power.
Targeting files and folders is easier.
And you feel more like a hacker in the movies!

2.  Filesystem

# Directories

Essentially, your computer is a filesystem made of folders and files:

Filesystem diagram

In the context of the command line, we refer to folders as directories.

Inside any given directory could be the following:

More directories (also known as subdirectories).
Files that have content inside (text, image, or video files).

# Print Working Directory: pwd

The filesystem of your computer can be intimidating at first, and it's easy to get lost.

The working directory is wherever you are currently at within the filesystem.

We can show this with the pwd command, which stands for "print working directory".

    pwd

/Users/dwight-schrute

This means that the working directory we are currently on is /Users/dwight-schrute, a dwight-schrute folder inside the Users folder

3.  Moving Day

# Change Directory: cd

So we can open the command line as well as view the current directory in our computer's filesystem.

But how do we actually navigate the filesystem via the command line? We do this with the cd “change directory” command!

    cd directory-name

The directory-name is the directory we want to change into (making this the new current directory).

Let's say we're currently on the following working directory:

    pwd

/Users/dwight-schrute/

Your username is also a directory that contains more directories, including one for your computer's desktop! We can move to that Desktop directory with the cd command:

    cd Desktop
    pwd

/Users/dwight-schrute/Desktop

If you try to change into a non-existent directory, you'll get an error:

    cd something

something: No such file or directory

# List Content: ls

But wait, how do you always know what you're typing next to cd is a valid directory name? There's a command to list out all subdirectories under our current directory!

We can use the ls list command to show all directories and files that exist in your current working directory. Assuming we're on the dwight-schrute directory:

    ls

Desktop
Documents
Images
script.js
dundie-awards.txt

Running the ls command shows there are three subdirectories:

Desktop
Documents
Images
There are also two files, script.js and dundie-awards.txt.

4.  House Tour

# Traversing the Filesystem

On the command line, typing cd followed by a valid directory name moves our current directory "forward" in the filesystem, as shown below:

Changing from one folder to another with the cd command

But that's not all the cd command can do! Oh no. It can also be used to go "backward" in the filesystem, using two periods. Assuming we're currently on the schrute-farms directory, here's what this looks like:

    pwd

/Users/dwight-schrute/schrute-farms
cd ..
pwd
/Users/dwight-schrute/

Using the .. double period moves us back in our filesystem.

Note: When moving forward in the filesystem, we go to a "child" directory. When moving backward, we go up to a "parent" directory.

Even so, one directory at a time can get tiring really quickly. In this case, we use a forward slash / to move up or down multiple directories in a single command:

    pwd

/Users/dwight-schrute/schrute-farms/
cd ../..
pwd
/Users/

# Viewing File Content

If we want to see what is inside of a file (like a text-based .txt file or a Python .py file), we can do so with the cat command!

    pwd

/Users/dwight-schrute/schrute-farms/
ls
beets.txt
cat beets.txt
I have 100 beets!

The cat command will print all text-based content from a file to the command line.

Note: The echo command can also be used for viewing file content, but the cat command is more commonly used.

5.  Clean Slate

# Clearing the Command Line

Phew! We've done a lot of typing on the command line already! Have you noticed the command line getting a little crowded with the previously run commands?

Crowded terminal with commands previously run thus far in course

While this may not bother some, you may be wondering if there is a way to "clean the slate" and clear the command line. Well, there is!

The clear command will clear everything from view on the command line.

clear command example

Note: This command does not reset your current working directory in the filesystem. It just makes the command line visibly cleaner.

# Keyboard Shortcuts

As you can imagine, the command line is mostly worked with a keyboard.

While you've already learned about and run a few awesome commands, there are some keyboard shortcuts you should try that do similar things.

## Command History

One of the most helpful shortcuts is using your keyboard's ↑ and ↓ arrow keys to automatically bring up commands you'd previously written.

This is a total game-changer and time-saver. Instead of typing or retyping a command, you can simply just bring it back with this shortcut!

## Tab

There is also a keyboard shortcut for completing what you type on the command line!

When typing on the command line, the tab key can be used for auto-completing the names of things such as:

The names of commands.
The names of existing files or directories.
tab shortcut example

This shortcut can be really nifty for reducing errors.

6.  Recipes

# Introduction

Command Description
pwd Prints the working directory on the command line.
ls Lists off the files and folders under the working directory.
cd Changes the location of the working directory.
cat Displays the contents of an existing file.
But the command line is so much more powerful than that!

It can also reorganize your filesystem and create new files and directories when needed.

In this chapter, we will learn how to manipulate the contents of our filesystem via the command line.

# Make Directory: mkdir

Our filesystem is made of directories that may contain files and even more directories. But what if we wanted to make new directories?

This is where the mkdir command comes in handy:

mkdir new-directory

The mkdir command, short for "make directory", creates a new directory inside of the current directory. 🌱

So if you're in the Users/taylor-swift file path and use the mkdir command:

mkdir albums

This creates a new empty albums directory.

Note: mkdir doesn't move us into the newly created directory, so in this case, we are still in the Users/taylor-swift file path and can check if it worked using the ls command or move into the newly created directory using the cd change directory command.

It's also possible to create subdirectories with the mkdir command, using a slash character.

Suppose we want to create a folder of lyrics for Taylor Swift's 2020 album Folklore:

    pwd

Users/taylor-swift
mkdir albums/folklore

From within the taylor-swift/albums directory, we created a new folklore directory. But we're still currently working from the taylor-swift directory.

Note: If we try making a new directory from within a nonexistent directory, we get the following error: mkdir: albums: No such file or directory.

7.  Cuisine Type

# Create New File: touch

Creating new directories in the command line is pretty cool, but what about new files? After all, files are what contain the really good stuff such as code, text, etc.

We can create new files using the touch command!

So suppose we want to create a text file for the song "Cardigan":

    touch cardigan.txt

Typing the touch command followed by the name of a new file will create it.

We can even use the touch command to create new files inside of existing directories:

    touch folklore/exile.txt

Here, we created a text file called exile.txt inside the folklore directory.

Note: Besides .txt files, the touch command can create any type of file such as .py Python files or .html HTML files.

8.  Grilled Cheese

# Write to a File

Not only can we create new files on the command line, but we can also write to them! 📝

We can do this with a command we already learned about — echo. You'll find that commands like this can be used for more than one purpose.

By itself, echo just prints text to the command line:

    echo "Vintage tee, brand new phone"

Vintage tee, brand new phone

But we can also use it to write to a file:

    echo "Vintage tee, brand new phone" > cardigan.txt

Here, we added song lyrics from "Cardigan" to a cardigan.txt file.

We first type echo with a piece of text, then the > greater than sign, followed by a file name we'd like to write to.

Note: If the file doesn't exist, it will be created automatically!

We can then use the cat command to display the file content:

    cat cardigan.txt

Vintage tee, brand new phone

It's important to mention, however, that using the > greater than symbol will overwrite any existing content in a file. If we want to add content to a file and keep what is already there, use two greater than symbols >>:

    echo "High heels on cobblestone" >> cardigan.txt
    cat cardigan.txt

Vintage tee, brand new phone
High heels on cobblestone

# Combine Files

Adding plain text to a file is cool and all, but that's a lot of typing on the command line.

What if we wanted to combine the text of two files? How can we do that?

This can be done with the cat command! 🐈

While the cat command can be used to display the contents of a file, it can also be used to put content from one file into another:

    cat file-a > file-b

After the cat command, we type the name of file-a followed by the greater than symbol >, followed by the name of file-b. This will write the contents of file-a into file-b.

But like with echo, using the single > greater than symbol will overwrite anything that existed before. To simply add contents to a file with the cat command, we use the double greater than >> symbol.

For example, if we wanted to add the chorus from "Cardigan" from one file to another:

    cat chorus.txt >> cardigan.txt

The output would look something like this:

    cat cardigan

Vintage tee, brand new phone
High heels on cobblestone
And when I felt like I was an old cardigan
Under someone's bed
You put me on and said I was your favorite

9.  Move Around

# Move Directories & Files

Just like when rearranging books in a library or customizing music playlists, sometimes we need to move things around in our computer filesystem.

Image, video, and music files going into folders

The command for the job is the mv command (short for "move"). With it, we can move a file or directory from one place to another.

    mv cardigan.txt albums/folklore/

Above, we type mv followed by the file/directory we want to move, followed by the directory we want to move things to. It's good to know that we can use the slash character / to be more specific about where we're moving things.

Note: If we're moving a directory, everything inside of it will be moved as well.

## Renaming

We can even use the mv command to rename existing files and directories:

    mv albums discography

If the second argument of mv is neither a file nor a directory, the first argument is renamed to that. This renames the albums directory to discography.

# Removing Directories & Files

What if there's something in our filesystem that we no longer need and we want to remove it?

On the command line, there are two options.

For files, we can use the rm command (short for "remove").

We can either remove a single file:

    rm exile.txt

Or we can remove multiple files in a single command:

    rm exile.txt cardigan.txt willow.txt

For removing directories, we use the rmdir command.

The same thing applies where we can either remove a single directory:

    rmdir folklore/

Or we can remove multiple directories (each separated by a space):

    rmdir folklore/ evermore/ 1989/

However, the rmdir command only removes empty directories. So if there's anything inside a given directory, this command will not work.

To remove a non-empty directory, we'll need to use the rm command with a special -r flag:

    rm -r folklore

This will remove the folklore directory along with what is inside of it.

The -r flag "recursively" deletes content of a directory, meaning that it deletes even the hidden files and subdirectories.

Depending on our computer's settings, we may be prompted to confirm we want to actually remove a non-empty directory. This is to ensure nothing important is accidentally deleted forever.

Note: To prevent unexpected behavior, make sure to change out of a directory before removing it with rm.

10. Copy That

# Copy Files: cp

In some situations, it is wise to create a copy of something so that our progress is saved for next time or so we can share it with our friends or colleagues.

The files and directories we make on the computer can be copied via the command line!

For copying file content onto another file, we use the cp command (short for "copy"):

cp file-a file-b

This will make a copy of file-a and send its contents into file-b.

If file-b does not exist, it is created automatically.
If it does exist, all contents are overwritten with what is copied from file-a.

# Copy Directories: cp -r

We can also make a copy of a directory with the cp command!

cp -r directory-a/ directory-b/

You must include the -r "recursive" flag to copy everything from one directory into another.

Just like with files, directory-b is automatically created if it doesn't yet exist. Otherwise, its content is overwritten with what is copied from directory-a.

Suppose we want to create a copy of a playlist of our favorite Taylor Swift songs:

    cp -r taylor-swift-playlist playlist-copy

All files and subdirectories in taylor-swift-playlist are copied over to playlist-copy!

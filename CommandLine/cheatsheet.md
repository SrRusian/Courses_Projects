# Navigation

Command Description
echo output-here Print what is typed next to this command.
pwd Print the current working directory.
cat file-name.extension Print the contents of a file.
ls List the contents of the current directory.
cd directory-name Change into an existing directory.
cd .. Change backward into an existing directory.
cd directory-name/sub-directory-name Change forward on multiple directories.
cd ../.. Change backward on multiple directories.
clear Clear the command line screen.

# Keyboard Shortcuts

Shortcut Description
tab Complete the name of an existing file or directory being typed.
↑/↓ Retype commands that were previously written.
command + k Clear the command line screen.
Note: Even after clearing the command line screen, you can still use previous commands with the ↑ and ↓ arrow keys!

# Manipulation

Command Description
mkdir Create a new directory from the current directory.
touch Create and save a new file.
echo "text" > file Overwrite existing content in file with "text".
echo "this text" >> file Write "this text" to existing content in file.
cat file-a > file-b Overwrite content of file-b with content of file-a.
cat file-a >> file-b Add content of file-a to content of file-b.
mv source-file target-file Move/rename the source-file into the target-file.
mv source-directory target-directory Move/rename the source-directory into the target-directory.
rm file Delete a file.
rm -r directory Delete a non-empty directory.
rmdir directory Delete an empty directory.
cp file-a > file-b Copy content of file-a into a file-b (overwriting anything already inside).
cp -r directory-a directory-b Copy content of directory-a into a directory-b (overwriting anything already inside).

# Operators

Operator Description Example

> Overwrite the contents of a file with the results of a command. echo "Hello, World" > file.txt
>
> > Add the result of a command to the end of a file. echo "Hello, World" >> file.txt
> > ; Run multiple commands in a row, one after another. echo "Howdy there!" ; cat file.xt
> > || Logical OR: Runs an alternative command if the first one fails. mkdir work || echo "Directory creation failed. Does it already exist?"
> > && Logical AND: Runs the next command if the first one succeeds. mkdir video-games && cd video-games

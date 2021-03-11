## Bash Note

### General
To measure the time,

`time <SOME_COMMAND>`

To suppress the output,

`<COMMAND> >/dev/null 2>/dev/null`

To show the number of files in a directories in one line,

`ls -l | grep -v ^d | wc -l`

To show the directory file size,

`du -h your_directory`

or more in compact,

`du -hcs your_directory`

To count the number of files in a directory, using a tree comand,

`tree DIRECTORY`

To exit the shell program, `exit 0` 

To create an array,

`arr=(1 2 3 4 9)`

To access this array,

`${arr[@]}` You need `[@]` because without this, you will only get the first element of the array, which is 1.

To access the array elements but excluding the last element,

`${arr[@]::${#arr[@]}-1}`



Double quotation can consists of variables

`x=2`
`y=3`
`echo "(${x},${y})"` => (2,3)

But single quatation cannot consists of variables but instead takes name of the variable itself,

`echo '(${x},${y})'` => (${x},${y})

For if .. elif .. else statements, basic syntax is as following. Make sure to have spaces between single bracket, variable, etc.

```
if [ $var == $otherVar ]
then
   SOME_COMMAND
elif [ $var == $otherVar ]
then
    SOME_COMMAND
else
    SOME_COMMAND
fi
```
You can put semicolon `;` to make `then` inline as,

`if [ $var == $otherVar ]; then`

To generate the unique id in bash script and save it the variable,

`uuid=$(uuidgen)`


### Conda


When you use miniconda3 in linux, first bash command to go to your shell

 `> bash`

if conda command is not recognized, add a line under **.bashrc** file in your user home directory:

`export PATH=~/miniconda3/bin:$PATH`

then test it with

`conda --version`

now you can activate with conda command

`conda actiate`

### Running in Background (e.g. Screen)

You can run command with `&` in the background by,

`<COMMAND> &`

Multiple commands (3 processes) in the background by,

`<COMMAND> & <COMMAND> & <COMMAND> &`

Screen command to make another shell that can run in the background.

`screen`

Shortcut:

- Shortcut <kbd>Ctrl</kbd> + <kbd>A</kbd> then press <kbd>C</kbd> to create a new window (with shell)
- Shortcut <kbd>Ctrl</kbd> + <kbd>A</kbd> then press <kbd>D</kbd> to detach from the current screen
- `screen -r` to resume the screen session. For multiple screen sessions, do `screen -r <SCREEN_ID>`
- `screen -ls` to list the current running sessions
- <kbd>Ctrl</kbd> + <kbd>A</kbd> and <kbd>Esc</kbd> to enter scrolling mode. Press <kbd>Esc</kbd> again to exit the scrolling mode.


### Git

To reset all stashed stages from `git add <FILES>` do,

`git reset`

To revert the actual changes you have made instead of unstash them,

`git checkout -- <FILE_NAME>`

To commit with muliple lines of comment with vim editor (make sure you are in English keyboard),

1. `git commit`
2. Then press <kbd>i</kbd>
3. Type comments
4. Press <kbd>Esc</kbd>, then enter `wq` and press <kbd>Enter</kbd>.

To commit with one line of comment,

`git commit -m "<COMMENT>"`

To see the changes,

`git diff <FILE>`

# Ubuntu Tips
## Time and dates
### Display
`timedatectl`

## File System
### move folders and sub files/folders
`sudo mv fromPath/ toPath/`
### rename folders
`mv old_name new_name `
### List all directories by size
`du -sh *`
### List all Files by size and update
`stat -c "%y %s %n" *`

and sorted by date - reversed

`stat -c '%y - %n' * | sort -r -t'-' -k1,1`
### How many files in a directory
`find . -type f | wc -l`

`$ tree share/some/directory/ | tail -1
558 directories, 853 files`

### List the block devices attached to your instance
`lsblk`
### Get space used on volumes
`df -T`

`df -h`
### Get type of storage device
sudo file -s /dev/xvd*
### Expand the Linux Volume
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html

## Process Management
### List all processes
`ps -ef`
#### Get Skyze process
`ps -ef | grep skyze `

In `ps -ef` the Skyze process looks like:

`ubuntu   22440 22283  1 07:47 pts/0    00:00:01 /home/ubuntu/.local/share/virtualenvs/Skyze-ZP_7bfwZ/bin/python3 run_skyze.py`
### Run process in background independent of shell

`nohup pipenv run python3 run_skyze.py > /dev/null 2>&1 &`


`nohup pipenv run python3 run_skyze.py > /Logs/skyze20180108.out 2>&1 &`

1. nohup means: Do not terminate this process even when the stty is cut off.
2. > /dev/null means: stdout goes to /dev/null (which is a dummy device that does not record any output).
3. 2>&1 means: stderr also goes to the stdout (which is already redirected to /dev/null). You may replace &1 with a file path to keep a log of errors, e.g.: 2>/tmp/myLog
4. & at the end means: run this command as a background task.


`nohup script.sh 2>&1 script.out &
#### later:
tail -f script.out`

If you close the shell/terminal or log off, your command is no longer a child of that shell. It belongs to `init` process. If you search in `pstree` you'll see it is now owned by process 1 (init). That cannot be brought back to the foreground because the foreground no longer exists.

#### Stop the processes
`ubuntu@ip-172-31-91-79:~/Skyze/Skyze$ pgrep -a python3
30691 /home/ubuntu/.local/share/virtualenvs/Skyze-ZP_7bfwZ/bin/python3 run_skyze.py`

`kill 7360`
#### Disown
It will immediately be removed from the list in the jobs output and no longer associated with the terminal.

The command is called by specifying a job number. For instance, to immediately disown job 2, we could type:

`disown -h %2`
This leaves the process in a state not unlike that of a nohup process after the controlling terminal has been closed. The exception is that any output will be lost when the controlling terminal closes if it is not being redirected to a file.
You can pass the -h flag to the disown process instead in order to mark the process to ignore SIGHUP signals, but to otherwise continue on as a regular job:

### Process Commands
In Unix, a background process executes independently of the shell, leaving the terminal free for other work. To run a process in the background, include an & (an ampersand) at the end of the command you use to run the job. Following are some examples:

To run the count program, which will display the process identification number of the job, enter:
 `count &`
To check the status of your job, enter:
 `jobs`
To bring a background process to the foreground, enter:
 `fg`
If you have more than one job suspended in the background, enter:
 `fg %#`
Replace # with the job number, as shown in the first column of the output of the jobs command.

You can kill a background process by entering:
 `kill PID`
Replace PID with the process ID of the job. If that fails, enter the following:

 `kill -KILL PID`
To determine a job's PID, enter:
 `jobs -l`
If you are using sh, ksh, bash, or zsh, you may prevent background processes from sending error messages to the terminal. Redirect the output to /dev/null using the following syntax:
 `count 2> /dev/null &`

## Zip on Mac //// Unzip Ubuntu

After much research and experimentation, I found this works every time:

1) Create a zipped tar file with this command on the Mac in Terminal:

`tar -cvzf your_archive_name.tar.gz your_folder_name/`

`zip -r my_arch.zip my_folder`

2) When you FTP the file from one server to another, make sure you do so with binary mode turned on

3) Unzip and untar in two steps in your shell on the Linux box (in this case, tcsh):

`gunzip your_archive_name.tar.gz`

`tar -xvf your_archive_name.tar`

## ADDING ENVIORNMENT VARIABLES
```pwd
ls-a
nano .bash_profile
source ~/.bash_profile
printenv```

## Reload bash files
`. ~/.bashrc`

# Using the Command Line

Before Apple Computers made the Graphical User Interface (GUI) mainstream in the 1980s, most interaction with computers was via the command line. Users would be presented with a "command prompt",  character like `>` which would prompt them to enter a **command**. They would then hit the `Enter` key and the command would execute (generally providing some feedback on the next line). A typical command would look like `print "Hello"`. Commands could have **arguments** (also referred to as flags); for instance `print -l "Hello"` might print "hello" in all lower case.

User's of today's Windows and Macintosh machines have mostly forgotten how to do things with the command line, but this knowledge is still useful for Digital Humanists. Many experienced users prefer the command line to the GUI because it can be faster. Some tools must still be installed from the command line. And Digital Humanists often have to perform actions on a server, for which the interface is still largely the command line.

This last use brings up an important point. Most servers today run some brand of the Linux operating system (an open source version of Unix). Apple built its own operating system off of Linux, and part of the appeal of the Macintosh for many technical users is that it makes available a Unix-like command line. Windows, on the other hand, uses Microsoft's proprietary DOS system. There are similarities but also differences between the commands available in each environment. However, moving between them only requires remembering a few different terms and commands.

## Accessing the Command Line

In Windows, the interface for the command line is generally known as the "Command Prompt". The easiest way to open a command prompt is to type the `Windows key+X`, followed by `C`. This should open a black window with a command prompt, preceded your current location on the disk. On the Macintosh, the interface is known as the "Terminal", and it can be opened by searching for "terminal". The background will be white, but it will also indicate your location on the disk before the command prompt.

## Understanding File Paths

Before going further, you should have a clear understanding of the architecture of your computer's file storage. This is a hierarchical system in which folders (directories) and files are embedded in in a tree-like structure. In the GUI, you simply double click on a folder's icon to open it and view what is inside. If there is another folder, you double-click on that, and so on down the hierarchy.

On the command line, every file or folder has a **path** relative to the root directory. Each level is indicated by a slash. On Windows, this is a backward slash. On the Mac and in Linux, it is a forward slash. For instance, on Windows, you might open a command prompt and find that it says something like `C:\Users\Scott`. `C:` is the hard drive, and the rest tells you that you are inside a folder called "Scott", which is inside a folder called "Users", which is at the top level of the hierarchy. Whatever commands you run, the computer will assume that they start from this location. On the Mac or in Linux, typing the `pwd` command will tell you the path of your current location. **It is very important to become familiar with file paths before you proceed.**

It is also worth noting that web addresses (URLs) make use of the same system. For instance, `http://iacer.edu.np` is the address to the IACER website's root location. `http://iacer.edu.np/about-us/iacer-overview` refers to a web page `iacer-overview` inside a folder called `about-us`, which is one level below the root. If you had access to the command prompt on IACER's server, you could navigate there using the commands below. (Note: This is true in principle. Some websites use different storage methods and only display file path-like structures in the URL because they make the web address intuitive. This is most likely to be the case for IACER's website.)

## Understanding Commands

Typically, a command will be a word like `print` or an abbreviation like `mkdir` (for "make directory"). Some commands may be followed by arguments. **In this case the command and the argument will always be separated by a space.** It is thus important to recognise what is a command and what is an argument, since leaving the space out will cause an error. Sometimes arguments will require you to provide a "string". This is a sequence of letters and/or numbers such as a file name. Strings are often required to be in quotations marks (single or double).

## Changing Your Location

>Mac and Linux users: Remember to use a forward slash, rather than a backslash when typing the commands below.

To change the command prompt's location in you file structure, use the `cd` (change directory command). The argument for `cd` is a file path. For instance, if you begin at the root `C:` and you want to go to a folder containing the Lexos tool, you might enter `cd C:\Users\Scott\Documents\Lexos`. This is called a full, or **absolute**, path. 

>Tip: In the Windows GUI, you can click on a folder's address bar to get the absolute path to that folder.

If you were in the `C:\Users\Scott` folder, you could use a **relative** path: `cd Documents\Lexos`, which just gives the path relative to the current location.

But how would you get to `C:\Users\Scott` from the `Lexos` folder? You could enter an absolute path. That would work. But you can also move up the hierarchy by typing `cd ..`. If you did that twice, you could move the the `Scott` folder. But you could also move up the hierarchy like this: `cd ..\..` (that is, you could do it with one command).

You should practice moving around your system with the `cd` command. To make the process easier, you should examine what is inside each folder by listing its contents. On Windows, the command to do this is `dir`. On the Mac and Linux, it is `ls`. Try these commands before moving on.

## What Else Can I Do on the Command Line

You can run applications and programming languages from the command line. For instance, your machine probably has a path like `C:\Program Files (x86)\Microsoft Office\Office14` (it may be slightly different on your computer). If you `cd` to that directory, and type `winword.exe`, your copy of Microsoft Word will launch. Likewise, if you have Python installed on your machine, and you type `python`, you will get the Python command prompt where you can run commands in Python. DOS (the command line language used by Windows) and Linux have many built-in commands of their own. The Linux commands are generally more useful to learn because they are used more often in server environments. Generally, the best way to learn is to Google "How do I _____ in Linux" or "How do I ______ in DOS".


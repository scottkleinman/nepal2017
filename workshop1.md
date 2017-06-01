# Workshop 1

## Using the Command Line

To access the command prompt, hold down the `Windows key + X` and then click `C`. Alternatively, hold down the `Windows key + Q` and search for "command prompt". Another way is to type `Windows key + R` to bring up the `Run` box and type `cmd.exe` into the text field.

### Basic Concepts

The **command prompt** refers to the character (`>` on Windows) next to which you type commands on the command line. After a command, hit `Enter` to execute the command. To exit the command prompt, close the window or type the `exit` command.

A **command** consists of a single string of characters (normally a word or abbreviation) followed by one or more **arguments**. Arguments are strings of characters that modify the command's behaviours. They are separated from commands by spaces. For instance, the command `more` displays text. If you want to display the text of a certain file, you might use the filename as an argument: `more filename.txt`. Some arguments are "flags" for instance, `more filename.txt +1` will display starting from the second line. You can generally type `help more` (or use any other command as the argument of `help` to find out what flags are available and what they do).

A **path** is a representation of a location on the system's file storage. This location may be for a file or a folder (directory). All locations are represented relative to the the system's root. In the Macintosh and Linux operating systems, forward slashes are used for this purpose. In Windows, backslashes are used. In Windows the system's root (the hard drive) is typically `C:`. Generally, files are stored in a `Documents` folder assigned to a specific user. So the path to the `Documents` folder might look like `C:\Users\Scott\Documents`.

>Trick: In your normal file explorer, click on the address bar for any folder. You will see the path to that folder. You can even copy and paste it.

### Changing Locations

On Windows, the command prompt will generally open in the `C:\Users\Username` path. To change locations, use the `cd` (change directory) command. Try this:

1. Open a command prompt and look at the path shown to see what your username is.
2. Type `cd Documents`. You should move to the `Documents` folder.
3. To go back, type `cd ..`. This means "go up one level". If you wanted to go up two levels from your current location, you could type `cd ..\..`. Try it, and you should be at the root: `C:`.

### Viewing the Contents of a Directory

To see the contents of a directory, `cd` to that directory and type the `dir` command. If your listing is too long to read, you can paginate it by using `dir|more`. Then hit the space bar to advance each page.

>Trick: On the command line, try hitting the up arrow one or two times. Notice what happens? It cycles through your previous history of commands. This can be a huge time saver.

### Running a Shell Script

Another term for the command line is the **shell**, the interface for interacting with the computer's operating system. In addition to executing simple commands in the shell, you can run "shell script". A **script** is a plain text file that contains a sequence of commands. When a script becomes very long, it tends to be referred to as a **program**, but there is no clear dividing line between the two.

We'll try a simple script. Open an editor and type the following script:

```
@echo off
mkdir dhnepal2017
cd dhnepal2017
@echo This is a test> test.txt
```

Save this as `myscript.bat` in your `Documents` folder. Here's what the script does.

1. `@echo off` tells the shell not to display the effects of each command on the command line. This is optional.
2. `mkdir dhnepal2017` creates a new directory called `dhnepal2017` inside your `Documents` folder.
3. `@echo This is a test> test.txt` creates a new file called `test.txt` and writes the text "This a test" to it.

Once you run this script, you have two choices. You can type `more test.txt` to view the file on the command line, or you can go to your file explorer and double-click on the icon to open it in your editor.

Now try the following variant:

```
@echo off
@echo This is another test> dhnepal2017/test2.txt
```

Save this as `myscript2.bat` in your `Documents` folder. Make sure you are in the `Documents` folder on the command line. `myscript2.bat`. This time, you already have a `dhnepal2017` folder, so you don't need to create it. But you _do_ want to create your file inside that folder. Notice that this script provides the path to the location where the file should be written.

### Relative Paths and Absolute Paths

The path given in the above script is a **relative path**: that is, it specifies the location relative to the current directory. You could also have given the path as `C:\Users\Username\Documents\dhnepal2017`. This full path is known as the **absolute path**. Hopefully, the simple script above demonstrates how important it is to understand file paths so that you can tell the computer where to perform operations.

Note that URLs (web addresses) also work on a similar basis. Your browser requires the absolute path to a file wherever it is housed, but websites may internally reference resources (e.g. the location of an image) using relative paths.

### Why Would I Want to Work on the Command Line?

1. Interacting with the operating system can provide access to some very powerful features.
2. Some software is most easily started or installed from the command line.
3. Programming languages like Python and PHP use file paths, so it is useful to keep in touch with this way of interacting with your file storage.
4. _Sometimes_ it is actually faster to do things from the command line, especially when yu get comfortable with it.

## Using Keyboard Shortcuts

A keyboard shortcut is a faster way of performing an action for which your software has a menu option. For instance, instead of using your mouse or trackpad to select `File > Copy`, just type `Control+C`. Likewise, to paste what you have copied, type `Control+V` (`Control+P` is typically for the "Print" command). Here are some of the more common keyboard commands. You will save a lot of time if you learn to use them.

<table class="table table-striped table-bordered">
<tr><td>`Control + C`</td><td>Copy</td></tr>
<tr><td>`Control + V`</td><td>Paste</td></tr>
<tr><td>`Control + Z`</td><td>Undo</td></tr>
<tr><td>`Control + Y`</td><td>Repeat or Redo</td></tr>
<tr><td>`Control + A`</td><td>Select All</td></tr>
<tr><td>`Control + O`</td><td>Open</td></tr>
<tr><td>`Control + W`</td><td>Close</td></tr>
<tr><td>`Control + F`</td><td>Find</td></tr>
<tr><td>`Control + H`</td><td>Find and Replace</td></tr>
</table>

Some software will have variants on these key combinations, and some software allows you to customise them.

## Setting up a Development Environment

A development environment is a sandbox for testing out applications. Most of the time, this involves running software on your local machine without publishing it to the internet. For applications or files to be visible on the internet, they must be present on an "internet facing" server. Typically, files are "served" to the internet through a language like PHP (which runs the blog software Wordpress) or Python (which is used for many text analysis applications). For this workshop, we will practice setting up development environments, which we will use in later workshops. We will have two goals:

1. Create a working LAMP stack and install the Wordpress blog software.
2. Install Python and run its Jupyter notebooks environment.

Before getting started, make sure that you have downloaded and installed [Sublime Text 3](https://www.sublimetext.com/3). To download it, click on the link appropriate for your system (most Windows users should use the 64 bit version). To install it, double-click the icon in your downloads folder.

### Installing a Local LAMP stack

Wordpress is generally run on a bundle of software packages called LAMP: This stands for **Linux** (the operating system), **Apache** (the web server), **MySQL** (the database), and PHP (the programming language). Typically, Apache is run on a dedicated server machine, but you can run it locally. The **XAMPP** distribution is a complete LAMP package that you can download and install on your laptop.

>As an aside, whilst installing a **local** LAMP stack is pretty easy, installing one on a server is much more difficult. Not only do you need an actual server machine, but you also need to take many security considerations into account and keep the server running to ensure continuous access. This is why many people choose to host their content on commercial internet service providers (ISPs) where the hosting service takes care of these tasks. 

For a complete workflow that takes you through the steps of installing XAMPP and Wordpress, see the separate [Installing Wordpress tutorial](https://github.com/scottkleinman/nepal2017/blob/master/installing_wordpress.md).

### Installing Python

Python is a programming language that is relatively easy to learn and has many built-in or available functions that are particularly useful for digital humanists. It is possible to run it off of a LAMP stack, but this has added complications. Be aware that few ISPs offer PHP and Python in the same environment, so, if you are interested in using both together, this will require a little bit of investigating.

One feature of Python that takes some getting used to is that it contains a minimal number of features out of the box. If you want more features, you have to install Python **packages** (also called "modules" or "libraries") from the command line and then import these packages into your scripts. However, many packages are so common and useful that it makes sense to install them when you install Python. Various companies have released Python "distributions", which are applications that install Python along with the most popular packages. We will install the Anaconda distribution, which is very easy to do. Then we will install some missing packages to get some practice.

1. Visit the Anaconda downloads page on the web: [http://continuum.io/downloads](http://continuum.io/downloads). Where it says "Download
Anaconda Now", click the icon for your operating system.
2. This next bit is where most people run into problems. Stare at the screen until you see a blue button that say **64-bit Graphical Installer**. Immediately above, it should say **Python 2.7**. Click the **blue** button to download the installer. If you have a very old computer, you may have to use the Windows 32-bit version, in which case, you should click the smaller link below. If you are unsure whether your computer is running a 32-bit or a 64-bit version of Windows, follow the instructions at [https://support.microsoft.com/en-us/kb/827218](https://support.microsoft.com/en-us/kb/827218).
3. Double-click the installer application icon (it will be called something like `Anaconda2-4.1.1-Windows-x86_64.exe`) and follow the instructions on the screen.

> *Note: The installation location is not important; however, make sure that 
> you leave the option to `Update the PATH variable` checked. This will ensure 
> that Windows knows that you want to use the Anaconda distribution of Python 
> when you launch _Lexos_. This is especially important if you already have a 
> different version of Python installed.*

When the process is complete, select **Finish** to finish the installation of Anaconda.

You should now verify that we have installed it correctly. To do this, open a Windows Command Prompt and enter the command `python -V`. This will display the version of Python your are running. You should see a response that looks like: `Python 2.7.12 :: Anaconda 4.1.1 (64-bit)`. If you do not see `:: Anaconda 4.1.1` then you did not update your PATH variable during the Anaconda installation. It may be useful to uninstall Anaconda and try to install it again, following the instructions above. To uninstall Anaconda, go to your computer's Control Panel, choose `Add or Remove Programs` or `Uninstall a program` and then select `Python 2.7 (Anaconda)`.

Now let's try installing some additional packages. Anaconda comes with a package installer called `pip`. Generally, you can install packages from the command line with the command `pip install PACKAGENAME`. You can update the package any time with `pip install -U PACKAGENAME`. We'll try installing three packages used by the text analysis software Lexos, which we'll be employing in later workshops. Enter the following commands, one by one (you may have to wait for each to install):

```python
pip install gensim
pip install chardet
pip install natsort
```

**Note: Packages are downloaded from the internet, so you must have internet access for this process to work.**

Now we'll try a couple of options to get you familiar with Python. First, we'll run a Python command on the command line. In the command prompt, type `python` and his enter. Notice that the command prompt character changes to `>>>`? That means that you no longer have access to the operating system's shell. Instead, the command prompt is expecting you to enter Python commands. So let's try it. Type `print("Hello world")` and hit `Enter`. The response should be "Hello world". You've just run some (not very complicated) Python code. To get out of the Python prompt, type `exit()` and hit `Enter`. The system's shell prompt will return.

You can do anything you want in Python from the command line, but it is not a very good environment to work in. One of the most popular environments today is **Jupyter notebooks** (formerly called **iPython notebooks**), which allow you to run Python in your web browser. Jupyter notebooks comes pre-installed in Anaconda. To start it, type `jupyter notebook` or `ipython notebook` at the command prompt. There will be a short pause, and then a web browser will open with the Jupyter notebooks home page. **Do not close the command prompt window.**

On the Jupyter notebook home page, find the **New** button at the top right and select `Python 2`. Another tab will open containing an empty cell. Click on it and type `print("Hello world")`. Then click `Shift + Enter`. You will see "Hello world" in the response. The advantage over doing this in the command line is that you can enter multiple commands and execute them all at once. Let's write a quick Python script to demonstrate this. In the next cell, type

```Python
fruit = ['oranges', 'apples', 'bananas', 'grapes']
for item in fruit:
    print("item")
```

We won't play with Python further at this stage, so let's concentrate on how to shut down Jupyter notebooks. First, the notebook you are working in is automatically kept open on your computer for the next time you start Jupyter notebooks. Since this is just a test, we don't want to save it. In the `File` menu, select `Close and Halt`. This will close the window and delete the notebook. You still have to quit the Jupyter notebooks process. To do this, go back to the command prompt where you started it and type `Control + C`. You may have to do it more than once.


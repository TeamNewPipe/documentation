# About This Documentation


The documentation you are currently reading was written using [mkdocs](https://www.mkdocs.org/). It is a tool that will generate a static website based on [markdown](https://www.markdownguide.org/) files. Markdown has the advantage that it is simple to read and write, and that there are several tools that can translate a markdown file into languages like HTML or LaTeX.

## Installation

Mkdocs is written in [Python](https://www.python.org/) and is distributed through the Python internal package manager [pip](https://pypi.org/project/pip/), thus you need to get python and pip running on your operating system first.

## Windows

1. Download the latest [Python3](https://www.python.org/downloads/windows/) version.
2. When running the setup program, make sure to tick, "Add Python 3.x to PATH".
![check_path](img/check_path.png)
3. Install Python.
4. Open PowerShell or cmd.exe and type: `pip3 install mkdocs`.

## MacOS

MacOS already includes Python, however, pip is still missing. The easiest and most nondestructive way is to install the MacOS package manager, [homebrew](https://brew.sh/index_de), first. The advantage of homebrew is that it will only modify your home directory, and not the root dir, so your OS will not be tampered with.

1. Install [homebrew](https://brew.sh/index_de).
2. Install Python from Homebrew, which will also install pip. Enter this command:
`brew install python`.
3. Install mkdocs:
`pip3 install mkdocs`.

## Linux/*BSD

Linux/*BSD also has Python pre-installed. Most distributions also contain pip by default. If it is not installed, you may need to figure out how to install pip3 through the package manager of your system.

1. Install pip3 with these commands according to distributions: 
    - __Ubuntu/Mint__: `apt install python3-pip`
    - __Fedora/CentOS__: `sudo dnf install python3-pip`
    - __Arch/Manjaro__: `sudo pacman -S python-pip`
    - __openSuse__: `sudo zypper install python-pip`
    - __*BSD__: You are already advanced enough to know how you can force the bits on your disk to become pip by meditating upon it.
2. Run `pip3 install mkdocs` to install mkdocs only for the current user,
or run `sudo pip3 install mkdocs` to install mkdocs systemwide. Last one has the higher chance to work properly.

## Android/ChromeOS
This might sound funny, but according to the growing amount of Chromebooks and Android tablets with keyboards, this might actually be useful.

1. Install the [Termux App](https://termux.com/) from [F-Droid](https://f-droid.org/packages/com.termux/).
2. Launch Termux and type `apt update`
3. Install Python and Git with the command: `apt install git python`
4. Install mkdocs with `pip install mkdocs`.

From herein, everything will be the same as on Desktop. If you want to edit the files, you can (besides vim or emacs which are available through Termux) use your preferred text editor on Android. This is possible by opening the files with the Termux integration of the build in android file manager:

![termux_files](img/termux_files.png)

## Updating
Sometimes, mkdocs changes the way of how it serves, or the syntax will differ. This is why you should make sure to always run the latest version of mkdocs. To check, simply run `pip3 install --upgrade mkdocs` or `sudo pip3 install --upgrade mkdocs` if you installed pip system wide on a Linux/BSD* system.

## Using mkdocs
In order to extend this documentation, you have to clone it from its [GitHub repository](https://github.com/TeamNewPipe/documentation). When you clone it, you will find a [mkdocs.yml](https://github.com/TeamNewPipe/documentation/blob/master/mkdocs.yml) file, and a [docs](https://github.com/TeamNewPipe/documentation/tree/master/docs) directory inside. The yaml file is the [config file](https://www.mkdocs.org/user-guide/configuration/) while in the directory docs the documentation files are stored. [Here](https://www.mkdocs.org/user-guide/writing-your-docs/) is a guide about how to use mkdocs.

## Write and Deploy
If you are writing a documentation page and want a live preview of it, you can enter the root directory of this documentation project, and then run `mkdocs serve` this will start the mkdocs internal web server on port `8000`. So all you have to do is type `localhost:8000` into the address bar of your browser, and here you go. If you modify a file, and save it, mkdocs will reload the page and show you the new content.

If you want to deploy the page so it will be up to date at the [GitHub pages](https://teamnewpipe.github.io/documentation/), simply type `mkdocs gh-deploy`. However, please be aware that this will not push your changes to the `master` branch of the repository. So, you still have to commit and push your changes to the actual git repository of this documentation. _Please be aware that only privileged maintainers can do this._

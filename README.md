# mangahub
Winter Of Code project under FOSS@BPHC

## Project Description
A software that provides a suitable interface for reading Manga. As of now, it can only display/detect sources **already downloaded by the user** onto his/her machine. There are plans to include an in-built download suite in the future.

Supported Operating Systems: Windows, Linux

Language used: Python 2.7.13

External Modules: kivy, kivy-garden
## Installation Instructions
#### Prerequisites
The user should have Python 2.7.* ( >= 2.7.13 ) already installed on their machine. Both the Python install directory and Scripts directory should be included in the PATH environment variable.

Also ensure that pip is installed. This is installed by default during your Python installation, unless specified otherwise. To check if pip is present on your system, enter the following into the Command line.
```
> pip --version
```
If pip is present, the version number will be printed. Else, an error is thrown.

A working internet connection is required to install additional modules using the provided installation scripts.
### Windows
 Open Command Prompt by pressing Win+R and typing "cmd" (without quotes) and then pressing enter.

 Navigate to the directory where you have downloaded the application by executing:
```
> cd path_to_directory
```
Run the installation file by typing the following command and then pressing Enter.
```
> install_windows.bat
```
As the required external modules are downloaded and installed, output will be visible on the prompt. If any **permission denied** errors are encountered, open Command Prompt As Administrator and try again.

### Linux
Open Terminal (Ctrl+Alt+T) and navigate to the directory where the application has been downloaded by executing:
```
$ cd path_to_directory
```
Now execute:
```
$ ./install.sh
```
If this does not work, ensure that the file is executable by running:
```
$ chmod +x install.sh
```

## Usage
Open the application by running the 'main.py' file. This can be done either by double-clicking it, or through Command Prompt / Terminal, based on you Python installation settings.

Detailed help for usage is provided within the application itself.

## Examples
An 'Examples' folder is included in this repo for testing purposes wihout needing you to download any Manga by yourself.

To import, Add the 'Manga' folder as a source. **NOT** the Examples folder itself.

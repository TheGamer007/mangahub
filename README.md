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

## Usage and Help
#### Opening/Running the application
Open the application by running the 'main.py' file. This can be done either by double-clicking it, or through Command Prompt / Terminal, based on your Python installation settings.

#### File Tree Structure
The application asks the user to add directories as 'sources' and then scans these automatically in order to populate a list of series. The structure currently supported is as follows:
```
>source_dir/
  >series_dir_1
  >series_dir_2
    >chapter_dir_1
    >chapter_dir_2
      img_1
      img_2
```
The source directory contains each series as a separate directory. Each of the series directories will have chapters in separate directories. The chapter directories contain the image files corresponding to pages of the Manga.

Since all the user does is add the source directory, names of series and chapters are taken from the respective directory names. As far as ordering is concerned, the list of directories are natural sorted, so they can be named anything as long as they appear in proper order within your file browser.

#### Adding sources
The first time the application is opened, a black screen will be displayed with two buttons at the bottom. Pressing the 'Manage Sources' button opens a dialog that allows adding of new sources. Once a source is added, the series within it will be automatically scanned and displayed on the HomeScreen.
>Note:<br>If the path to a source directory changes, i.e. the previous path does not exist anymore, then the application will ignore the source. This prevents erroneous listings and unexpected crashes.

#### Opening a Chapter
Clicking on a title listed on the HomeScreen opens the SeriesScreen where each chapter is listed. If there are a lot of chapters, it may take a few seconds for the screen to load, so please refrain from clicking multiple times. Clicking on a chapter opens an ImageViewScreen positioned at the first page of the sekected chapter.

#### Navigating while reading
Buttons, Spinners and keys can be used to smoothly navigate while reading. Pressing either 'left' / 'a' or 'right' / 'd' turns the page in the corresponding direction. The large buttons to the side are used to skip to the previous and next chapters.
>Note:<br>
While this is a Manga, the image files will likely be ordered in left-to-right fashion and not in the traditional right-to-left. Hence, pressing 'right' moves to the next page and 'left' to the previous one.<br>
An optional setting might be added in future updates to allow for right-to-left navigation as well.

#### Bookmarking
An 'Add Bookmark' button is provided on top of the page in the ImageViewScreen to allow for easy bookmarking of important pages. A short description can be added to distinguish the bookmark and specify context.<br>
In order to view all bookmarked pages, press the 'View Bookmarks' button on the bottom of the HomeScreen. Pressing any of the listed items will automatically open the corresponding page.

**At any point in the application (except when Dialogs are open), pressing the 'Backspace' key will return the user to the HomeScreen.**

## Samples
A folder with samples for testing the application can be found [here](https://drive.google.com/drive/folders/0B7lmcKGeLFy2T1VRU2Y4WTJfb28?usp=sharing). Download the 'MangaHub Samples' folder and add it as the source. You should now be able to see a series named 'Detective Conan' listed on the HomeScreen.

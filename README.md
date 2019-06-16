# youtube_downloader
It simplifies downloading youtube videos and playlist using youtube-dl and idm. Right now it only downloads the best quality video, audio combination from youtube.


## Installation
This program has three additional dependencies: youtube-dl, pyperclip, and internet download manager. Make sure you have all of them.

```bash
pip install youtube-dl
pip install pyperclip
```
And youtube-dl and internet download manager need to be in the path. Installing youtube-dl using pip automatically adds it to path, so now you only need to add internet download manager to path.

## Usage
Run the program using

```bash
python youtube.py
```
The program continuously(at 1 sec interval to be precise) checks the clipboard for change and if the contents in the clipboard is youtube video url, then the process begins and within 30-40 secs idm will get the link and a idm dialog box will pop up. If the link is playlist it might take 2-3 minutes before idm gets all the links. 

Just copy the youtube video url and the download should begin. Feel free to change the code and make it your own.

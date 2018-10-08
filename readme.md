# Tone Master #

* Authors: Hrvoje Katić
* Download [stable version][1]

Welcome to Tone Master! I've created this little NVDA add-on just for fun, but also for you to have fun while using it.

I always wanted to create musical tunes with NVDA, rather than just listening to NVDA's progress and error beeps. However, it's not too easy to do, so first I wanted to make it easier. That's why I wrote Tone Master. Just imagine how it could be for you to hear NVDA playing song by Mozzart or Beethoven, or may be greatest hits by Rolling Stones. Although the final result sounds like those ringtones on old mobile phones, it may still be funny.

Tone Master simplifies process of playing tone sequences by implementing tone data files. These files can be edited with your favorite text editor and then saved for playback with NVDA. Read on for instructions!

## Tone data files

Before you can play your first musical tune with Tone Master, you have to create and load your tone data file first. Tone data files are simply text files with .tdf extension. Tone Master uses these files for processing and playing back tone sequences. To create tone data file for Tone Master to be able to play it successfully, you have to follow simple rules described below.

1. Each line in .tdf file *must* contain three parameters separated by colon (:). The first parameter is tone pitch, the second parameter is tone duration, and the third one is the time of silence between each tone. All three parameters are necessary to specify, otherwise Tone Master will not be able to play your tone data.
2. Pitch and duration parameters must be specified as signed integers, and the silence must be specified as floating point real value.
3. A hash sign (#) at the beginning of any line in .tdf file will be treeted as a comment and will be ignored by Tone Master.

Example: Play a sequence of 3 tones

1500:100:0.5

1000:100:0.09

500:100:0.7

In this example, the first tone in a sequence has a pitch of 1500, duration of 100 and 0.5 silence. The second tone's pitch is 1000, duration is 100, and the silence is 0.09. The last tone in a sequence has pitch 500, duration 100, and the silence is 0.7.

Note, the silence parameter is necessary to specify even if you think that it's not, because if not specified, NVDA will override the previous tone by the next one, and you will get unexpectable results. That's why I made it to be necessary.

To get more familiar with tone data files syntax, please view and try editing the example file included with this add-on. It's located in the "tones" subfolder, where all your .tdf files must be located as well.

## Shortcut keys

* Alt+NVDA+T: Plays currently loaded tone data if everything is ok.
* Alt+Shift+NVDA+T: Stops playback for currently loaded tone data if any tone data is playing.
* Alt+NVDA+N: Creates and opens a new blank tone data file in Notepad for editing.
* Alt+NVDA+L: Opens a dialog that lets you choose one of your available tone data files to be loaded for playback.
* Alt+NVDA+E: Opens currently loaded tone data file in Notepad for editing.
* Alt+NVDA+O: Opens a folder with tone data files where you should also save them in order to be located by Tone Master.

## Other notes

You can also create, edit and load tone data files, or open tones folder where these files are located by going into the NVDA menu, Tools SubMenu, Tone Master SubMenu.

When the dialog for creating new tone data file is displayed, type the name without .tdf extension. The extension will be automatically added by Tone Master. If no name was specified, Tone Master will use the default name "untitled.tdf". Tone Master will automatically create and load new file for you, and it will also be opened in Notepad for editing. Press Escape at the file name prompt to cancel new file creation.

Note: Tone Master uses Notepad for editing tone data files, since it comes with Windows by default and therefore any computer should have it available.

When the dialog for loading tone data file is open, use the arrow keys to select a file to load and then press Enter. Press Escape to cancel loading.

When you open a folder with .tdf files, you can then load them in your text editor for viewing or editing. However, in order to hear your results on the fly, I highly recommend you to load the file into Tone Master first if possible. Then you can edit the file, save your progress, and after each save you can use play command to hear your last result.

## Changes for 1.3

* Fixed: Fixed compatibility issue with newer NVDA versions.

## Changes for 1.2

* Fixed: Addressed major issue where selecting an empty tone data, then selecting another one and trying to play it results in tone data not being played.

## Changes for 1.1

* Added: An option to create new tone data file and open it in Notepad for editing.
* Added: An option to edit currently loaded tone data file in Notepad.
* Improved: Error messages are now more user-friendly.
* Improved: Certain addon features such as opening tones folder or editing tone data files in Notepad are now disallowed on secure screens.
* Improved: User will be notified by NVDA if tone data playback is stopped.
* Fixed: Disallowed playback of tone data while the one is already playing.

## Changes for 1.0

* Initial release.

[1]: https://github.com/nvdaaddons/toneMaster/releases/download/v1.3/toneMaster-1.3.nvda-addon

# Tone Master
# Author: Hrvoje Katic
# Copyright 2016, released under GPL.
# Allows you to create and play tone sequences by using tone data files.

import globalPluginHandler
from logHandler import log
import codecs
import os
import glob
import subprocess
import tones
import ui
import time
import threading
import gui
import wx
import globalVars
import addonHandler
addonHandler.initTranslation()

loaded=None
playing=False

class player(threading.Thread):
	# The tone playback must be performed in a separate thread to avoid lagging.

	def __init__(self, toneData):
		threading.Thread.__init__(self)
		self.toneData=toneData

	def run(self):
		global playing
		tone=0
		for p in self.toneData:
			if not playing: break
			try:
				tone+=1
				tones.beep(int(p[0]), int(p[1]))
				time.sleep(float(p[2]))
			except ValueError:
				# Translators: This message will be spoken by NVDA if there's an error with tone data playback.
				wx.CallAfter(gui.messageBox, _("""Woops! I found an error at tone number %d while playing tone data file, some values are missing or incorrect.
Please correct any errors and try again.
Bad syntax: %s"""%(tone, ':'.join(p))), _("Error"), style=wx.OK | wx.CENTER|wx.ICON_ERROR)
				tone=len(self.toneData)
				break
		if tone>=len(self.toneData):
			playing=False

class toneData(object):
	# Used for loading and playing back tone data files.

	def __init__(self, fileName):
		self.fileName=fileName
		self._entries=list()
		fileName=os.path.join(self.fileName)
		if not os.path.isfile(fileName): 
			raise LookupError(fileName)
		f=codecs.open(fileName,"r","utf_8_sig",errors="replace")
		for line in f:
			if line.isspace() or line.startswith('#'):
				continue
			line=line.rstrip('\r\n')
			temp=line.split(":")
			if len(temp)>2:
				self._entries.append(temp)
			else:
				# Translators: This message will be spoken by NVDA if user tries to play the tone data, but tone data that is currently loaded contains errors.
				wx.CallAfter(gui.messageBox, _("""Error while parsing line in tone data file, please correct any errors and try again.
The line containing errors: %s"""%line), _("Error"), style=wx.OK | wx.CENTER|wx.ICON_ERROR)
				log.warning("can't parse line '%s'"%line)
		log.debug("Loaded %d entries." % len(self._entries))
		f.close()

	def play(self):
		global playing
		tonePlayer=player(self._entries)
		tonePlayer.start()
		playing=True

class loadToneDataDialog(gui.SettingsDialog):
	# Translators: Title of the dialog for loading tone data files.
	title=_("Load Tone Data")

	def __init__(self, parent):
		super(loadToneDataDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		# Translators: Help message for Load Tone Data dialog.
		helpLabel=wx.StaticText(self, label=_("Select tone data file you wish to load for playing:"))
		helpLabel.Wrap(self.GetSize()[0])
		sizer.Add(helpLabel)
		fileListSizer=wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A label for files list in Load Tone Data dialog.
		fileListLabel=wx.StaticText(self, label=_("Files"))
		fileListSizer.Add(fileListLabel)
		self._filesListbox=wx.ListBox(self, choices=[os.path.split(path)[-1] for path in glob.glob(os.path.join(os.path.dirname(__file__), 'tones', '*.tdf'))])
		fileListSizer.Add(self._filesListbox)
		sizer.Add(fileListSizer)
		self._filesListbox.SetSelection(0)

	def postInit(self):
		self._filesListbox.SetFocus()

	def onOk(self, event):
		global loaded
		super(loadToneDataDialog, self).onOk(event)
		loaded=self._filesListbox.GetStringSelection()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: Script category for Tone Master commands in input gestures dialog.
	scriptCategory=_("Tone Master")

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		if globalVars.appArgs.secure:
			return
		self.menu=gui.mainFrame.sysTrayIcon.toolsMenu
		self.tmMenu=wx.Menu()
		self.tmSubMenu=self.menu.AppendSubMenu(self.tmMenu,
		# Translators: The name of Tone Master add-on submenu.
		_("Tone Master"),
		# Translators: The tooltip text for Tone Master add-on submenu.
		_("Tone data player"))
		self.newToneDataItem=self.tmMenu.Append(wx.ID_ANY,
		# Translators: The name for an item of Tone Master add-on submenu that opens a new blank tone data file in Notepad for editing.
		_("&New tone data file"),
		# Translators: The tooltip text for an item of Tone Master add-on submenu that opens a new blank tone data file in Notepad for editing.
		_("Opens a new blank tone data file in Notepad for editing"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.OnNewToneData, self.newToneDataItem)
		self.loadToneDataItem=self.tmMenu.Append(wx.ID_ANY,
		# Translators: The name for an item of Tone Master add-on submenu that opens a dialog for loading tone data files.
		_("&Load tone data file..."),
		# Translators: The tooltip text for an item of Tone Master add-on submenu that opens a dialog for loading tone data files.
		_("Opens a dialog for loading tone data files to play"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.OnLoadToneDataDialog, self.loadToneDataItem)
		self.editToneDataItem=self.tmMenu.Append(wx.ID_ANY,
		# Translators: The name for an item of Tone Master add-on submenu that opens currently loaded tone data file in Notepad for editing.
		_("&Edit tone data file"),
		# Translators: The tooltip text for an item of Tone Master add-on submenu that opens currently loaded tone data file in Notepad for editing.
		_("Opens currently loaded tone data file in Notepad for editing"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.OnEditToneData, self.editToneDataItem)
		self.openTonesFolderItem=self.tmMenu.Append(wx.ID_ANY,
		# Translators: The name for an item of Tone Master add-on submenu that opens a folder with tone data files.
		_("&Open folder with tone data files"),
		# Translators: The tooltip text for an item of Tone Master add-on submenu that opens a folder with tone data files.
		_("Opens a folder with tone data files in file explorer"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.OnOpenTonesFolder, self.openTonesFolderItem)

	def terminate(self):
		try:
			self.menu.RemoveItem(self.tmSubMenu)
		except wx.PyDeadObjectError:
			pass

	def OnNewToneData(self, evt):
		if globalVars.appArgs.secure:
			return
		global loaded
		newToneDataDialog=wx.TextEntryDialog(gui.mainFrame,
		# Translators: A message which prompts the user to enter tone data file name in New Tone Data File dialog.
		_("Enter file name:"),
		# Translators: Title of the dialog for creating new tone data file.
		_("New Tone Data File"))
		res=newToneDataDialog.ShowModal()
		if res==wx.ID_OK:
			if newToneDataDialog.GetValue():
				loaded=newToneDataDialog.GetValue().encode('mbcs')+'.tdf'
			else:
				loaded='untitled.tdf'
			newFile=os.path.join(os.path.dirname(__file__), 'tones', loaded)
			f=codecs.open(newFile,"w","utf_8_sig",errors="replace") # create a new file
			f.close() # close the file in Python since we will be using Notepad for editing
			p=subprocess.Popen(["notepad.exe", newFile]) # finally open newly created file in Notepad

	def OnLoadToneDataDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(loadToneDataDialog)

	def OnEditToneData(self, evt):
		if globalVars.appArgs.secure:
			return
		if loaded is None:
			# Translators: This message will be spoken by NVDA if user tries to edit tone data, but no tone data was loaded.
			ui.message(_("Please load tone data file first."))
			return
		editFile=os.path.join(os.path.dirname(__file__), 'tones', loaded)
		p=subprocess.Popen(["notepad.exe", editFile])

	def OnOpenTonesFolder(self, evt):
		if globalVars.appArgs.secure:
			return
		try:
			os.startfile(os.path.join(os.path.dirname(__file__), 'tones'))
		except WindowsError:
			pass

	def script_playToneData(self, gesture):
		global playing
		if loaded is None:
			# Translators: This message will be spoken by NVDA if user tries to play the tone data, but no tone data was loaded.
			ui.message(_("Please load tone data file first."))
			return
		if playing:
			return
		t=toneData(os.path.join(os.path.dirname(__file__), 'tones', loaded))
		playing=True
		t.play()
	# Translators: Input help mode message for Play Tone Data command.
	script_playToneData.__doc__=_("Plays currently loaded tone data if everything is ok.")

	def script_stopToneData(self, gesture):
		global playing
		playing=False
	# Translators: Input help mode message for Stop Tone Data playback command.
	script_stopToneData.__doc__=_("Stops playback for currently loaded tone data if any tone data is playing.")

	def script_newToneData(self, gesture):
		wx.CallAfter(self.OnNewToneData, None)
	# Translators: Input help mode message for New Tone Data command.
	script_newToneData.__doc__=_("Opens a new blank tone data file in Notepad for editing.")

	def script_editToneData(self, gesture):
		wx.CallAfter(self.OnEditToneData, None)
	# Translators: Input help mode message for Edit Tone Data command.
	script_editToneData.__doc__=_("Opens currently loaded tone data file in Notepad for editing.")

	def script_loadToneData(self, gesture):
		wx.CallAfter(self.OnLoadToneDataDialog, None)
	# Translators: Input help mode message for Load Tone Data command.
	script_loadToneData.__doc__=_("Opens a dialog that lets you choose one of your available tone data files to be loaded for playback.")

	def script_openTonesFolder(self, gesture):
		wx.CallAfter(self.OnOpenTonesFolder, None)
	# Translators: Input help mode message for Open Tones Folder command.
	script_openTonesFolder.__doc__=_("Opens a folder with tone data files where you should also save them in order to be located by Tone Master.")

	__gestures={
		"kb:NVDA+Alt+T":"playToneData",
		"kb:NVDA+Alt+Shift+T":"stopToneData",
		"kb:NVDA+Alt+N":"newToneData",
		"kb:NVDA+Alt+E":"editToneData",
		"kb:NVDA+Alt+L":"loadToneData",
		"kb:NVDA+Alt+O":"openTonesFolder"
	}

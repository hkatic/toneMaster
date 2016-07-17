# Tone Master
# Author: Hrvoje Katic
# Copyright 2016, released under GPL.
# Allows you to create and play tone sequences by using tone data files.

import globalPluginHandler
from logHandler import log
import codecs
import os
import glob
import tones
import ui
import time
import threading
import gui
import wx
import addonHandler
addonHandler.initTranslation()

loaded=None
playing=True

class player(threading.Thread):
	# The tone playback must be performed in a separate thread to avoid lagging.

	def __init__(self, toneData):
		threading.Thread.__init__(self)
		self.toneData=toneData

	def run(self):
		for p in self.toneData:
			if not playing: break
			try:
				tones.beep(int(p[0]), int(p[1]))
				time.sleep(float(p[2]))
			except ValueError:
				# Translators: This message will be spoken by NVDA if there's an error with tone data playback.
				ui.message(_("Woops! I found an error while playing tone data file, some values are missing or incorrect. Please correct any errors and try again."))

class toneData(object):
	# Used for loading and playing back tone data files.

	def __init__(self, fileName):
		self.fileName=fileName
		self._entries=list()
		fileName=os.path.join(self.fileName)
		if not os.path.isfile(fileName): 
			raise LookupError(fileName)
		f = codecs.open(fileName,"r","utf_8_sig",errors="replace")
		for line in f:
			if line.isspace() or line.startswith('#'):
				continue
			line=line.rstrip('\r\n')
			temp=line.split(":")
			if len(temp)>2:
				self._entries.append(temp)
			else:
				# Translators: This message will be spoken by NVDA if user tries to play the tone data, but tone data that is currently loaded contains errors.
				ui.message(_("Error in tone data file, please correct any errors and try again. The line containing errors: %s"%line))
				log.warning("can't parse line '%s'"%line)
		log.debug("Loaded %d entries." % len(self._entries))
		f.close()

	def play(self):
		tonePlayer=player(self._entries)
		tonePlayer.start()

class loadToneDataDialog(gui.SettingsDialog):
	# Translators: Title of the dialog for loading tone data files.
	title = _("Load Tone Data")

	def __init__(self, parent):
		super(loadToneDataDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		# Translators: Help message for Load Tone Data dialog.
		helpLabel=wx.StaticText(self, label=_("Select tone data file you wish to load for playing:"))
		helpLabel.Wrap(self.GetSize()[0])
		sizer.Add(helpLabel)
		fileListSizer=wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A label for files list in Load Tone Data dialog.
		fileListLabel = wx.StaticText(self, label=_("Files"))
		fileListSizer.Add(fileListLabel)
		self._filesListbox = wx.ListBox(self, choices=[os.path.split(path)[-1] for path in glob.glob(os.path.join(os.path.dirname(__file__), 'tones', '*.tdf'))])
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
	scriptCategory = _("Tone Master")

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu=gui.mainFrame.sysTrayIcon.toolsMenu
		self.tmMenu=wx.Menu()
		self.tmSubMenu=self.menu.AppendSubMenu(self.tmMenu,
		# Translators: The name of Tone Master add-on submenu.
		_("Tone Master"),
		# Translators: The tooltip text for Tone Master add-on submenu.
		_("Tone data player"))
		self.loadToneDataItem=self.tmMenu.Append(wx.ID_ANY,
		# Translators: The name for an item of Tone Master add-on submenu that opens a dialog for loading tone data files.
		_("&Load tone data file..."),
		# Translators: The tooltip text for an item of Tone Master add-on submenu that opens a dialog for loading tone data files.
		_("Opens a dialog for loading tone data files to play"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.OnLoadToneDataDialog, self.loadToneDataItem)
		self.openTonesFolderItem = self.tmMenu.Append(wx.ID_ANY,
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

	def OnLoadToneDataDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(loadToneDataDialog)

	def OnOpenTonesFolder(self, evt):
		try:
			os.startfile(os.path.join(os.path.dirname(__file__), 'tones'))
		except WindowsError:
			pass

	def script_playToneData(self, gesture):
		global playing
		if loaded==None:
			# Translators: This message will be spoken by NVDA if user tries to play the tone data, but no tone data was loaded.
			ui.message(_("Please load tone data file first."))
			return
		t=toneData(os.path.join(os.path.dirname(__file__), 'tones', loaded))
		playing=True
		t.play()
	script_playToneData.__doc__=_("Plays currently loaded tone data if everything is ok.")

	def script_stopToneData(self, gesture):
		global playing
		playing=False
	script_stopToneData.__doc__=_("Stops playback for currently loaded tone data if any tone data is playing.")

	def script_loadToneData(self, gesture):
		wx.CallAfter(self.OnLoadToneDataDialog, None)
	script_loadToneData.__doc__=_("Opens a dialog that lets you choose one of your available tone data files to be loaded for playback.")

	def script_openTonesFolder(self, gesture):
		wx.CallAfter(self.OnOpenTonesFolder, None)
	script_openTonesFolder.__doc__=_("Opens a folder with tone data files where you should also save them in order to be located by Tone Master.")

	__gestures={
		"kb:NVDA+Alt+T":"playToneData",
		"kb:NVDA+Alt+Shift+T":"stopToneData",
		"kb:NVDA+Alt+L":"loadToneData",
		"kb:NVDA+Alt+O":"openTonesFolder"
	}

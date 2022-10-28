import wx
class Markdown(wx.Frame):
	def __init__(self):
		super().__init__(None, title="Create Markdown")
		self.Center()
		self.activeFile = None
		p = wx.Panel(self)	
		wx.StaticText(p, -1, "Markdown")
		self.htmls = wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL)
		open = wx.Button(p, -1, "open")
		open.Bind(wx.EVT_BUTTON, self.onOpen)
		save = wx.Button(p, -1, "save")
		save.Bind(wx.EVT_BUTTON, self.onSave)
		closs = wx.Button(p, -1, "&Close the open file")
		closs.Bind(wx.EVT_BUTTON, self.onbacks)

		clos = wx.Button(p, -1, "back")
		clos.Bind(wx.EVT_BUTTON, self.onback)
		self.contextSetup()
		self.Show()
	def onhh(self,event):
		h1 = wx.GetTextFromUser("Write the heading number from 1 to 6")
		h2 = wx.GetTextFromUser("Write the the words")
		if h1 =="1":
			self.htmls.write(f"""# {h2}
""")
		elif h1 =="2":
			self.htmls.write(f"""## {h2}
""")
		elif h1 =="3":
			self.htmls.write(f"""### {h2}
""")
		elif h1 =="4":
			self.htmls.write(f"""#### {h2}
""")
		elif h1 =="5":
			self.htmls.write(f"""##### {h2}
""")
		elif h1 =="6":
			self.htmls.write(f"""###### {h2}
""")
		else:
			wx.MessageBox("error","error")
	def onp(self,event):
		p1 = wx.GetTextFromUser("write the paragraph")
		self.htmls.write(f"""{p1}
""")
	def onl(self,event):
		link1 = wx.GetTextFromUser("write the name of link")
		link2 = wx.GetTextFromUser("write the URL")
		self.htmls.write(f"""({link1})[{link2}]
""")
	def onOpen(self, event):
		openDialog = wx.FileDialog(self, "open")
		result = openDialog.ShowModal()
		if result == wx.ID_CANCEL:
			return

		path = openDialog.Path
		filename = openDialog.Filename
		file = open(path, "r", encoding="utf-8")
		self.content.Value = file.read()
		file.close()
		self.Title = f"{filename} - notepad"
		self.activeFile = path

	def onSave(self, event):
		if not self.activeFile:
			saveDialog = wx.FileDialog(self, "save", style=wx.FD_SAVE)
			saveDialog.Wildcard = "md files(.md(|*.md)"
			result = saveDialog.ShowModal()
			if result == wx.ID_CANCEL:
				return
			path = saveDialog.Path
			filename = saveDialog.Filename
		else:
			path = self.activeFile
		file = open(path, "w", encoding="utf-8")
		file.write(self.htmls.Value)
		file.close()
		self.activeFile = path
		self.htmls.SetModified(False)
		wx.MessageBox(f"saved in {path}","file")
	def onback(self, event):
		self.Close()
	def onbacks(self, event):
		self.activeFile = None
	def contextSetup(self):
		context = wx.Menu()
		hs = context.Append(-1, "&heading")
		ps = context.Append(-1, "&paragraph")
		ls = context.Append(-1, "&link")
		self.Bind(wx.EVT_MENU, self.onhh,hs)
		self.Bind(wx.EVT_MENU, self.onp,ps)
		self.Bind(wx.EVT_MENU, self.onl,ls)
		self.htmls.Bind(wx.EVT_CONTEXT_MENU, lambda event: self.PopupMenu(context))



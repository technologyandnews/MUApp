import pyperclip
import webbrowser
import wx
class blindapps (wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="download apps")
		self.Center()
		self.activeFile = None
		p = wx.Panel(self)
		link="none"
		linkp=""
		self.system= wx.Choice(p , -1,choices=["windows"])
		self.ca= wx.Choice(p , -1)
		self.list1= wx.Choice(p , -1)
		self.list2= wx.Choice(p , -1)
		self.list3= wx.Choice(p , -1)
		self.list4= wx.Choice(p , -1)
		self.list5= wx.Choice(p , -1)
		self.list6= wx.Choice(p , -1)
		self.list7= wx.Choice(p , -1)
		self.list8= wx.Choice(p , -1)
		self.list9= wx.Choice(p , -1)
		self.list10= wx.Choice(p , -1)
		self.link= wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL + wx.TE_READONLY)
		self.link.Value=link
		download= wx.Button(p, -1, "&download app")
		self.Bind(wx.EVT_BUTTON, lambda event: webbrowser.open_new(link), download)
		downloadbage= wx.Button(p, -1, "download &page")
		self.Bind(wx.EVT_BUTTON, lambda event: webbrowser.open_new(linkp), downloadbage)
		copy= wx.Button(p, -1, "&copy link")
		self.Bind(wx.EVT_BUTTON, lambda event: 			pyperclip.copy(link), copy)
		save= wx.Button(p, -1, "&save link ")
		self.system.Bind(wx.EVT_CHOICE, self.onS)
		 #self.ca.Bind(wx.EVT_CHOICE, self.onCa)
		 #self.list1.Bind(wx.EVT_CHOICE, self.onL1)
		 #self.list2.Bind(wx.EVT_CHOICE, self.onL2)
		 #self.list3.Bind(wx.EVT_CHOICE, self.onL3)
		 #self.list4.Bind(wx.EVT_CHOICE, self.onL4)
		 #self.list5.Bind(wx.EVT_CHOICE, self.onL5)





		self.Show()
	def onS(self, event):
			self.ca.Set(["screen readers","screen recorders","microsoft products","tools","text processing","Audio and video players ","internet prowsers","download files","protection","video editing and streaming programs","audio editing","communication and mail management","files copying and burning","File compression/decompression","Other apps"])
		if self.system.Value== "windows":
			self.ca.Set(["screen readers","screen recorders","microsoft products","tools","text processing","Audio and video players ","internet prowsers","download files","protection","video editing and streaming programs","audio editing","communication and mail management","files copying and burning","File compression/decompression","Other apps"])

			self.ca.Set(["screen readers","screen recorders","microsoft products","tools","text processing","Audio and video players ","internet prowsers","download files","protection","video editing and streaming programs","audio editing","communication and mail management","files copying and burning","File compression/decompression","Other apps"])













app = wx.App()
blindapps()
app.MainLoop()
import TextToSpeech
import notepad
import SearchMultipleSites
import RandomSelection
import SimpleCalculator
import LirnBraillesForBlind
import html
import md
import extract
import wx
class blindapps (wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="MUapp")
		self.Center()
		p = wx.Panel(self)
		notep = wx.Button(p, -1, "Notepad")
		SearchMultipleSite = wx.Button(p, -1, "SearchMultipleSites")
		textt = wx.Button(p, -1, "Text to speach")
		randomSelection = wx.Button(p, -1, "RandomSelection")
		SimpleCalculat= wx.Button(p, -1, "SimpleCalculator")
		LirnBrailleForBlind= wx.Button(p, -1, "LirnBraillesForBlind")
		htmls= wx.Button(p, -1, "Create HTML")
		mds= wx.Button(p, -1, "Create Markdown")
		extraction= wx.Button(p, -1, """extract links or "text" """)
		self.Show()
		self.Bind(wx.EVT_BUTTON, lambda event: notepad.Notepad(), notep)
		self.Bind(wx.EVT_BUTTON, lambda event: SearchMultipleSites.SearchMultipleSites(), SearchMultipleSite)
		self.Bind(wx.EVT_BUTTON, lambda event: TextToSpeech.texttospeech(), textt)
		self.Bind(wx.EVT_BUTTON, lambda event: RandomSelection.RandomSelection(), randomSelection)
		self.Bind(wx.EVT_BUTTON, lambda event: SimpleCalculator.SimpleCalculator(), SimpleCalculat)
		self.Bind(wx.EVT_BUTTON, lambda event: LirnBraillesForBlind.LirnBraillesForBlind(), LirnBrailleForBlind)
		self.Bind(wx.EVT_BUTTON, lambda event: html.html(), htmls)
		self.Bind(wx.EVT_BUTTON, lambda event: md.Markdown(), mds)
		self.Bind(wx.EVT_BUTTON, lambda event: extract.extract(), extraction)

app = wx.App()
blindapps()
app.MainLoop()
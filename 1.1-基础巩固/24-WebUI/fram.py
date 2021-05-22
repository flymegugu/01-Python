# coding=utf-8
import wx 
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="事件触发",size=(600,500))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,label="请点击ok按钮",pos=(110,20))
        b = wx.Button(parent=panel,label='ok',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,b)
    def on_click(self,event):
        self.statictext.SetLabelText('hello,world')
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()
#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        quit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        about = helpMenu.Append(wx.ID_ABOUT, 'About', 'About application')
        menubar.Append(fileMenu, '&File')
        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, quit)
        self.Bind(wx.EVT_MENU, self.loadAbout, about)

        self.SetSize((300, 200))
        self.SetTitle('Tri-Peaks')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

    def loadAbout(self, e):
    	wx.MessageBox('Tri-Peaks\nÞróun Hugbúnaðar vor 2014\nHópur 30:\nDaníel Sandjárn\nKjartan B. Rough\nDaníel Heimsson\nFunky Oak\nHans Pétursson', 'About', 
        wx.OK | wx.ICON_INFORMATION)


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()

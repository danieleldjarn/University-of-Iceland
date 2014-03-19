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
        new = fileMenu.Append(wx.ID_NEW, 'New game', 'Start new game')
        quit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        highscore = helpMenu.Append(wx.ID_VIEW_LIST, 'Highscores', 'Show highscores')
        about = helpMenu.Append(wx.ID_ABOUT, 'About', 'About application')
        menubar.Append(fileMenu, '&File')
        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.Start, new)
        self.Bind(wx.EVT_MENU, self.OnQuit, quit)
        self.Bind(wx.EVT_MENU, self.loadHighscore, highscore)
        self.Bind(wx.EVT_MENU, self.loadAbout, about)

        self.SetSize((800, 600))
        self.SetTitle('Tri-Peaks')
        self.SetBackgroundColour((1,83,9))
        self.Centre()
        self.Show(True)
        
    def Start(self, e):
        self.SetTitle('New game')


    def OnQuit(self, e):
        self.Close()

    def loadHighscore(self, e):
        self.SetTitle('Highscore')


    def loadAbout(self, e):
    	wx.MessageBox('Tri-Peaks\nÞróun Hugbúnaðar vor 2014\nHópur 30:\nDaníel Sandjárn\nKjartan B. Rough\nDaníel Heimsson\nFunky Oak\nHans Pétursson', 'About', 
        wx.OK)


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()

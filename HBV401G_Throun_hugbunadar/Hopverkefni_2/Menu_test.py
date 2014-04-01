#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import sys

class Highscores(wx.Frame):
    def __init__(self, parent, id, title,time =-1,show=True):
        wx.Frame.__init__(self, parent, id, title, size=(330, 230))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self, -1)

        if time != -1:
            self.checkForHighscore(time)
        hs = self.getScoreList()

        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'nr.', width=25)
        self.list.InsertColumn(1, 'name', width=225)
        self.list.InsertColumn(2, 'time', wx.LIST_FORMAT_RIGHT, 80)

        count = 1
        for i in hs:
            index = self.list.InsertStringItem(sys.maxint, str(count))
            nafn = ""
            for j in range(len(i)-1):
                nafn += i[j]+" "
            self.list.SetStringItem(index, 1, nafn)
            self.list.SetStringItem(index, 2, i[-1])
            count += 1
            if count >10:
                break

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)
        
        self.Centre()
        self.Show(show)

    #opnar highscores file og skilar gildum úr honum í röðuðum lista
    def getScoreList(self):
        import os.path
        if not os.path.isfile("highscores"):
            highscorefile = open("highscores", "w+")
        else:
            highscorefile = open("highscores")
        temp = []
        hslist = []
        temp += highscorefile.readlines()
        highscorefile.close()
        for i in temp:
            hslist.append(i.split())
        hslist = sorted(hslist, key = lambda x: x[-1]) 
        return hslist

    #athugar hvort time kemst í top 10. ef já skrifar það inn
    def checkForHighscore(self,time):
        if self.returnScore(time):
            self.setHighscore(time)

    #skilar true ef time kemst í top 10
    def returnScore(self,time):
        temp = []
        temp = self.getScoreList()
        ScoreListLength = 9
        if len(temp) <= ScoreListLength:
            return True
        elif time <= float(temp[ScoreListLength][-1]):
            return True
        else:
            return False

    #skrifar highscore í út í skjal
    def setHighscore(self,time):
        import os.path
        if not os.path.isfile("highscores"):
            highscorefile = open("highscores", "w+")
        else:
            highscorefile = open("highscores", "a")
        
        #popup til að sækja nafn á sigurvegara
        dlg = wx.TextEntryDialog(None,'What is your name?','You\'ve got a new highscore!', '')
        popup = dlg.ShowModal()
        name = dlg.GetValue()
        dlg.Destroy()
        
        if name != "":
            highscorefile.write(name+" "+str(time)+"\n")
        highscorefile.close()





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
        Highscores(self, -1, 'Highscores')

    def loadAbout(self, e):
    	wx.MessageBox('Tri-Peaks\nÞróun Hugbúnaðar vor 2014\nHópur 26 eða 30:\nDaníel Sandjárn\nKjartan B. Rough\nDaníel Heimsson\nFunky Oak\nHans Óli', 'About', 
        wx.OK)


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()



#on win:       Highscores(self, -1, 'Highscores',time)

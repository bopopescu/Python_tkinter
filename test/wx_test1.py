#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     wx_test1
   Description :
   Author :        Mr.Zhang
   date：          2019/7/26 0026
-------------------------------------------------
   Change Activity:
                   2019/7/26 0026:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'

import wx


class MDIFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, "MDI Parent - www.yiibai.com", size=(600, 400))
        menu = wx.Menu()
        menu.Append(5000, "&New Window")
        menu.Append(5001, "&Exit")
        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=5000)
        self.Bind(wx.EVT_MENU, self.OnExit, id=5001)

    def OnExit(self, evt):
        print("123")
        self.Close(False)

    def OnNewWindow(self, evt):
        win = wx.MDIChildFrame(self, -1, "Child Window")
        win.Show(True)


app = wx.App()
frame = MDIFrame()
frame.Show()
app.MainLoop()
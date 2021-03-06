import sys

import wx                  # This module uses the new wx namespace
from string import Template
import wx.html
import wx.lib.wxpTag

#---------------------------------------------------------------------------

class MyAboutBox(wx.Dialog):
    preamble = \
'''
<html>
<body bgcolor="#FFD33F">
<center><table bgcolor="#80FF80" width="100%%" cellspacing="0"
cellpadding="0" border="5">
<tr>
    <td align="center">
    <h1>GWiz </h1>
    <br>
    Running on Python:$PY_VERSION with wxPyton: $WX_VERSION<br>
    Platform:$WX_PLATFORM<br>
    <p>Copyright 2009</p>
    <p>Authors:</p>
    <p>Kenneth Lerman</p>
    <p>Splash Screen and Hat Icon by Wayne Parks</p>
    <p><font size="-1">Licensed under the <i>GPL</i></font></p>
    <p> <p>
    </td>
</tr>
</table></center>
'''
    postamble = \
'''
<p><wxp module="wx" class="Button">
    <param name="label" value="Okay">
    <param name="id"    value="ID_OK">
</wxp></p>
</html>
'''
    def __init__(self, parent, text):
        wx.Dialog.__init__(self, parent, -1, 'GWiz Help',)
        html = wx.html.HtmlWindow(self, -1, size=(420, -1))
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()

        map = {'PY_VERSION': sys.version.split()[0],
                   'WX_VERSION': wx.VERSION_STRING,
                   'WX_PLATFORM': wx.PlatformInfo[1:]}

#!!!KL modify this to scroll the text so that long help files will be
#supported

        htmlCode = self.preamble + text + self.postamble

        t = Template(htmlCode)
##         print "htmlCode before:%s" % htmlCode
        try:
            htmlCode = t.safe_substitute(map)
        except TypeError:
            #!!!KL safe_substitue seems to throw an exception
##             print "exception TypeError"
            pass
        
##         print "htmlCode after:%s" % htmlCode

        html.SetPage(htmlCode)
        btn = html.FindWindowById(wx.ID_OK)
        ir = html.GetInternalRepresentation()
        html.SetSize( (ir.GetWidth()+25, ir.GetHeight()+25) )
        self.SetClientSize(html.GetSize())
        self.CenterOnParent(wx.BOTH)

#---------------------------------------------------------------------------


if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = MyAboutBox(None)
    dlg.ShowModal()
    dlg.Destroy()
    app.MainLoop()


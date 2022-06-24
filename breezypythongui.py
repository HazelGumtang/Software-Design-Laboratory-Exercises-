import sys
versionNumber = sys.version_info.major
if versionNumber == 3:
    import tkinter
    import tkinter.simpledialog
    Tkinter = tkinter
    tkSimpleDialog = tkinter.simpledialog
else:
    import Tkinter
    import tkSimpleDialog

N = Tkinter.N
S = Tkinter.S
E = Tkinter.E
W = Tkinter.W
CENTER = Tkinter.CENTER
END = Tkinter.END
NORMAL= Tkinter.NORMAL
DISABLED = Tkinter.DISABLED
NONE = Tkinter.NONE
WORD = Tkinter.WORD
VERTICAL = Tkinter.VERTICAL
HORIZONTAL = Tkinter.HORIZONTAL
RAISED = Tkinter.RAISED
SINGLE = Tkinter.SINGLE
ACTIVE = Tkinter.ACTIVE

class EasyFrame(Tkinter.Frame):
    """Represents an application window."""
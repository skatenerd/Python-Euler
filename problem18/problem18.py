Python 2.5.4 (r254:67916, Jan 20 2010, 21:44:03) 
[GCC 4.3.3] on linux2
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.4      ==== No Subprocess ====
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 79, in open_calltip
    self.calltip.showtip(arg_text, sur_paren[0], sur_paren[1])
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 66, in showtip
    self.position_window()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 35, in position_window
    self.parencol))
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 2860, in bbox
    self.tk.call((self._w, 'bbox') + args)) or None
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1033, in _getints
    return tuple(map(getint, self.tk.splitlist(string)))
ValueError: invalid literal for int() with base 10: '(127,'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 35, in <module>
    triangle = makeTriangle(numList)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 11, in makeTriangle
    for line in triangle:
NameError: global name 'triangle' is not defined
>>> 
['75\n', '95 64\n', '17 47 82\n', '18 35 87 10\n', '20 04 82 47 65\n', '19 01 23 75 03 34\n', '88 02 77 73 07 63 67\n', '99 65 04 28 06 16 70 92\n', '41 41 26 56 83 40 80 70 33\n', '41 48 72 33 47 32 37 16 94 29\n', '53 71 44 65 25 43 91 52 97 51 14\n', '70 11 33 28 77 73 17 78 39 68 17 57\n', '91 71 52 38 17 14 91 43 58 50 27 29 48\n', '63 66 04 68 89 53 67 30 73 16 69 87 40 31\n', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\n']
['75\n', '95 64\n', '17 47 82\n', '18 35 87 10\n', '20 04 82 47 65\n', '19 01 23 75 03 34\n', '88 02 77 73 07 63 67\n', '99 65 04 28 06 16 70 92\n', '41 41 26 56 83 40 80 70 33\n', '41 48 72 33 47 32 37 16 94 29\n', '53 71 44 65 25 43 91 52 97 51 14\n', '70 11 33 28 77 73 17 78 39 68 17 57\n', '91 71 52 38 17 14 91 43 58 50 27 29 48\n', '63 66 04 68 89 53 67 30 73 16 69 87 40 31\n', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\n']
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 35, in <module>
    triangle = makeTriangle(numList)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 14, in makeTriangle
    toAdd.append((int(x),0))
ValueError: invalid literal for int() with base 10: ''
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 34, in <module>
    numList  = getStrings("triangle.txt")
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 5, in getStrings
    line.pop()
AttributeError: 'str' object has no attribute 'pop'
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 79, in open_calltip
    self.calltip.showtip(arg_text, sur_paren[0], sur_paren[1])
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 66, in showtip
    self.position_window()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 35, in position_window
    self.parencol))
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 2860, in bbox
    self.tk.call((self._w, 'bbox') + args)) or None
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1033, in _getints
    return tuple(map(getint, self.tk.splitlist(string)))
ValueError: invalid literal for int() with base 10: '(135,'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
fnorb = list("fnorb")
>>> fnorb
['f', 'n', 'o', 'r', 'b']
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
>>> 
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
[[('7', -1), ('5', -1)], [('9', -1), ('5', -1), (' ', -1), ('6', -1), ('4', -1)], [('1', -1), ('7', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('8', -1), ('2', -1)], [('1', -1), ('8', -1), (' ', -1), ('3', -1), ('5', -1), (' ', -1), ('8', -1), ('7', -1), (' ', -1), ('1', -1), ('0', -1)], [('2', -1), ('0', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('8', -1), ('2', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('6', -1), ('5', -1)], [('1', -1), ('9', -1), (' ', -1), ('0', -1), ('1', -1), (' ', -1), ('2', -1), ('3', -1), (' ', -1), ('7', -1), ('5', -1), (' ', -1), ('0', -1), ('3', -1), (' ', -1), ('3', -1), ('4', -1)], [('8', -1), ('8', -1), (' ', -1), ('0', -1), ('2', -1), (' ', -1), ('7', -1), ('7', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('0', -1), ('7', -1), (' ', -1), ('6', -1), ('3', -1), (' ', -1), ('6', -1), ('7', -1)], [('9', -1), ('9', -1), (' ', -1), ('6', -1), ('5', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('2', -1), ('8', -1), (' ', -1), ('0', -1), ('6', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('9', -1), ('2', -1)], [('4', -1), ('1', -1), (' ', -1), ('4', -1), ('1', -1), (' ', -1), ('2', -1), ('6', -1), (' ', -1), ('5', -1), ('6', -1), (' ', -1), ('8', -1), ('3', -1), (' ', -1), ('4', -1), ('0', -1), (' ', -1), ('8', -1), ('0', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('3', -1), ('3', -1)], [('4', -1), ('1', -1), (' ', -1), ('4', -1), ('8', -1), (' ', -1), ('7', -1), ('2', -1), (' ', -1), ('3', -1), ('3', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('3', -1), ('2', -1), (' ', -1), ('3', -1), ('7', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('9', -1), ('4', -1), (' ', -1), ('2', -1), ('9', -1)], [('5', -1), ('3', -1), (' ', -1), ('7', -1), ('1', -1), (' ', -1), ('4', -1), ('4', -1), (' ', -1), ('6', -1), ('5', -1), (' ', -1), ('2', -1), ('5', -1), (' ', -1), ('4', -1), ('3', -1), (' ', -1), ('9', -1), ('1', -1), (' ', -1), ('5', -1), ('2', -1), (' ', -1), ('9', -1), ('7', -1), (' ', -1), ('5', -1), ('1', -1), (' ', -1), ('1', -1), ('4', -1)], [('7', -1), ('0', -1), (' ', -1), ('1', -1), ('1', -1), (' ', -1), ('3', -1), ('3', -1), (' ', -1), ('2', -1), ('8', -1), (' ', -1), ('7', -1), ('7', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('7', -1), ('8', -1), (' ', -1), ('3', -1), ('9', -1), (' ', -1), ('6', -1), ('8', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('5', -1), ('7', -1)], [('9', -1), ('1', -1), (' ', -1), ('7', -1), ('1', -1), (' ', -1), ('5', -1), ('2', -1), (' ', -1), ('3', -1), ('8', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('1', -1), ('4', -1), (' ', -1), ('9', -1), ('1', -1), (' ', -1), ('4', -1), ('3', -1), (' ', -1), ('5', -1), ('8', -1), (' ', -1), ('5', -1), ('0', -1), (' ', -1), ('2', -1), ('7', -1), (' ', -1), ('2', -1), ('9', -1), (' ', -1), ('4', -1), ('8', -1)], [('6', -1), ('3', -1), (' ', -1), ('6', -1), ('6', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('6', -1), ('8', -1), (' ', -1), ('8', -1), ('9', -1), (' ', -1), ('5', -1), ('3', -1), (' ', -1), ('6', -1), ('7', -1), (' ', -1), ('3', -1), ('0', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('6', -1), ('9', -1), (' ', -1), ('8', -1), ('7', -1), (' ', -1), ('4', -1), ('0', -1), (' ', -1), ('3', -1), ('1', -1)], [('0', -1), ('4', -1), (' ', -1), ('6', -1), ('2', -1), (' ', -1), ('9', -1), ('8', -1), (' ', -1), ('2', -1), ('7', -1), (' ', -1), ('2', -1), ('3', -1), (' ', -1), ('0', -1), ('9', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('9', -1), ('8', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('9', -1), ('3', -1), (' ', -1), ('3', -1), ('8', -1), (' ', -1), ('5', -1), ('3', -1), (' ', -1), ('6', -1), ('0', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('2', -1), ('3', -1)]]
>>> 
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
[[('7', -1), ('5', -1)], [('9', -1), ('5', -1), (' ', -1), ('6', -1), ('4', -1)], [('1', -1), ('7', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('8', -1), ('2', -1)], [('1', -1), ('8', -1), (' ', -1), ('3', -1), ('5', -1), (' ', -1), ('8', -1), ('7', -1), (' ', -1), ('1', -1), ('0', -1)], [('2', -1), ('0', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('8', -1), ('2', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('6', -1), ('5', -1)], [('1', -1), ('9', -1), (' ', -1), ('0', -1), ('1', -1), (' ', -1), ('2', -1), ('3', -1), (' ', -1), ('7', -1), ('5', -1), (' ', -1), ('0', -1), ('3', -1), (' ', -1), ('3', -1), ('4', -1)], [('8', -1), ('8', -1), (' ', -1), ('0', -1), ('2', -1), (' ', -1), ('7', -1), ('7', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('0', -1), ('7', -1), (' ', -1), ('6', -1), ('3', -1), (' ', -1), ('6', -1), ('7', -1)], [('9', -1), ('9', -1), (' ', -1), ('6', -1), ('5', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('2', -1), ('8', -1), (' ', -1), ('0', -1), ('6', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('9', -1), ('2', -1)], [('4', -1), ('1', -1), (' ', -1), ('4', -1), ('1', -1), (' ', -1), ('2', -1), ('6', -1), (' ', -1), ('5', -1), ('6', -1), (' ', -1), ('8', -1), ('3', -1), (' ', -1), ('4', -1), ('0', -1), (' ', -1), ('8', -1), ('0', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('3', -1), ('3', -1)], [('4', -1), ('1', -1), (' ', -1), ('4', -1), ('8', -1), (' ', -1), ('7', -1), ('2', -1), (' ', -1), ('3', -1), ('3', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('3', -1), ('2', -1), (' ', -1), ('3', -1), ('7', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('9', -1), ('4', -1), (' ', -1), ('2', -1), ('9', -1)], [('5', -1), ('3', -1), (' ', -1), ('7', -1), ('1', -1), (' ', -1), ('4', -1), ('4', -1), (' ', -1), ('6', -1), ('5', -1), (' ', -1), ('2', -1), ('5', -1), (' ', -1), ('4', -1), ('3', -1), (' ', -1), ('9', -1), ('1', -1), (' ', -1), ('5', -1), ('2', -1), (' ', -1), ('9', -1), ('7', -1), (' ', -1), ('5', -1), ('1', -1), (' ', -1), ('1', -1), ('4', -1)], [('7', -1), ('0', -1), (' ', -1), ('1', -1), ('1', -1), (' ', -1), ('3', -1), ('3', -1), (' ', -1), ('2', -1), ('8', -1), (' ', -1), ('7', -1), ('7', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('7', -1), ('8', -1), (' ', -1), ('3', -1), ('9', -1), (' ', -1), ('6', -1), ('8', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('5', -1), ('7', -1)], [('9', -1), ('1', -1), (' ', -1), ('7', -1), ('1', -1), (' ', -1), ('5', -1), ('2', -1), (' ', -1), ('3', -1), ('8', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('1', -1), ('4', -1), (' ', -1), ('9', -1), ('1', -1), (' ', -1), ('4', -1), ('3', -1), (' ', -1), ('5', -1), ('8', -1), (' ', -1), ('5', -1), ('0', -1), (' ', -1), ('2', -1), ('7', -1), (' ', -1), ('2', -1), ('9', -1), (' ', -1), ('4', -1), ('8', -1)], [('6', -1), ('3', -1), (' ', -1), ('6', -1), ('6', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('6', -1), ('8', -1), (' ', -1), ('8', -1), ('9', -1), (' ', -1), ('5', -1), ('3', -1), (' ', -1), ('6', -1), ('7', -1), (' ', -1), ('3', -1), ('0', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('6', -1), ('9', -1), (' ', -1), ('8', -1), ('7', -1), (' ', -1), ('4', -1), ('0', -1), (' ', -1), ('3', -1), ('1', -1)], [('0', -1), ('4', -1), (' ', -1), ('6', -1), ('2', -1), (' ', -1), ('9', -1), ('8', -1), (' ', -1), ('2', -1), ('7', -1), (' ', -1), ('2', -1), ('3', -1), (' ', -1), ('0', -1), ('9', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('9', -1), ('8', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('9', -1), ('3', -1), (' ', -1), ('3', -1), ('8', -1), (' ', -1), ('5', -1), ('3', -1), (' ', -1), ('6', -1), ('0', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('2', -1), ('3', -1)]]
>>> 
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
[[('7', -1), ('5', -1)], [('9', -1), ('5', -1), (' ', -1), ('6', -1), ('4', -1)], [('1', -1), ('7', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('8', -1), ('2', -1)], [('1', -1), ('8', -1), (' ', -1), ('3', -1), ('5', -1), (' ', -1), ('8', -1), ('7', -1), (' ', -1), ('1', -1), ('0', -1)], [('2', -1), ('0', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('8', -1), ('2', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('6', -1), ('5', -1)], [('1', -1), ('9', -1), (' ', -1), ('0', -1), ('1', -1), (' ', -1), ('2', -1), ('3', -1), (' ', -1), ('7', -1), ('5', -1), (' ', -1), ('0', -1), ('3', -1), (' ', -1), ('3', -1), ('4', -1)], [('8', -1), ('8', -1), (' ', -1), ('0', -1), ('2', -1), (' ', -1), ('7', -1), ('7', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('0', -1), ('7', -1), (' ', -1), ('6', -1), ('3', -1), (' ', -1), ('6', -1), ('7', -1)], [('9', -1), ('9', -1), (' ', -1), ('6', -1), ('5', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('2', -1), ('8', -1), (' ', -1), ('0', -1), ('6', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('9', -1), ('2', -1)], [('4', -1), ('1', -1), (' ', -1), ('4', -1), ('1', -1), (' ', -1), ('2', -1), ('6', -1), (' ', -1), ('5', -1), ('6', -1), (' ', -1), ('8', -1), ('3', -1), (' ', -1), ('4', -1), ('0', -1), (' ', -1), ('8', -1), ('0', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('3', -1), ('3', -1)], [('4', -1), ('1', -1), (' ', -1), ('4', -1), ('8', -1), (' ', -1), ('7', -1), ('2', -1), (' ', -1), ('3', -1), ('3', -1), (' ', -1), ('4', -1), ('7', -1), (' ', -1), ('3', -1), ('2', -1), (' ', -1), ('3', -1), ('7', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('9', -1), ('4', -1), (' ', -1), ('2', -1), ('9', -1)], [('5', -1), ('3', -1), (' ', -1), ('7', -1), ('1', -1), (' ', -1), ('4', -1), ('4', -1), (' ', -1), ('6', -1), ('5', -1), (' ', -1), ('2', -1), ('5', -1), (' ', -1), ('4', -1), ('3', -1), (' ', -1), ('9', -1), ('1', -1), (' ', -1), ('5', -1), ('2', -1), (' ', -1), ('9', -1), ('7', -1), (' ', -1), ('5', -1), ('1', -1), (' ', -1), ('1', -1), ('4', -1)], [('7', -1), ('0', -1), (' ', -1), ('1', -1), ('1', -1), (' ', -1), ('3', -1), ('3', -1), (' ', -1), ('2', -1), ('8', -1), (' ', -1), ('7', -1), ('7', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('7', -1), ('8', -1), (' ', -1), ('3', -1), ('9', -1), (' ', -1), ('6', -1), ('8', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('5', -1), ('7', -1)], [('9', -1), ('1', -1), (' ', -1), ('7', -1), ('1', -1), (' ', -1), ('5', -1), ('2', -1), (' ', -1), ('3', -1), ('8', -1), (' ', -1), ('1', -1), ('7', -1), (' ', -1), ('1', -1), ('4', -1), (' ', -1), ('9', -1), ('1', -1), (' ', -1), ('4', -1), ('3', -1), (' ', -1), ('5', -1), ('8', -1), (' ', -1), ('5', -1), ('0', -1), (' ', -1), ('2', -1), ('7', -1), (' ', -1), ('2', -1), ('9', -1), (' ', -1), ('4', -1), ('8', -1)], [('6', -1), ('3', -1), (' ', -1), ('6', -1), ('6', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('6', -1), ('8', -1), (' ', -1), ('8', -1), ('9', -1), (' ', -1), ('5', -1), ('3', -1), (' ', -1), ('6', -1), ('7', -1), (' ', -1), ('3', -1), ('0', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('1', -1), ('6', -1), (' ', -1), ('6', -1), ('9', -1), (' ', -1), ('8', -1), ('7', -1), (' ', -1), ('4', -1), ('0', -1), (' ', -1), ('3', -1), ('1', -1)], [('0', -1), ('4', -1), (' ', -1), ('6', -1), ('2', -1), (' ', -1), ('9', -1), ('8', -1), (' ', -1), ('2', -1), ('7', -1), (' ', -1), ('2', -1), ('3', -1), (' ', -1), ('0', -1), ('9', -1), (' ', -1), ('7', -1), ('0', -1), (' ', -1), ('9', -1), ('8', -1), (' ', -1), ('7', -1), ('3', -1), (' ', -1), ('9', -1), ('3', -1), (' ', -1), ('3', -1), ('8', -1), (' ', -1), ('5', -1), ('3', -1), (' ', -1), ('6', -1), ('0', -1), (' ', -1), ('0', -1), ('4', -1), (' ', -1), ('2', -1), ('3', -1)]]
>>> 
['7', '5']

['9', '5', ' ', '6', '4']

['1', '7', ' ', '4', '7', ' ', '8', '2']

['1', '8', ' ', '3', '5', ' ', '8', '7', ' ', '1', '0']

['2', '0', ' ', '0', '4', ' ', '8', '2', ' ', '4', '7', ' ', '6', '5']

['1', '9', ' ', '0', '1', ' ', '2', '3', ' ', '7', '5', ' ', '0', '3', ' ', '3', '4']

['8', '8', ' ', '0', '2', ' ', '7', '7', ' ', '7', '3', ' ', '0', '7', ' ', '6', '3', ' ', '6', '7']

['9', '9', ' ', '6', '5', ' ', '0', '4', ' ', '2', '8', ' ', '0', '6', ' ', '1', '6', ' ', '7', '0', ' ', '9', '2']

['4', '1', ' ', '4', '1', ' ', '2', '6', ' ', '5', '6', ' ', '8', '3', ' ', '4', '0', ' ', '8', '0', ' ', '7', '0', ' ', '3', '3']

['4', '1', ' ', '4', '8', ' ', '7', '2', ' ', '3', '3', ' ', '4', '7', ' ', '3', '2', ' ', '3', '7', ' ', '1', '6', ' ', '9', '4', ' ', '2', '9']

['5', '3', ' ', '7', '1', ' ', '4', '4', ' ', '6', '5', ' ', '2', '5', ' ', '4', '3', ' ', '9', '1', ' ', '5', '2', ' ', '9', '7', ' ', '5', '1', ' ', '1', '4']

['7', '0', ' ', '1', '1', ' ', '3', '3', ' ', '2', '8', ' ', '7', '7', ' ', '7', '3', ' ', '1', '7', ' ', '7', '8', ' ', '3', '9', ' ', '6', '8', ' ', '1', '7', ' ', '5', '7']

['9', '1', ' ', '7', '1', ' ', '5', '2', ' ', '3', '8', ' ', '1', '7', ' ', '1', '4', ' ', '9', '1', ' ', '4', '3', ' ', '5', '8', ' ', '5', '0', ' ', '2', '7', ' ', '2', '9', ' ', '4', '8']

['6', '3', ' ', '6', '6', ' ', '0', '4', ' ', '6', '8', ' ', '8', '9', ' ', '5', '3', ' ', '6', '7', ' ', '3', '0', ' ', '7', '3', ' ', '1', '6', ' ', '6', '9', ' ', '8', '7', ' ', '4', '0', ' ', '3', '1']

['0', '4', ' ', '6', '2', ' ', '9', '8', ' ', '2', '7', ' ', '2', '3', ' ', '0', '9', ' ', '7', '0', ' ', '9', '8', ' ', '7', '3', ' ', '9', '3', ' ', '3', '8', ' ', '5', '3', ' ', '6', '0', ' ', '0', '4', ' ', '2', '3']

>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
['75']

['95', '64']

['17', '47', '82']

['18', '35', '87', '10']

['20', '04', '82', '47', '65']

['19', '01', '23', '75', '03', '34']

['88', '02', '77', '73', '07', '63', '67']

['99', '65', '04', '28', '06', '16', '70', '92']

['41', '41', '26', '56', '83', '40', '80', '70', '33']

['41', '48', '72', '33', '47', '32', '37', '16', '94', '29']

['53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14']

['70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17', '57']

['91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29', '48']

['63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87', '40', '31']

['04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', '60', '04', '23']

>>> 
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
[[('75', -1)], [('95', -1), ('64', -1)], [('17', -1), ('47', -1), ('82', -1)], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
[[('75', -1)], [('95', -1), ('64', -1)], [('17', -1), ('47', -1), ('82', -1)], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
('75', -1)
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
['75', '95 64', '17 47 82', '18 35 87 10', '20 04 82 47 65', '19 01 23 75 03 34', '88 02 77 73 07 63 67', '99 65 04 28 06 16 70 92', '41 41 26 56 83 40 80 70 33', '41 48 72 33 47 32 37 16 94 29', '53 71 44 65 25 43 91 52 97 51 14', '70 11 33 28 77 73 17 78 39 68 17 57', '91 71 52 38 17 14 91 43 58 50 27 29 48', '63 66 04 68 89 53 67 30 73 16 69 87 40 31', '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
[[('75', -1)], [('95', -1), ('64', -1)], [('17', -1), ('47', -1), ('82', -1)], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
('75', -1)
>>> 
('75', -1)
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
75
>>> 
0
0
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 44, in <module>
    print getMaxDist(1,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 40, in getMaxDist
    return max(left[0],right[0])
TypeError: 'int' object is unsubscriptable
>>> 
0
0
0
>>> 
0
0
0
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
('75', -1)
0
0
0
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
[('75', -1)]
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
('75', -1)
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
75
>>> 
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
leftzero
0
0
0
>>> 
leftzero
('75', -1)
0
('75', -1)
('75', -1)
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 42, in <module>
    print getMaxDist(1,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 38, in getMaxDist
    return max(left[0],right[0])
TypeError: 'int' object is unsubscriptable
>>> 
0
('75', -1)
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 44, in <module>
    print getMaxDist(1,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 40, in getMaxDist
    return max(left[0],right[0])
TypeError: 'int' object is unsubscriptable
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
(0, 0)
('75', -1)
75
>>> 
87
>>> 
('35', -1)
('87', -1)
87
>>> 
('99', -1)
('65', -1)
99
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 48, in <module>
    triangle = getMaxDist(1,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 41, in getMaxDist
    triangle[i][j][1]=maxDist
TypeError: 'str' object does not support item assignment
>>> 
5
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 49, in <module>
    triangle = getMaxDist(1,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 42, in getMaxDist
    triangle[i][j][1]=maxDist
TypeError: 'str' object does not support item assignment
>>> 
75
>>> 
75
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 49, in <module>
    triangle = getMaxDist(0,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 26, in getMaxDist
    triangle[0][0][1]=triangle[0][0][0]
TypeError: 'tuple' object does not support item assignment
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
[[(('75', -1), ('75', -1))], [('95', -1), ('64', -1)], [('17', -1), ('47', -1), ('82', -1)], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
[[('75', '75')], [('95', -1), ('64', -1)], [('17', -1), ('47', -1), ('82', -1)], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
>>> 
('95', -1)
Traceback (most recent call last):
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 50, in <module>
    triangle = getMaxDist(1,0,triangle)
  File "/home/dog/Programs/project_euler/problem18/problem18.py", line 43, in getMaxDist
    triangle[i][j][1]=maxDist
TypeError: 'tuple' object does not support item assignment
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
[[('75', '75')], [('95', '7595'), ('64', '7564')], [('17', '9517'), ('47', '9547'), ('82', '6482')], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
[[('75', '75')], [('95', 170), ('64', 139)], [('17', 112), ('47', 142), ('82', 146)], [('18', -1), ('35', -1), ('87', -1), ('10', -1)], [('20', -1), ('04', -1), ('82', -1), ('47', -1), ('65', -1)], [('19', -1), ('01', -1), ('23', -1), ('75', -1), ('03', -1), ('34', -1)], [('88', -1), ('02', -1), ('77', -1), ('73', -1), ('07', -1), ('63', -1), ('67', -1)], [('99', -1), ('65', -1), ('04', -1), ('28', -1), ('06', -1), ('16', -1), ('70', -1), ('92', -1)], [('41', -1), ('41', -1), ('26', -1), ('56', -1), ('83', -1), ('40', -1), ('80', -1), ('70', -1), ('33', -1)], [('41', -1), ('48', -1), ('72', -1), ('33', -1), ('47', -1), ('32', -1), ('37', -1), ('16', -1), ('94', -1), ('29', -1)], [('53', -1), ('71', -1), ('44', -1), ('65', -1), ('25', -1), ('43', -1), ('91', -1), ('52', -1), ('97', -1), ('51', -1), ('14', -1)], [('70', -1), ('11', -1), ('33', -1), ('28', -1), ('77', -1), ('73', -1), ('17', -1), ('78', -1), ('39', -1), ('68', -1), ('17', -1), ('57', -1)], [('91', -1), ('71', -1), ('52', -1), ('38', -1), ('17', -1), ('14', -1), ('91', -1), ('43', -1), ('58', -1), ('50', -1), ('27', -1), ('29', -1), ('48', -1)], [('63', -1), ('66', -1), ('04', -1), ('68', -1), ('89', -1), ('53', -1), ('67', -1), ('30', -1), ('73', -1), ('16', -1), ('69', -1), ('87', -1), ('40', -1), ('31', -1)], [('04', -1), ('62', -1), ('98', -1), ('27', -1), ('23', -1), ('09', -1), ('70', -1), ('98', -1), ('73', -1), ('93', -1), ('38', -1), ('53', -1), ('60', -1), ('04', -1), ('23', -1)]]
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
[[('75', '75')], [('95', 170), ('64', 139)], [('17', 112), ('47', 142), ('82', 146)], [('18', 35), ('35', 82), ('87', 169), ('10', 92)], [('20', 38), ('04', 39), ('82', 169), ('47', 134), ('65', 75)], [('19', 39), ('01', 21), ('23', 105), ('75', 157), ('03', 68), ('34', 99)], [('88', 107), ('02', 21), ('77', 100), ('73', 148), ('07', 82), ('63', 97), ('67', 101)], [('99', 187), ('65', 153), ('04', 81), ('28', 105), ('06', 79), ('16', 79), ('70', 137), ('92', 159)], [('41', 140), ('41', 140), ('26', 91), ('56', 84), ('83', 111), ('40', 56), ('80', 150), ('70', 162), ('33', 125)], [('41', 82), ('48', 89), ('72', 113), ('33', 89), ('47', 130), ('32', 115), ('37', 117), ('16', 96), ('94', 164), ('29', 62)], [('53', 94), ('71', 119), ('44', 116), ('65', 137), ('25', 72), ('43', 90), ('91', 128), ('52', 89), ('97', 191), ('51', 145), ('14', 43)], [('70', 123), ('11', 82), ('33', 104), ('28', 93), ('77', 142), ('73', 116), ('17', 108), ('78', 169), ('39', 136), ('68', 165), ('17', 68), ('57', 71)], [('91', 161), ('71', 141), ('52', 85), ('38', 71), ('17', 94), ('14', 91), ('91', 164), ('43', 121), ('58', 136), ('50', 118), ('27', 95), ('29', 86), ('48', 105)], [('63', 154), ('66', 157), ('04', 75), ('68', 120), ('89', 127), ('53', 70), ('67', 158), ('30', 121), ('73', 131), ('16', 74), ('69', 119), ('87', 116), ('40', 88), ('31', 79)], [('04', 67), ('62', 128), ('98', 164), ('27', 95), ('23', 112), ('09', 98), ('70', 137), ('98', 165), ('73', 146), ('93', 166), ('38', 107), ('53', 140), ('60', 147), ('04', 44), ('23', 54)]]
>>> 
[[('75', '75')], [('95', 170), ('64', 139)], [('17', 187), ('47', 217), ('82', 221)], [('18', 205), ('35', 252), ('87', 308), ('10', 231)], [('20', 225), ('04', 256), ('82', 390), ('47', 355), ('65', 296)], [('19', 244), ('01', 257), ('23', 413), ('75', 465), ('03', 358), ('34', 330)], [('88', 332), ('02', 259), ('77', 490), ('73', 538), ('07', 472), ('63', 421), ('67', 397)], [('99', 431), ('65', 397), ('04', 494), ('28', 566), ('06', 544), ('16', 488), ('70', 491), ('92', 489)], [('41', 472), ('41', 472), ('26', 520), ('56', 622), ('83', 649), ('40', 584), ('80', 571), ('70', 561), ('33', 522)], [('41', 513), ('48', 520), ('72', 592), ('33', 655), ('47', 696), ('32', 681), ('37', 621), ('16', 587), ('94', 655), ('29', 551)], [('53', 566), ('71', 591), ('44', 636), ('65', 720), ('25', 721), ('43', 739), ('91', 772), ('52', 673), ('97', 752), ('51', 706), ('14', 565)], [('70', 636), ('11', 602), ('33', 669), ('28', 748), ('77', 798), ('73', 812), ('17', 789), ('78', 850), ('39', 791), ('68', 820), ('17', 723), ('57', 622)], [('91', 727), ('71', 707), ('52', 721), ('38', 786), ('17', 815), ('14', 826), ('91', 903), ('43', 893), ('58', 908), ('50', 870), ('27', 847), ('29', 752), ('48', 670)], [('63', 790), ('66', 793), ('04', 725), ('68', 854), ('89', 904), ('53', 879), ('67', 970), ('30', 933), ('73', 981), ('16', 924), ('69', 939), ('87', 934), ('40', 792), ('31', 701)], [('04', 794), ('62', 855), ('98', 891), ('27', 881), ('23', 927), ('09', 913), ('70', 1040), ('98', 1068), ('73', 1054), ('93', 1074), ('38', 977), ('53', 992), ('60', 994), ('04', 796), ('23', 724)]]
>>> import math
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 55, in try_open_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
    self._remove_calltip_window()
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 41, in _remove_calltip_window
    self.calltip.hidetip()
  File "/usr/lib/python2.5/idlelib/CallTipWindow.py", line 126, in hidetip
    self.label.destroy()
AttributeError: 'NoneType' object has no attribute 'destroy'
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 65, in open_calltip
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.5/lib-tk/Tkinter.py", line 1417, in __call__
    return self.func(*args)
  File "/usr/lib/python2.5/idlelib/MultiCall.py", line 151, in handler
    r = l[i](event)
  File "/usr/lib/python2.5/idlelib/CallTips.py", line 62, in refresh_calltip_event
    self.open_calltip(False)
print str(math.factorial(100))

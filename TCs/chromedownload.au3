; ControlFocus("另存为", "","Edit1")
; ControlFocus("title","text",controlID) Edit1=Edit instance 1
; Wait 10 seconds for the Upload window to appear

  WinWait("[CLASS:#32770]","",10)

; Set input focus to the edit control of Upload window using the handle returned by WinWait

  ControlFocus("另存为","","Edit1")

  Sleep(2000)

; Set the File name text on the Edit field

  ControlSetText("另存为", "", "Edit1", "C:\gts\DData\seleniumdemo\autoit-v3-setup")

  Sleep(2000)

; Click on the Open button

  ControlClick("另存为", "","Button2");
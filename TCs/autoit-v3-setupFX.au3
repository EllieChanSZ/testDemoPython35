  WinWait("[CLASS:#32770]","",10)

; Set input focus to the edit control of Upload window using the handle returned by WinWait

  ControlFocus("输入要保存的文件名…","","Edit1")

  Sleep(2000)

; Set the File name text on the Edit field

  ControlSetText("输入要保存的文件名…", "", "Edit1", "C:\gts\DData\seleniumdemo\autoit-v3-setup")

  Sleep(2000)

; Click on the Open button

  ControlClick("输入要保存的文件名…", "","Button2");
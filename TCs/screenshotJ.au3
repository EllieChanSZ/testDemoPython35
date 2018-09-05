; "*.au3" file by autoIt is more easy than "*.ahk" file by autoHotKey
#include

BathCapture()

Func BathCapture()
Sleep(2000)

;load the data file
Local $lines = FileReadToArray("sysmbols.csv")

;locate the window to be captured
Local $hWnd = WinGetHandle("Sublime");this might change to putty or the window title

For $1 = 0 to UBound($lines) - 1

	;loop input for symbol code
	Send($lines[$i])
	Send("{Enter}");this might adapt to the terminal operation,some tab order thing
	; MsgBox($MB_SYSTEMMODAL,$hWnd,$lines[$i]);debug msgbox

	;capture to certain file, the content is from the window we specified
	_ScreenCapture_CaptureWnd($lines[$i] & "_capture.jpg",$hWnd)
	Next

EndFunc

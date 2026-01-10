
def send_message(display_area=None):
    message = "Hello, This is your schedule message."
    print(message)

    if display_area:
        display_area.insert("end", message + "\n")
#        display_area.see("end")
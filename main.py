import sys
import keyboard
from keyboard._keyboard_event import KEY_DOWN, KEY_UP
import json

def action(event):
    if event.event_type == KEY_DOWN:
        message = {
        'type': 'keydown',
        'key': event.name
        }
        sys.stdout.write(json.dumps(message))
        sys.stdout.flush()
    if event.event_type == KEY_UP:
        message = {
            'type': 'keyup',
            'key': event.name
        }
        sys.stdout.write(json.dumps(message))
        sys.stdout.flush()

if __name__ == "__main__":
    keyboard.hook(lambda e: action(e))
    for line in sys.stdin:
        if line.strip() == 'Exit':
            break
        sys.stdout.write(line.strip())
        sys.stdout.flush()

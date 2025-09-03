import keyboard
import yaml
import os
import sys


default_config = {
    'output_key_presses': True,

    'remaps': {
        'a': 'b',
        'b': 'c',
        'right shift': 'h'
    }
}


# Return the config data
def load_config():
    
    # Check if config file exists
    if not os.path.isfile('config.yaml'):
        # Create config file
        print('Config file created: Please edit the config file and restart the program.')
        with open('config.yaml', 'w') as file:
            yaml.safe_dump(default_config, file, default_flow_style=False)
        sys.exit()
    

    # Load config file
    with open('config.yaml', 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(exc)


# Output names of pressed keys
def print_key_presses():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f'"{event.name}" pressed!')


# Remap keys
def remap_keys(remaps):
    for old_key, new_key in remaps.items():
        keyboard.remap_key(old_key, new_key)


def main():
    config = load_config()

    # Remap keys
    remap_keys(config['remaps'])

    # Print key presses
    if config['output_key_presses'] == True:
        print_key_presses()
    else:
        # Stop the script from exiting
        keyboard.wait()


if __name__ == "__main__":
    main()
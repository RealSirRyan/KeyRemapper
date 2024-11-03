import keyboard
import yaml
import time


def load_config():
    with open("src/config.yaml", 'r') as file:
        
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(exc)



def print_key_presses():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f'"{event.name}" pressed!')



def remap_keys(remaps):
    for old_key, new_key in remaps.items():
        keyboard.remap_key(old_key, new_key)



def main():
    config = load_config()

    #Remapping Keys
    remap_keys(config['remaps'])

    #Printing keypresses
    if config['output_key_presses'] == True:
        print_key_presses()
    else:
        #Stop the script from exiting
        keyboard.wait()


main()
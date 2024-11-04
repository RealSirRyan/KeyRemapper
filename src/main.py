import keyboard
import yaml
import os
import shutil
import sys


#Returns the config data
def load_config():
    
    #Checking if a config file exists
    if not os.path.isfile('config.yaml'):
        #Creating a config file
        print('Config file created. Please edit the config file and restart.')
        shutil.copy('src/default_config.yaml', 'config.yaml')
        
        #Fixing ownership (linux)
        if os.geteuid() == 0: #0 corresponds to root
            uid = int(os.environ.get('SUDO_UID'))#Environment variable for the user who ran sudo
            gid = int(os.environ.get('SUDO_GID'))

            os.chown('./config.yaml', uid, gid)
        
        sys.exit()
    

    #Loading the config file
    with open('config.yaml', 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(exc)



#Outputs names of pressed keys
def print_key_presses():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f'"{event.name}" pressed!')



#Remaps keys
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
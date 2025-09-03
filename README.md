Small Python program for remapping keyboard inputs.
For example, you can set it so clicking "A" is registered as "B".

#### Instructions
1) Run the program to generate the config file.
2) In the config file, you can specify your key remaps under the 'remaps' field. Each line represents a different remap. The first value is the key you press on your keyboard, and the second value is the key it is remapped to. For example, `a: b` will remap the 'A' key to 'B'.
While the program is running, it will output the names of any keys you press. You can refer to these names while writing your config. If you want to disable this behaviour, set `output_key_presses` to false.
4) Run the program again. Any remaps specified in the config file should now be active. Close the program to reverse the effect.

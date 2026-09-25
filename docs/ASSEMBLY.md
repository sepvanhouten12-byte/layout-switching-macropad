# assembly notes

these are my current notes for putting the macropad together

i have not finished building the final version yet so some things can still change

## parts

- pcb
- 3d printed case
- raspberry pi pico 2w or 2wh
- 15 switches
- 15 1n4148 diodes
- 3 linear faders
- female headers
- tp4056 charging board
- battery

The full list is in the [bom](../bom.csv)

## build order

1. solder the diodes onto the pcb and check that they face the right way
2. solder the switches
3. check the switch matrix with a multimeter
4. add the three faders
5. add the pico headers and extra headers
6. check power and ground before connecting anything
7. put the pcb in the case and check the usb and charging ports
8. connect the pico and test the firmware before closing the case

The battery and charging circuit need extra care

Check the polarity and make sure there are no shorts before connecting the battery

The firmware still needs to be added

first i want to test each key then the faders and then the layout switching

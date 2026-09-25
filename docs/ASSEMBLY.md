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
- 1x2 pin header for the charging power input

The full list is in the [bom](../bom.csv)

## build order

1. solder the diodes onto the pcb and check that they face the right way
2. solder the switches
3. check the switch matrix with a multimeter
4. add the three faders
5. add the pico headers and extra headers
6. check power and ground before connecting anything
7. **Before mounting the PCB in the case, wire and position the battery and TP4056 as described below.**
8. put the pcb in the case and check the usb and charging ports
9. connect the pico and test the firmware before closing the case

## battery and TP4056 wiring

The battery and charging circuit need extra care. Do this wiring before screwing the PCB into the case:

1. Identify the TP4056 battery pads marked `B+` and `B-`, and the charging-input pads marked `IN+` and `IN-` (sometimes these are labelled `+` and `-`). Do not confuse the battery pads with the input pads.
2. Solder the Li-ion battery's **red wire to `B+`** on the TP4056.
3. Solder the Li-ion battery's **black wire to `B-`** on the TP4056.
4. Solder the 1x2 pin header to the TP4056's charging-power input: one pin to `IN+` and the other pin to `IN-`. The positive pin must go to `IN+` and the ground/negative pin must go to `IN-`. This 1x2 header is the power input for the charger; it is not a replacement for the battery connection on `B+`/`B-`.
5. Inspect every solder joint and use a multimeter to verify that positive and negative are not shorted. Check the header polarity against the schematic before applying power or connecting the battery.

Before closing the case, place the TP4056 onto its two 3D-printed locating pins. Lay the battery in the case in its intended position, with the wires routed so they cannot be pinched. Only after the TP4056 and battery are positioned correctly should you place and screw the PCB into the case. Make sure the PCB, screws, and case cannot press on or damage the battery or its wires.

Check the polarity and make sure there are no shorts before connecting the battery or charger power.

The firmware still needs to be added

first i want to test each key then the faders and then the layout switching

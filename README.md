# layout switching macropad

this project started as a way to learn how to design a switch matrix pcb and get better at cad. i wanted a compact macropad that felt useful, looked clean, and could switch layouts with hardware controls instead of relying on a single static keymap.

it has 15 keys in a 3x5 matrix and 3 faders. the key layout changes depending on the position of the slider, so the same keys can do different things in different modes. the design is built around a custom pcb, a 3d printed case, and a rechargeable battery setup.

## features

- 15 mechanical keys in a 3x5 layout
- 3 faders for layout switching and other controls
- raspberry pi pico 2wh with wifi and pre-soldered headers as the microcontroller
- rechargeable battery setup
- custom pcb
- 3d printed case
- expansion headers for possible future additions
- programmable in circuitpython

## how it works

this macropad uses a 3x5 switch matrix with diodes to reduce ghosting and keep the wiring simple. the three faders are used for layout switching and control, while the main key matrix handles the actual input layer.

current firmware is in [openpad_firmware_v1.py](openpad_firmware_v1.py). the code is written in circuitpython and maps the keys to common shortcuts and media actions. the first fader controls master volume, while the other two faders are currently reserved for future custom actions.

## files

- [JOURNAL.md](JOURNAL.md) - the full project journal
- [docs/ASSEMBLY.md](docs/ASSEMBLY.md) - assembly notes
- [cad/](cad/) - case and other cad files
- [production/](production/) - files needed for pcb production
- [bom.csv](bom.csv) - bill of materials
- [PCB_Z_PCB_macropad-pcb_2026-09-25.json](PCB_Z_PCB_macropad-pcb_2026-09-25.json) - pcb file
- [X_Schematic_macropad-pcb_2026-09-09.pdf](X_Schematic_macropad-pcb_2026-09-09.pdf) - schematic pdf
- [Y_layout%20changing%20macropad%20case.step](Y_layout%20changing%20macropad%20case.step) - case step file
- [openpad_firmware_v1.py](openpad_firmware_v1.py) - circuitpython firmware

## design

the pcb uses a switch matrix with diodes to help prevent ghosting. it is a 4-layer pcb, with the two inner layers used as ground and 3v3 planes.

there are also spare pins on female headers for possible future expansions. the pcb is 120mm x 140mm, and the case is designed to be 3d printed around it.

this design was sanity-checked by a teacher before finalizing the build, and the project was made with a focus on learning practical pcb design, enclosure design, and custom input hardware.

## pictures

### pcb design

<img width="377" height="400" alt="pcb design" src="https://github.com/user-attachments/assets/874ed2a6-cad7-4714-9880-486e902d7965" />

<img width="554" height="405" alt="pcb routing" src="https://github.com/user-attachments/assets/0628d32a-503e-4969-b1e8-06f76351fb0a" />

final build without keycaps/case
<img width="553" height="487" alt="image" src="https://github.com/user-attachments/assets/651567b3-0156-4607-b1c1-93cc81d50501" />

## BOM

| Item | Vendor | Qty | Unit price | Total price |
| --- | --- | ---: | ---: | ---: |
| Raspberry Pi Pico 2WH with WiFi and pre-soldered headers | [Otronic](https://www.otronic.nl/en/raspberry-pi-pico-2wh-with-wifi-and-pre-soldered-headers) | 1 | €11.95 | €11.95 |
| Slider fader potentiometer linear 2-channel 75mm 10k | [Otronic](https://www.otronic.nl/en/slider-fader-potentiometer-linear-2-channel-75mm-10k) | 3 | €2.30 | €6.90 |
| 1N4148 diode | [Otronic](https://otronic.nl/nl/diode-1n4148.html) | 15 | €0.15 | €2.25 |
| 40-pin female header | [Otronic](https://www.otronic.nl/nl/40-pins-header-female-2-54mm) | 3 | €0.65 | €1.95 |
| 3.7V 4000mAh rechargeable LiPo battery | [Otronic](https://www.otronic.nl/en/3-7v-4000mah-rechargeable-lipo-lithium-polymer-flat-battery-606090) | 1 | €10.95 | €10.95 |
| TP4056 charging and protection circuit | [Otronic](https://otronic.nl/nl/lithium-batterij-laadmodule-met-bescherming-tp4056.html) | 1 | €2.40 | €2.40 |
| Gateron KS-3X1 switches | [Gateron](https://www.gateronswitch.com/products/gateron-ks-3x1-full-milky-switch-set) | 1 set | €9.10 | €9.10 |
| 5x custom PCBs | JLCPCB | 1 | €43.30 | €43.30 |
| Shipping and discount | Various | 1 |  | €29.41 |
| **Grand total** |  |  |  | **€115.60** |

For the full bill of materials, see [bom.csv](bom.csv).

## design link

- [Tinkercad case model](https://www.tinkercad.com/things/2xOaqvWOUL6-layout-changing-macropad-case)

## license

this project uses the cc0 license.

# layout switching macropad

this is my custom macropad that switches layouts with faders and is planned to use kmk firmware.

it has 15 keys in a 3x5 matrix and 3 faders. the idea is that one of the faders can switch between layouts, so the same keys can do different things depending on the position of the slider.

## features

- 15 mechanical keys in a 3x5 layout
- 3 faders for layout switching and other controls
- raspberry pi pico 2w as the microcontroller
- rechargeable battery setup
- custom pcb
- 3d printed case
- expansion headers for possible future additions
- programmable in python with kmk

## files

- [JOURNAL.md](JOURNAL.md) - the full project journal
- [docs/ASSEMBLY.md](docs/ASSEMBLY.md) - assembly notes
- [cad/](cad/) - case and other cad files
- [production/](production/) - files needed for pcb production
- [bom.csv](bom.csv) - bill of materials
- [PCB_Z_PCB_macropad-pcb_2026-09-25.json](PCB_Z_PCB_macropad-pcb_2026-09-25.json) - pcb file
- [X_Schematic_macropad-pcb_2026-09-09.pdf](X_Schematic_macropad-pcb_2026-09-09.pdf) - schematic pdf
- [Y_layout%20changing%20macropad%20case.step](Y_layout%20changing%20macropad%20case.step) - case step file

## design

the pcb uses a switch matrix with diodes to help prevent ghosting. it is a 4-layer pcb, with the two inner layers used as ground and 3v3 planes.

there are also spare pins on female headers for possible future expansions. the pcb is 120mm x 140mm, and the case is designed to be 3d printed around it.

## pictures

### pcb design

<img width="377" height="400" alt="pcb design" src="https://github.com/user-attachments/assets/874ed2a6-cad7-4714-9880-486e902d7965" />

<img width="554" height="405" alt="pcb routing" src="https://github.com/user-attachments/assets/0628d32a-503e-4969-b1e8-06f76351fb0a" />

### case design

<img width="476" height="405" alt="case design" src="https://github.com/user-attachments/assets/a90850a4-d9b6-4c30-854f-aa1092fbbbfe" />

<img width="682" height="347" alt="case and pcb design" src="https://github.com/user-attachments/assets/aa54b008-01a3-409d-99cf-728decf4c936" />

## BOM

| Item | Vendor | Qty | Unit price | Total price |
| --- | --- | ---: | ---: | ---: |
| Raspberry Pi Pico 2WH | Otronic | 1 | €11.95 | €11.95 |
| 2 Channel Linear Fader 75mm 10k | Otronic | 3 | €2.30 | €6.90 |
| 1N4148 diode | Otronic | 15 | €0.15 | €2.25 |
| 40-pin female header | Otronic | 3 | €0.65 | €1.95 |
| 3.7V rechargeable 4000mAh LiPo battery | Otronic | 1 | €10.95 | €10.95 |
| TP4056 charging and protection circuit | Otronic | 1 | €2.40 | €2.40 |
| Gateron KS-3X1 switches | Gateron | 1 set | €9.10 | €9.10 |
| 5x custom PCBs | JLCPCB | 1 | €43.30 | €43.30 |
| Shipping and discount | Various | 1 |  | €29.41 |
| **Grand total** |  |  |  | **€115.60** |

For the full bill of materials, see [bom.csv](bom.csv).

## design link

- [Tinkercad case model](https://www.tinkercad.com/things/2xOaqvWOUL6-layout-changing-macropad-case)

## license

this project uses the cc0 license.

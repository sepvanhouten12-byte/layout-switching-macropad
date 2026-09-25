hello this is my repo for my layout switching macropad

here is a short description of my project more info is obtainable in the JOURNAL.md section

so i am making a programmable macropad you can code in python and it uses the raspberry pi pico 2wh from otronic

it will be rechargeable and use bluetooth the keyboard part uses a 3x5 switch matrix and there will be 3 faders

you can program the faders how you want but my plan is to make one of them switch what the matrix does based on its position

it will have a 3d printed case and keycaps and i will use the acetone trick on the keycaps to get them nice and shiny

## files

here are the files for the project

- [cad files](cad/)
- [production files](production/)
- [assembly notes](docs/ASSEMBLY.md)
- [project journal](JOURNAL.md)

The original files are still in the main folder for now because github does not let me move the uploaded binary files with the tools i have here

## pictures

here are some screenshots of the datasheet and the finished pcb gerber

<img width="554" height="405" alt="image" src="https://github.com/user-attachments/assets/745ea788-668e-4b7a-aa24-76ef30555ff5" />

<img width="456" height="427" alt="image" src="https://github.com/user-attachments/assets/7d3516fb-3036-4b6c-b328-384c5336aaa9" />

as microcontroller it uses the raspberry pi pico 2w
and the pcb is 120 by 140 mm

also here is the tinkercad link for my model
https://www.tinkercad.com/things/2xOaqvWOUL6-layout-changing-macropad-case

here is the picture in jlcpcb of the pcb

<img width="671" height="169" alt="image" src="https://github.com/user-attachments/assets/cd122b70-51ae-4a58-b6f8-3e8aa165ad85" />
<img width="675" height="483" alt="image" src="https://github.com/user-attachments/assets/e41a633f-d510-466a-9db5-01d010412bde" />

## design files

- [pcb json file](PCB_Z_PCB_macropad-pcb_2026-09-25.json)
- [schematic pdf](X_Schematic_macropad-pcb_2026-09-09.pdf)
- [case step file](Y_layout%20changing%20macropad%20case.step)
- [bom](bom.csv)

The pcb json file is the file i uploaded again after the reviewer said the old one would not open

I checked that it is in the repository and that it contains the pcb data but i cannot open the file in a pcb editor from github

it should be opened in the same pcb program that exported it

## what still needs doing

i still need to add the gerber zip to the production folder

i also need to check the step file in a cad program and make sure the full assembly opens and all the parts are there

the firmware is not finished yet either

## BOM

| Item Description | Vendor | Qty | Unit Price | Total Price | Link |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Raspberry Pi Pico 2WH | Otronic | 1 | €11.95 | €11.95 | [Link](https://otronic.nl) |
| 2 Channel Linear Fader 75mm 10k | Otronic | 3 | €2.30 | €6.90 | [Link](https://otronic.nl) |
| Diode 1N4148 Max 100V 200mA | Otronic | 15 | €0.15 | €2.25 | [Link](https://otronic.nl) |
| 40 Pins Header Female 2.54mm | Otronic | 3 | €0.65 | €1.95 | [Link](https://otronic.nl) |
| 3.7V Rechargeable 4000mAh LiPo Battery | Otronic | 1 | €10.95 | €10.95 | [Link](https://otronic.nl) |
| TP4056 Lithium Battery Charging and Protection Circuit | Otronic | 1 | €2.40 | €2.40 | [Link](https://otronic.nl) |
| Gateron KS-3X1 Milky Yellow Red Pro Switch Set | Gateron | 1 | €9.10 | €9.10 | [Link](https://gateron.co) |
| 5x Custom PCBs | JLCPCB | 1 | €43.30 | €43.30 | [Link](https://jlcpcb.com) |
| Shipping and discount | Various | 1 |  | €29.41 |  |
| **Grand Total** |  |  |  | **€115.60** |  |

## license

this project uses the cc0 license

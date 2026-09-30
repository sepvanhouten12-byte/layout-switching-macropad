# layout switching macropad

A custom macropad that switches layouts with faders and runs on a Raspberry Pi Pico 2W using KMK firmware.

This is my little hardware + firmware build: a programmable 3x5 keyboard with 3 analog sliders that can change what the keys do depending on the slider position. The idea is basically a tiny, rechargeable, custom keyboard that can act like multiple layouts in one device.

## why I made this

I wanted a macropad that felt more flexible than a normal fixed-key board. Instead of just one set of keybindings, I wanted a device where the physical controls themselves could switch modes. The faders are the main bit here: one slider can shift the keyboard into a different layer, while the other keys can stay the same shape and feel.

So yeah, this is part custom PCB project, part CAD/case project, part firmware project, and all of it is me learning as I go.

## features

- 15 mechanical keys in a 3x5 layout
- 3 faders for layout switching / control
- Raspberry Pi Pico 2W as the controller
- rechargeable battery setup
- custom PCB and 3D printed case
- designed to be programmable in Python with KMK
- expansion headers for future stuff

## project structure

- [JOURNAL.md](JOURNAL.md) — the build log and progress notes
- [docs/ASSEMBLY.md](docs/ASSEMBLY.md) — assembly notes and build details
- [cad/](cad/) — CAD files and case work
- [production/](production/) — production/export files
- [bom.csv](bom.csv) — parts list
- [PCB_Z_PCB_macropad-pcb_2026-09-25.json](PCB_Z_PCB_macropad-pcb_2026-09-25.json) — PCB JSON export
- [X_Schematic_macropad-pcb_2026-09-09.pdf](X_Schematic_macropad-pcb_2026-09-09.pdf) — schematic
- [Y_layout%20changing%20macropad%20case.step](Y_layout%20changing%20macropad%20case.step) — case step model

## current status

This project is still in progress. I’ve reached the point where the PCB, case, and design files are mostly laid out, but the firmware and a few final production steps still need finishing.

Right now the biggest remaining work is:

- adding the final gerber zip to the production folder
- checking the STEP model in CAD and making sure the full assembly is valid
- finishing the firmware and testing the behavior of the fader-based layout switching

## gallery

Here are a few of the key design and build shots from the project:

<img width="554" height="405" alt="project render" src="https://github.com/user-attachments/assets/745ea788-668e-4b7a-aa24-76ef30555ff5" />

<img width="456" height="427" alt="pcb design" src="https://github.com/user-attachments/assets/7d3516fb-3036-4b6c-b328-384c5336aaa9" />

<img width="671" height="169" alt="jlcpcb view" src="https://github.com/user-attachments/assets/cd122b70-51ae-4a58-b6f8-3e8aa165ad85" />

<img width="675" height="483" alt="pcb board" src="https://github.com/user-attachments/assets/e41a633f-d510-466a-9db5-01d010412bde" />

## hardware notes

The board is designed around the Raspberry Pi Pico 2W, with a 3x5 switch matrix and 3 faders. The PCB is 120mm x 140mm, and the case is meant to be 3D printed and assembled around it.

The original files are still sitting in the main folder for now because GitHub is a little annoying about moving uploaded binary files around with the tools I have here.

## BOM

A rough parts list is below. For the full version, check [bom.csv](bom.csv).

| Item | Vendor | Qty | Price |
| --- | --- | ---: | ---: |
| Raspberry Pi Pico 2WH | Otronic | 1 | €11.95 |
| 2 Channel Linear Fader 75mm 10k | Otronic | 3 | €6.90 |
| 1N4148 diode | Otronic | 15 | €2.25 |
| 40-pin female header | Otronic | 3 | €1.95 |
| 3.7V rechargeable LiPo battery | Otronic | 1 | €10.95 |
| TP4056 charging/protection board | Otronic | 1 | €2.40 |
| Gateron KS-3X1 switches | Gateron | 1 set | €9.10 |
| PCB production | JLCPCB | 1 batch | €43.30 |
| Shipping / discount | Various | 1 | €29.41 |
| Total |  |  | €115.60 |

## design links

- Tinkercad model: https://www.tinkercad.com/things/2xOaqvWOUL6-layout-changing-macropad-case

## license

This project uses the CC0 license.

## a quick note

This project is still very much a personal build and a learning project, but that’s kinda the point. I wanted to make something useful, custom, and a little weird in the best way. If you want to see the full journey, the build notes are in [JOURNAL.md](JOURNAL.md).


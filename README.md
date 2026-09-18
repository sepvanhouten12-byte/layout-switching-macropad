hello this is my repo for my layout switching macropad
here is a short description of my project more info is obtainable in the JOURNAL.md section

so I am making a programmable macropad you can code in python and uses the raspberri pi pico 2wh from otronic
it will be rechargable and use Bluetooth the keyboardd part uses a 3x5 switch matrix and there will be 3 faders
you can program the faders how you want but my plan is to make 1 of them switch the things the matrix does based on its position
it will have a 3d printed case and keycaps and I will use the acetone trick on the keycaps to get them nice and shiny

here are some screenshots of the datasheet and the finished PCB gerber

<img width="554" height="405" alt="image" src="https://github.com/user-attachments/assets/745ea788-668e-4b7a-aa24-76ef30555ff5" />

<img width="456" height="427" alt="image" src="https://github.com/user-attachments/assets/7d3516fb-3036-4b6c-b328-384c5336aaa9" />

as microcontroller it uses the raspberri pi pico 2w 
and the pcb is 120 by 140 mm

also here is the tinkercad link for my model
https://www.tinkercad.com/things/2xOaqvWOUL6-layout-changing-macropad-case

here is the picture in jlcpcb of the pcb
<img width="671" height="169" alt="image" src="https://github.com/user-attachments/assets/cd122b70-51ae-4a58-b6f8-3e8aa165ad85" />
<img width="675" height="483" alt="image" src="https://github.com/user-attachments/assets/e41a633f-d510-466a-9db5-01d010412bde" />

BOM

| Item Description | Vendor | Qty | Unit Price | Total Price | Link |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Raspberry Pi Pico 2WH | Otronic | 1 | €11.95 | €11.95 | [Link](https://otronic.nl) |
| 2 Channel Linear Fader 75mm 10k | Otronic | 3 | €2.30 | €6.90 | [Link](https://otronic.nl) |
| Diode 1N4148 Max 100V 200mA | Otronic | 15 | €0.15 | €2.25 | [Link](https://otronic.nl) |
| 40 Pins Header Female 2.54mm (OT156-B126) | Otronic | 3 | €0.65 | €1.95 | [Link](https://otronic.nl) |
| 3.7V Rechargeable 4000mAh LiPo Battery | Otronic | 1 | €10.95 | €10.95 | [Link](https://otronic.nl) |
| TP4056 Lithium Battery Charging & Protection Circuit | Otronic | 1 | €2.40 | €2.40 | [Link](https://otronic.nl) |
| Shipping Costs (Otronic) | Otronic | 1 | €6.99 | €6.99 | - |
| **Otronic Subtotal** | | | | **€43.39** | |
| | | | | | |
| Gateron KS-3X1 Milky Yellow Red Pro Switch Set | Gateron | 1 | €9.10 | €9.10 | [Link](https://gateron.co) |
| Shipping Costs (Gateron) | Gateron | 1 | €4.90 | €4.90 | - |
| **Gateron Subtotal** | | | | **€14.00** | |
| | | | | | |
| 5x Custom PCBs (120x140mm, 4-Layer, 1.6mm, Black) | JLCPCB | 1 | €43.30 | €43.30 | [Link](https://jlcpcb.com) |
| Shipping Costs (JLCPCB) | JLCPCB | 1 | €24.91 | €24.91 | - |
| Coupon Discount | JLCPCB | 1 | -€10.00 | -€10.00 | - |
| **JLCPCB Subtotal** | | | | **€58.21** | |
| | | | | | |
| **Grand Total** | | | | **€115.60** | |

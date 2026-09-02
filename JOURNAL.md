layout switching macropad
https://github.com/sepvanhouten12-byte/layout-switching-macropad 
description: a macropad using kmk firmware that switches layouts with faders 
created_at: "2026-09-1"
september 1st:
(disclaimer: i worked on this project before in macondo
the feedback i got was make a pcb for it so I am taking the feedback and what i learned and now using it here. 
so that is why I'd would have a higher time than normal on this commit)

i chose my parts for the macropad today
15 keyboaard switches 3 faders and 1 potentiometer 
my microcontroller is the raspberri pi 2w 
and my power scource will be a tp4056 with 1 or two 18650 rechargable batteries 
I also thouroghly researched if the parts where compatible and it should be correct

<img width="757" height="167" alt="Screenshot 2026-09-01 14 27 35" src="https://github.com/user-attachments/assets/a719c2ce-44c2-44ac-a114-155d8d987f45" />

total time spent: 4h


# September 2nd: PCB

I started making and wiring the PCB
the keyboard switches are wired and I should only have to do do the faders and potentiometer
the keyboard switches all have diodes so I don't get ghosting 
I am using the matrix wiring method to detect Wich key is pressed to save gpio2 with this gpio2 I also would be able to code later expansions

<img width="546" height="381" alt="image" src="https://github.com/user-attachments/assets/6d23316d-3d26-4f74-8f0c-a66a80007b78" />
<img width="727" height="505" alt="image" src="https://github.com/user-attachments/assets/8674533e-1b98-4d47-9900-4ae6b0279edf" />


**Total time spent: 3h**

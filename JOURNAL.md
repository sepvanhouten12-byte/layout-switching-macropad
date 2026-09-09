layout switching macropad
https://github.com/sepvanhouten12-byte/layout-switching-macropad 
description: a macropad using kmk firmware that switches layouts with faders 
created_at: "2026-09-1"

# September 1st: <chose the parts>

(disclaimer: i worked on this project before in macondo the feedback i got was make a pcb for it so I am taking the feedback and what i learned and now using it here. so that is why I'd would have a higher time than normal on this commit)

i chose my parts for the macropad today 15 keyboaard switches 3 faders and 1 potentiometer my microcontroller is the raspberri pi 2w and my power scource will be a tp4056 with 1 or two 18650 rechargable batteries I also thouroghly researched if the parts where compatible and it should be correct

<img src="https://private-user-images.githubusercontent.com/288311236/645007829-d716fc22-37d1-4842-9090-2f8c1d3232ed.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODgzNzE4NjMsIm5iZiI6MTc4ODM3MTU2MywicGF0aCI6Ii8yODgzMTEyMzYvNjQ1MDA3ODI5LWQ3MTZmYzIyLTM3ZDEtNDg0Mi05MDkwLTJmOGMxZDMyMzJlZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwOTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDkwMlQxNzUyNDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ODQ2MDc2NTlmZDBlN2U4NmY3MzkyZmQ5M2FjZDM4YTg5OTE5N2NjMzMwZjYyMWU4OTVmMWQxNDRkNDNkOGQxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.gKYMVb8MHIlAsDVO_IBL-1B7wzyZiHLFG77WTNQji9g" alt="image"/><img width="991" height="173" alt="image" src="https://github.com/user-attachments/assets/f1b5a9e2-d636-4b56-825f-73bb96bd1dfd" />

**Total time spent: 4h**



# September 2nd: PCB

I started making and wiring the PCB
the keyboard switches are wired and I should only have to do do the faders and potentiometer
the keyboard switches all have diodes so I don't get ghosting 
I am using the matrix wiring method to detect Wich key is pressed to save gpio2 with this gpio2 I also would be able to code later expansions

<img width="546" height="381" alt="image" src="https://github.com/user-attachments/assets/6d23316d-3d26-4f74-8f0c-a66a80007b78" />
<img width="727" height="505" alt="image" src="https://github.com/user-attachments/assets/8674533e-1b98-4d47-9900-4ae6b0279edf" />


**Total time spent: 3h**


# September 3rd: finishing the pcb

i finished the wiring and did the routing of my pcb
I also found out the raspberri pi pico only has 3 analog inputs so I scrapped the potentiometer
and instead I'm doing just the 15 keyboard switches and 3 faders
I also took the spare pins I had and put them on a 22 pin female headers for later expansions
and took a 1x2 header for vsys and  gnd as power input
also I decided to take a 4 layer PCB and make the 2 middle layers planes for gnd and 3v3 

<img width="377" height="400" alt="image" src="https://github.com/user-attachments/assets/874ed2a6-cad7-4714-9880-486e902d7965" />
<img width="554" height="405" alt="image" src="https://github.com/user-attachments/assets/0628d32a-503e-4969-b1e8-06f76351fb0a" />


**Total time spent: 3h**



# September 7th: cad and alignment

today I learned how to set the 0,0 coordinates on my PCB dezing grid so I could align the screw holes nicer 
they are in each corner and 4 mm from the nearest two ends of the pcb
I also started the cad model thee PCB will be mounted on.
last I found out I need to make a minimum of 5 PCBs and it would cost 34-36 euros for production

<img width="476" height="405" alt="image" src="https://github.com/user-attachments/assets/a90850a4-d9b6-4c30-854f-aa1092fbbbfe" />

<img width="682" height="347" alt="image" src="https://github.com/user-attachments/assets/aa54b008-01a3-409d-99cf-728decf4c936" />


**Total time spent: 4h**


# September 8th: cad and working on the case

today I worked more on the case for the PCB and chose to let the raspberry pi 2w stick out of the top a bit because I thought it would be an nice asteatic 

<img width="697" height="459" alt="image" src="https://github.com/user-attachments/assets/2eb2595a-6411-465e-8c06-14ef3bd35f1f" />


**Total time spent: 1h**


# September 9th: bottom of case done

today I finished the bottom part of the case I now have a place for the pico 2w data port a place for the USB c charging port and a hole for the wires of the expansion pin headers to go through but I cant make the top cover yet course I don't know exactly where some of the press able parts for the buttons are and I don't wanna mess t up so I will do that once it is shipped and the parts are here

<img width="520" height="353" alt="image" src="https://github.com/user-attachments/assets/73288c8d-8750-490e-b909-51aaaa7fbac7" />


**Total time spent: 1h**

# September 9th: prices and shipping the project

okay so the project should be ready to ship but before I do that I need to make the shopping karts with the prices also I looked a bit more into my hardware details and found out you cant use kmk with the raspberri pi pico 2w so I will be using other non hack club libraries
but here are the screenshots of my cart 

<img width="1361" height="647" alt="image" src="https://github.com/user-attachments/assets/a9617163-d5d5-4033-9e21-dba34758b7d4" />
the pcb

<img width="736" height="459" alt="image" src="https://github.com/user-attachments/assets/45d3f777-36a3-490f-8c7d-5e51e6790683" />
<img width="1299" height="460" alt="image" src="https://github.com/user-attachments/assets/483429eb-4d66-4da0-9507-2d3491e21e2c" />
otronic cart

<img width="437" height="531" alt="image" src="https://github.com/user-attachments/assets/dbb58403-c35c-4931-bf05-0a2bdbb87884" />
the keyboard swithes

I couldn't get the akko switches cuz they wouldn't have them in stock for like 1 and a half months

total costs: 108.60 euros

**Total time spent: 4h**


layout switching macropad
https://github.com/sepvanhouten12-byte/layout-switching-macropad 
description: a macropad using kmk firmware that switches layouts with faders 
created_at: "2026-09-1"

# September 1st: <journal entry title!>

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

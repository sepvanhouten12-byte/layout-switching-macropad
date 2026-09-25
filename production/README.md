# production files

this folder is for everything needed to make the pcb

- [pcb json file](../PCB_Z_PCB_macropad-pcb_2026-09-25.json)
- [schematic pdf](../X_Schematic_macropad-pcb_2026-09-09.pdf)
- [bom](../bom.csv)

The reviewer specifically asked for production files such as a gerber zip

There is no gerber zip in the repository yet so this still needs to be added manually

export the gerbers from the pcb program and put the zip in this folder

it should include the copper layers the solder mask the silkscreen the board outline and the drill files

name it something simple like

```text
layout-switching-macropad-gerbers.zip
```

The json file is useful as the pcb design file but it does not replace the gerber zip

Before uploading the zip open it in a gerber viewer and check that the board outline holes switches and faders look right

# vhsHackPad

## Project Desc.
vhsHackPad is a custom macropad designed for VHS Hack Club. The project will combine a custom RP2040-based PCB, mechanical keyboard switches, USB-C, and a custom-designed enclosure into a compact programmable keyboard. Instead of using a separate development board, the RP2040 and its supporting electronics will be integrated directly onto the PCB, making the board thinner and more complete as a standalone device.

The PCB will also act as part of the visual design. It includes custom silkscreen artwork and branding such as “vhsHackPad,” “Designed by Preston Nguyen,” and “Made For VHS Hack Club.” The design also experimented with exposed ENIG gold artwork on the PCB rather than treating the circuit board as something that needs to be hidden inside the case.
The enclosure will be designed around the PCB and mechanical switches, with attention given to switch clearance, key spacing, 3D-printing tolerances, and a slide-in assembly that can stay securely together while still being removable.

## Main Features
- Custom RP2040 PCB
- USB-C
- Mechanical keyboard switches
- Programmable macropad firmware
- Custom PCB artwork/silkscreen
- Exposed ENIG/gold decorative PCB features
- Custom CAD enclosure
- Slide-in enclosure/tabs
- 3D printed on a Bambu Lab P1S
- Designed specifically for VHS Hack Club
- JLCPCB/JLCPCB assembly-compatible PCB design

## Process
1. Initial Idea & Planning
You decided to create a new custom macropad for VHS Hack Club. Unlike your previous XIAO RP2040 macropad, this version would have the RP2040 integrated directly onto the PCB.
You also wanted it to be more than just a functional circuit board. The PCB itself would contribute to the appearance of the finished HackPad, with custom artwork and VHS Hack Club branding.
2. PCB Schematic
You designed the electronics in KiCad, including:
- RP2040
- USB-C
- 3.3 V power
- crystal/oscillator circuitry
- keyboard switch GPIO connections
- supporting components
One issue you worked through involved the RP2040's external crystal. The crystal's signal pins needed to connect to the RP2040 oscillator pins while its grounded pads needed to be connected correctly. Fixing that resolved one of the schematic/PCB net problems.
3. PCB Layout & Routing
After finishing the schematic, you placed the components and routed the PCB.
You eventually got the actual electrical design to:
0 unconnected pads
0 footprint errors
0 electrical clearance violations
The remaining DRC warnings were related to silkscreen, rather than broken electrical connections.
That was an important milestone because it meant the board was electrically routed and you could focus on manufacturing and appearance.
4. PCB Artwork
You spent time making the PCB itself look unique rather than leaving it as a normal circuit board.
The board included:
vhsHackPad
Designed by Preston Nguyen
Made For VHS Hack Club
v1.0 // 8.12.26
You also worked on making artwork using exposed copper with ENIG, which would create gold-colored graphics on the finished PCB.
The idea was essentially:
F.Cu artwork + matching F.Mask opening → exposed ENIG gold
while using F.SilkS for white text/details.
You experimented with simplifying artwork so that extremely small details wouldn't disappear during PCB manufacturing.
5. Preparing for PCBA
You designed around JLCPCB assembly, including checking whether components could use their economical assembly process.
This also influenced component choice and PCB layout because you wanted the board to remain reasonably inexpensive rather than requiring unnecessarily expensive assembly.
6. Starting the Enclosure
After the PCB design, you moved into the mechanical side of the HackPad.
You used measurements from your previous macropad as a starting point rather than completely guessing the keyboard dimensions.
One change was the switch openings.
You chose approximately:
15.75 mm × 15.75 mm
for the switch openings because you didn't want the switches to clip tightly into the printed plate.
You then adjusted the spacing around the switches based on the previous macropad.
7. Switch Clearance Problems
While working on the CAD, some dimensions ended up being slightly too tight.
Instead of just scaling the entire enclosure, you adjusted individual clearances so that:
- switches wouldn't bind against the enclosure
- neighboring switches had enough material between them
- the PCB/case could still remain compact
This was especially important because the enclosure would be 3D printed, meaning the CAD dimensions couldn't assume perfectly dimensionally accurate parts.
8. Slide-In Case System
You designed the enclosure to use slide-in tabs rather than simply making two completely separate pieces.
The original openings/tabs involved dimensions around:
0.60 mm and 0.75 mm
but matching the tab exactly to the opening would be too tight on the P1S.
You experimented with reducing the tab dimensions to introduce printing clearance while keeping enough friction that the enclosure wouldn't fall apart.
One of the dimensions you considered was around:
0.45 mm tab for a 0.60 mm opening
and you also adjusted the surrounding wall dimensions as the tab geometry changed.
This was basically a tolerance-design problem: the fit needed to be:
tight enough to stay together → but loose enough to intentionally disassemble.
9. Case Iteration
Changing the tab dimensions affected other dimensions in the enclosure, so you had to go back and adjust wall spacing and clearances.
For example, when geometry changed from around 0.75 mm to 0.60 mm, you recalculated surrounding offsets instead of leaving the original case dimensions unchanged.
This was one of those parts of the project where a tiny dimensional change affected several other features.

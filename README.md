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
Yeah — here’s the same thing rewritten in first person, and kept more like a project-process summary rather than super formal writing.
Brief Project Description
vhsHackPad is a custom mechanical macropad I designed for VHS Hack Club. It uses a custom RP2040-based PCB with USB-C, mechanical switches, custom PCB artwork, and a 3D-printed enclosure. I designed both the electronics and enclosure myself, with the goal of making a compact, programmable macropad that also represents VHS Hack Club.
Project Process / Log
1. Initial Idea & Planning
I started vhsHackPad because I wanted to make a custom macropad specifically for VHS Hack Club. I had already made a macropad before using a XIAO RP2040, so this time I wanted to make it more advanced by putting the RP2040 and all of its supporting components directly onto my own PCB. I also wanted the PCB itself to look good instead of just hiding all of the electronics inside a case.
2. Designing the Schematic
I started designing the electronics in KiCad. I added the RP2040, USB-C, power circuitry, crystal, switches, and all of the supporting components needed for the RP2040 to work. Since I wasn't just using a development board this time, I had to actually figure out how all of the components around the RP2040 connected.
I ran into some problems while doing this, especially with the external crystal and some of the connections around the RP2040. I had to figure out which crystal pins were the actual signal pins and which ones needed to be grounded. After fixing those connections and some other schematic issues, I was able to move on to the actual PCB.
3. PCB Layout & Routing
After finishing the schematic, I started placing all of the components onto the PCB and routing everything together. I had to think about where the switches would go while also finding enough space for the RP2040, USB-C port, and all of the smaller components.
I went through the DRC multiple times while fixing routing and clearance problems. Eventually, I got the actual electrical design down to 0 unconnected pads, 0 footprint errors, and 0 electrical clearance violations. The remaining warnings were mostly related to the silkscreen instead of actual electrical problems.
4. Custom PCB Artwork
I didn't want the PCB to just look like a normal circuit board, so I spent time adding custom artwork and branding to it. I added things like vhsHackPad, Designed by Preston Nguyen, Made For VHS Hack Club, and the board version/date.
I also experimented with using exposed copper and ENIG to make parts of the artwork appear gold on the finished PCB. I had to figure out how the copper, solder mask openings, and silkscreen layers worked together. Some artwork also had to be simplified because really tiny details wouldn't manufacture very well.
5. Preparing the PCB for Manufacturing
While designing the board, I also kept PCB manufacturing and assembly in mind. I checked components and tried to make choices that would keep the board reasonably inexpensive and compatible with economical PCB assembly instead of making it unnecessarily expensive.
I also checked the final PCB for errors and made sure the important electrical issues were fixed before considering it ready to manufacture.
6. Designing the Enclosure
Once the PCB was mostly finished, I started designing the enclosure. I used measurements from my previous macropad as a starting point since I already knew roughly what worked and what didn't.
For the new design, I made the switch openings about 15.75 mm × 15.75 mm because I didn't want the switches to tightly clip into the printed enclosure. I also worked on the spacing between the switches and the edges so everything would fit without making the case unnecessarily large.
7. Fixing Switch & Case Clearances
Some of my original dimensions ended up being a little too tight, so I had to go back and change the clearances. Since the enclosure will be 3D printed, I couldn't design everything with basically zero tolerance and expect it to fit perfectly.
I adjusted the switch openings, spacing, and surrounding walls until there was enough room for everything while still keeping the HackPad compact.
8. Designing the Slide-In Case
I wanted the enclosure pieces to slide together instead of relying on a bunch of screws, so I designed small slide-in tabs and matching openings.
Originally, some of the tabs and openings were around 0.60 mm and 0.75 mm, but I realized that making a tab exactly the same size as its opening would probably make it way too tight after 3D printing. I started experimenting with smaller tab dimensions, including around 0.45 mm for a 0.60 mm opening, to add enough tolerance.
The goal was to make the fit tight enough that the case wouldn't randomly come apart, but not so tight that it would be insanely difficult to separate.
9. Iterating the CAD
Changing the tabs also affected the rest of the case, so I had to keep adjusting nearby dimensions and wall thicknesses. For example, when I changed dimensions from around 0.75 mm to 0.60 mm, I also had to change some of the distances between those features and the walls.
A lot of the enclosure design ended up being small iterations like this—changing one measurement, checking what it affected, and then adjusting the surrounding geometry until everything worked together.
10. Final Design
After working through the electronics, PCB layout, artwork, enclosure, and tolerances, I ended up with a complete vhsHackPad design that combines my custom PCB with a custom enclosure. The project was also a step up from my previous macropad because instead of building around a premade RP2040 development board, I designed the RP2040 electronics directly into the PCB myself.

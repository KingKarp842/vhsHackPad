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

## Creation Process
1. Initial Idea & Planning 
- I started vhsHackPad because I wanted to make a custom macropad specifically for VHS Hack Club. I had already made a macropad before using a XIAO RP2040, so this time I wanted to make it more advanced by putting the RP2040 and all of its supporting components directly onto my own PCB. I also wanted the PCB itself to look good instead of just hiding all of the electronics inside a case.

3. Designing the Schematic
- I started designing the electronics in KiCad. I added the RP2040, USB-C, power circuitry, crystal, switches, and all of the supporting components needed for the RP2040 to work. Since I wasn't just using a development board this time, I had to actually figure out how all of the components around the RP2040 connected.
I ran into some problems while doing this, especially with the external crystal and some of the connections around the RP2040. I had to figure out which crystal pins were the actual signal pins and which ones needed to be grounded. After fixing those connections and some other schematic issues, I was able to move on to the actual PCB.
<img width="1038" height="713" alt="vhsHackPad SCHEMATIC" src="https://github.com/user-attachments/assets/7909ef98-4950-440e-b947-1d233d48576f" />

4. PCB Layout & Routing
- After finishing the schematic, I started placing all of the components onto the PCB and routing everything together. I had to think about where the switches would go while also finding enough space for the RP2040, USB-C port, and all of the smaller components.
I went through the DRC multiple times while fixing routing and clearance problems. Eventually, I got the actual electrical design down to 0 unconnected pads, 0 footprint errors, and 0 electrical clearance violations. The remaining warnings were mostly related to the silkscreen instead of actual electrical problems.
<img width="611" height="578" alt="vhshackpadMCU" src="https://github.com/user-attachments/assets/ed777dcb-c00a-4cb0-a0f7-cb3ed291f26a" />
Figuring out how to route all the parts to the MCU properly
<img width="958" height="779" alt="vhsHackPadRouting" src="https://github.com/user-attachments/assets/ba831b61-ca22-4fd3-ac9a-70ec28a2eaa7" />
Finished Routing
<img width="1002" height="807" alt="vhsHackPad-nosilk" src="https://github.com/user-attachments/assets/093a5f71-54ad-454d-846f-aedc387d9a4a" />
3D Render

5. Custom PCB Artwork
- I didn't want the PCB to just look like a normal circuit board, so I spent time adding custom artwork and branding to it. I added things like vhsHackPad, Designed by Preston Nguyen, Made For VHS Hack Club, and the board version/date.
I also experimented with using exposed copper and ENIG to make parts of the artwork appear gold on the finished PCB. I had to figure out how the copper, solder mask openings, and silkscreen layers worked together. Some artwork also had to be simplified because really tiny details wouldn't manufacture very well.
<img width="960" height="717" alt="vhsHackPadCOPPERFLAG" src="https://github.com/user-attachments/assets/5d66b3b2-3fe2-4a5c-a251-688c8727aaa3" />
Copper flag art
<img width="798" height="622" alt="vhsHackPad PCB" src="https://github.com/user-attachments/assets/2688a59a-1454-4fca-b337-0e3ecc8530d3" />
Orpheus (Hack Club Mascot) silk art!
<img width="685" height="526" alt="vhsHackPad M B" src="https://github.com/user-attachments/assets/27c07095-98cb-45b8-9630-62af9318d20d" />
3D Render w/ Silk

6. Preparing the PCB for Manufacturing
- While designing the board, I also kept PCB manufacturing and assembly in mind. I checked components and tried to make choices that would keep the board reasonably inexpensive and compatible with economical PCB assembly instead of making it unnecessarily expensive.
I also checked the final PCB for errors and made sure the important electrical issues were fixed before considering it ready to manufacture.
<img width="1101" height="593" alt="Screenshot 2026-08-14 at 11 58 27 PM" src="https://github.com/user-attachments/assets/f9bbbb9c-8921-4665-ba7a-9078649225a0" />
Matching Parts 
<img width="1153" height="897" alt="vhsHackPadJLCBack" src="https://github.com/user-attachments/assets/028b6453-7aa3-4262-97b4-3d3b7f16dc11" />
<img width="1153" height="897" alt="vhsHackPadJLCFront" src="https://github.com/user-attachments/assets/6bd2a338-6dc5-4156-88f5-b77d4188fd09" />
Render of the pcb (obviously in black)

7. Designing the Enclosure
- Once the PCB was mostly finished, I started designing the enclosure. I used measurements from my previous macropad as a starting point since I already knew roughly what worked and what didn't.
For the new design, I made the switch openings about 15.75 mm × 15.75 mm because I didn't want the switches to tightly clip into the printed enclosure. I also worked on the spacing between the switches and the edges so everything would fit without making the case unnecessarily large.

8. Fixing Switch & Case Clearances
- Some of my original dimensions ended up being a little too tight, so I had to go back and change the clearances. Since the enclosure will be 3D printed, I couldn't design everything with basically zero tolerance and expect it to fit perfectly.
I adjusted the switch openings, spacing, and surrounding walls until there was enough room for everything while still keeping the HackPad compact.

9. Designing the Slide-In Case
- I wanted the enclosure pieces to slide together instead of relying on a bunch of screws, so I designed small slide-in tabs and matching openings.
Originally, some of the tabs and openings were around 0.60 mm and 0.75 mm, but I realized that making a tab exactly the same size as its opening would probably make it way too tight after 3D printing. I started experimenting with smaller tab dimensions, including around 0.45 mm for a 0.60 mm opening, to add enough tolerance.
The goal was to make the fit tight enough that the case wouldn't randomly come apart, but not so tight that it would be insanely difficult to separate.

10. Iterating the CAD
- Changing the tabs also affected the rest of the case, so I had to keep adjusting nearby dimensions and wall thicknesses. For example, when I changed dimensions from around 0.75 mm to 0.60 mm, I also had to change some of the distances between those features and the walls.
A lot of the enclosure design ended up being small iterations like this—changing one measurement, checking what it affected, and then adjusting the surrounding geometry until everything worked together.

11. Final Design
- After working through the electronics, PCB layout, artwork, enclosure, and tolerances, I ended up with a complete vhsHackPad design that combines my custom PCB with a custom enclosure. The project was also a step up from my previous macropad because instead of building around a premade RP2040 
development board, I designed the RP2040 electronics directly into the PCB myself.
<img width="1536" height="2048" alt="528901A4-0872-4D8E-BF5D-6395DE8F3A71_1_102_o" src="https://github.com/user-attachments/assets/acca4576-e64d-4492-90f4-3e4a35212d4f" />
<img width="768" height="1024" alt="A22F3DD4-4E69-48C5-B66F-BC39F1697796_1_105_c" src="https://github.com/user-attachments/assets/95757621-b769-4be9-a09c-224483ad3d23" />
<img width="768" height="1024" alt="52E2D442-2B58-433F-9D02-B933B688B8AD_1_105_c" src="https://github.com/user-attachments/assets/370025d0-f761-4410-a616-e0fa677e3d97" />
Final Assembled Build

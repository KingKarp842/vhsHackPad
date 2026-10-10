# vhsHackPad

This project took me around 30 hours total. It was definitely not a straight line from idea to finished macropad, but that was kind of the point. I wanted to make something more advanced than my previous macropad, and vhsHackPad ended up being a mix of PCB design, CAD, firmware, artwork, and a lot of fixing small problems that turned into bigger problems.

## Project Desc.
vhsHackPad is a custom macropad I made for VHS Hack Club. It uses a custom RP2040-based PCB, mechanical keyboard switches, USB-C, and a custom 3D printed enclosure. Instead of using a separate development board, I put the RP2040 and all the supporting parts directly onto the PCB, which made the board thinner and feel more like a real finished device.

I also wanted the PCB to be part of the design instead of something hidden inside the case. The board has custom silkscreen artwork and branding like "vhsHackPad," "Designed by Preston Nguyen," and "Made For VHS Hack Club." I also experimented with exposed ENIG/gold artwork so some of the art would show up as shiny gold on the finished PCB.

The enclosure was designed around the PCB and switches, with a slide-in style case instead of a bunch of screws. That part sounded simple at first, but the tolerances and tabs ended up taking multiple versions before they felt reasonable.

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
- I started vhsHackPad because I wanted to make a custom macropad specifically for VHS Hack Club. I had already made a macropad before using a XIAO RP2040, so this time I wanted to level it up by putting the RP2040 directly onto my own PCB. I also wanted the board to actually look cool and show the Hack Club/maker side of the project, not just be a plain circuit board hidden under keycaps.

2. Designing the Schematic
- I started the electronics in KiCad. I added the RP2040, USB-C, power circuitry, crystal, switches, and all the smaller supporting components that the RP2040 needs. Since I was not using a dev board this time, I had to actually understand how the chip was wired instead of just plugging into pins on a premade board.

I also added a GPIO pinout for fun because I had enough room and thought it would be cool if the macropad could technically act kind of like a dev board too, even though I would not really recommend using it that way. One of the harder parts here was figuring out the crystal and some of the RP2040 support circuitry. I had to check which crystal pins were the actual signal pins and which ones needed to be grounded. After fixing that and cleaning up a few other schematic issues, I could finally move on to the PCB layout.

<img width="1038" height="713" alt="vhsHackPad SCHEMATIC" src="https://github.com/user-attachments/assets/7909ef98-4950-440e-b947-1d233d48576f" />

3. PCB Layout & Routing
- The PCB layout was probably one of the biggest parts of the whole project. I had to place the switches, USB-C port, RP2040, flash, crystal, power parts, and a bunch of tiny components on a board that I still wanted to keep compact.

At first I kept moving the MCU around because every placement seemed to fix one problem and create another one. If the RP2040 was in one spot, the USB routing was easier but the switch traces were worse. If I moved it somewhere else, the support components fit better but routing got messy again. I probably moved the MCU back and forth way more times than I expected.

This was also my first time working with an embedded MCU directly on a board, so I had to research where the supporting components should go relative to the chip. The crystal and decoupling capacitors could not just be thrown anywhere. I had to think about keeping important parts close while still making room for the switches and artwork.

Routing was dense because there were a lot of parts fighting for space on a small board. I went through DRC multiple times while fixing clearance problems, routing issues, and unconnected pads. Eventually, I got the actual electrical design down to 0 unconnected pads, 0 footprint errors, and 0 electrical clearance violations. The remaining warnings were mostly silkscreen-related instead of real electrical problems.

<img width="611" height="578" alt="vhshackpadMCU" src="https://github.com/user-attachments/assets/ed777dcb-c00a-4cb0-a0f7-cb3ed291f26a" />

Figuring out how to route all the parts to the MCU properly

<img width="958" height="779" alt="vhsHackPadRouting" src="https://github.com/user-attachments/assets/ba831b61-ca22-4fd3-ac9a-70ec28a2eaa7" />

Finished Routing

<img width="1002" height="807" alt="vhsHackPad-nosilk" src="https://github.com/user-attachments/assets/093a5f71-54ad-454d-846f-aedc387d9a4a" />

3D Render

4. Custom PCB Artwork
- I did not want the PCB to just look like a normal circuit board, so I spent a good amount of time adding custom artwork and branding. I added vhsHackPad, Designed by Preston Nguyen, Made For VHS Hack Club, the board version/date, and a bunch of Orpheus art that looked really good on the render.

The exposed copper/ENIG art was also a learning thing. I had to figure out how copper, solder mask openings, and silkscreen all interacted. Some details that looked fine on screen were too tiny to manufacture cleanly, so I had to simplify parts of the artwork and make sure it would still look decent on the real PCB.
<img width="960" height="717" alt="vhsHackPadCOPPERFLAG" src="https://github.com/user-attachments/assets/5d66b3b2-3fe2-4a5c-a251-688c8727aaa3" />

Copper flag art

<img width="798" height="622" alt="vhsHackPad PCB" src="https://github.com/user-attachments/assets/2688a59a-1454-4fca-b337-0e3ecc8530d3" />

Orpheus (Hack Club Mascot) silk art!

<img width="685" height="526" alt="vhsHackPad M B" src="https://github.com/user-attachments/assets/27c07095-98cb-45b8-9630-62af9318d20d" />

3D Render w/ Silk

5. Preparing the PCB for Manufacturing
- While designing the board, I kept manufacturing and assembly in mind. I checked components and tried to pick parts that would keep the PCB reasonably inexpensive and compatible with economical PCB assembly instead of making the board way more expensive than it needed to be.

I also checked the final PCB for errors before calling it ready. This was important because once the board is manufactured, a small mistake can turn into a much more annoying problem. I made sure the important electrical issues were fixed before moving forward.
<img width="1101" height="593" alt="Screenshot 2026-08-14 at 11 58 27 PM" src="https://github.com/user-attachments/assets/f9bbbb9c-8921-4665-ba7a-9078649225a0" />

Matching Parts

<img width="1153" height="897" alt="vhsHackPadJLCBack" src="https://github.com/user-attachments/assets/028b6453-7aa3-4262-97b4-3d3b7f16dc11" />

<img width="1153" height="897" alt="vhsHackPadJLCFront" src="https://github.com/user-attachments/assets/6bd2a338-6dc5-4156-88f5-b77d4188fd09" />

Render of the pcb (obviously in black)

6. Designing the Enclosure
- Once the PCB was mostly finished, I started designing the enclosure. I used measurements from my previous macropad as a starting point because I already had a rough idea of what worked and what did not.

For this version, I made the switch openings around 15.75 mm x 15.75 mm because I did not want the switches to clip in too tightly. I wanted the build to be removable enough that the board could still be accessed. I also had to balance the spacing between the switches and the case edges so it stayed compact without making everything cramped.

7. Fixing Switch & Case Clearances
- Some of the original CAD dimensions looked fine in SolidWorks but were too tight for real 3D printing. That was one of the bigger lessons from the enclosure: if two parts are modeled with basically no tolerance, they are probably not going to slide together nicely after printing.

I had to go back and resize the switch openings, spacing, and walls. The slide-in tabs especially needed adjustments because the first versions were either too tight or just not practical. I went through about 4 versions of the enclosure, changing a measurement, checking what it affected, and then changing nearby features too.

8. Designing the Slide-In Case
- I wanted the enclosure pieces to slide together instead of using a bunch of screws, so I designed small slide-in tabs with matching openings. This ended up being way more annoying than I expected.

Originally, some of the tabs and openings were around 0.60 mm and 0.75 mm, but that was too close for 3D printing. A tab that is the same size as the slot in CAD does not magically fit perfectly in real life. I experimented with smaller tab dimensions, including around 0.45 mm for a 0.60 mm opening, so there would actually be some clearance.

The goal was to make the case tight enough that it would not randomly fall apart, but loose enough that it could still slide together without feeling like I was about to break it. This part took a lot of tiny edits.

<img width="768" height="1024" alt="A388B26B-A696-4B3C-B306-50D3C65838B8_1_105_c" src="https://github.com/user-attachments/assets/e931b18b-b2d4-410b-84e1-1eddc6c1d85c" />

<img width="768" height="1024" alt="71BBC9EB-22AC-4D64-BC14-521CB4A789E4_1_105_c" src="https://github.com/user-attachments/assets/6bdb2d86-b64d-478d-af46-90998e82a7f9" />

<img width="768" height="1024" alt="B477437C-3D49-40A2-884D-C89541A27FF9_1_105_c" src="https://github.com/user-attachments/assets/93b5db9f-a7e9-4bc0-9e27-02151a498c83" />

Solidworks Crashed alot... also lapse didn't work on all of CAD...

9. Iterating the CAD
- A lot of the CAD process was basically fixing one thing and then realizing that the fix affected something else. Changing the tabs affected the nearby walls. Changing wall thickness affected how much space the PCB had. Changing clearances affected whether the slide-in case felt usable.

For example, when I changed dimensions from around 0.75 mm to 0.60 mm, I also had to adjust distances between those features and the walls. It was not just one magic number that fixed everything. I had to keep checking the whole case as one system.

SolidWorks also crashed a lot, which made the process more frustrating because I could not always just smoothly iterate. Still, after enough versions, the enclosure ended up in a much better place than the first model.

<img width="768" height="1024" alt="A8300315-275C-4646-8056-96588B22744A_1_105_c" src="https://github.com/user-attachments/assets/399c8f66-313a-4e18-bc09-9d0e5f41fb52" />

Top View of Finished CAD

<img width="768" height="1024" alt="2E81ADBB-D204-44F5-8050-76056BB91F5F_1_105_c" src="https://github.com/user-attachments/assets/b48bae63-4c14-4478-bea1-a3022c32b2bd" />

FINISHED CAD

10. Final Hardware Design
- After the electronics, PCB layout, artwork, enclosure, and tolerance work, I ended up with a complete vhsHackPad design. This was a big step up from my previous macropad because I was no longer building around a premade RP2040 board. I designed the RP2040 electronics into the PCB myself, which made the final build cleaner and more complete.

The manufactured PCB honestly came out really nice, especially the artwork. The enclosure and acrylic were less perfect. I used score-and-snap for the acrylic, and one of the corners did not snap cleanly along the line. The top-left corner ended up looking kind of ugly because I rushed it and did not support/snap it as carefully as I should have. It still works, but it is definitely a visible reminder that the physical build matters just as much as the CAD.

<img width="768" height="1024" alt="B6525CCC-FC3B-416D-AB25-DD14E9A96C1E_1_105_c" src="https://github.com/user-attachments/assets/960c6158-ac60-4d56-b8cc-5d29d792fadf" />

Manufactured PCB! (IT LOOKS SO GOOD YAYY)

<img width="1536" height="2048" alt="528901A4-0872-4D8E-BF5D-6395DE8F3A71_1_102_o" src="https://github.com/user-attachments/assets/acca4576-e64d-4492-90f4-3e4a35212d4f" />

<img width="768" height="1024" alt="A22F3DD4-4E69-48C5-B66F-BC39F1697796_1_105_c" src="https://github.com/user-attachments/assets/95757621-b769-4be9-a09c-224483ad3d23" />

I was scoring and snapping the acrylic and got lazy so the top left is snapped weird

<img width="768" height="1024" alt="52E2D442-2B58-433F-9D02-B933B688B8AD_1_105_c" src="https://github.com/user-attachments/assets/370025d0-f761-4410-a616-e0fa677e3d97" />

Final Assembled Build

11. Programming the HackPad
- After the hardware was designed, I worked on the firmware that makes the HackPad act like a keyboard. I used CircuitPython with KMK to program the RP2040 and assign actions to the mechanical switches.

This also needed multiple updates instead of working perfectly the first time. I had to make sure the switch pins in the firmware matched the GPIO pins I chose in the PCB design. Since the PCB was custom, the code had to match my actual hardware layout, not some default macropad layout from online.

The firmware is easy to change later, so the keys can be remapped to different shortcuts or functions without changing the hardware. That was one of the reasons I wanted to use KMK/CircuitPython in the first place.

12. Testing & Iterating the Firmware
- Once the firmware was on the board, I tested the switches to make sure each key press was detected and sent the expected keyboard input over USB. Some things needed fixing. One of the main bugs was that the left and right arrow keys were backwards, so pressing the physical left key would act like right, and pressing the right key would act like left.

To fix it, I had to compare the code against the actual PCB pin assignments and key layout, then update the keymap so the physical keys matched what they were supposed to do. I also updated the firmware multiple times while testing different key assignments and making sure the macropad behaved like a normal USB keyboard.

This part reminded me that a PCB can be electrically fine and still need software debugging. The code running is not the same thing as every key doing the correct thing.

Check out the CODE README under the Firmware section!

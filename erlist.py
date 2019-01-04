def text_import():
	text = """*********************
*********************
C0 error codes
*********************	
*********************	
00;-----;No Error;
01;-----;Syntax Error;There is a wrong set of parameters or parameter ranges.
02;-----;Hardware Error;Steps lost on one or more hardware components, or component not initialized or not functioning.  Drive Blocked.  Low Power, etc.
03;-----;Command not completed;Not Executed Error .  There was an error in previous part command.
04;-----;Clot detected;Clot Error.  Blood Clot detected.  LLD not interrupted.
05;-----;Barcode Unreadable;Barcode Error.  Barcode could not be read or is missing.
06;-----;Too Little Liquid;"Insufficient Liquid Error.  Not enough liquid available. 1.    Liquid Surface is not detected. 2.    Aspirate/Dispense conditions could not be fulfilled. 
07;-----;Tip Already Fitted;Tip Present Error.  A Tip has already been picked up.  Repeated attempts to fit a tip or iSWAP Movement with Tips.
08;-----;No Tip;No Tip Error.  Tip is missing or not picked up.  Command was started without fitting tip (Tip was not fitted or fell off again).
09;-----;No Carrier;No Carrier Error.  No Carrier present for loading.  Load command without Carrier present.
10;-----;Not Completed;Execution Error.  A step or a part of a step could not be processed.  Command in the command buffer was aborted dur to an error in a previous command, or command stack was deleted.
11;-----;Dispense with pressure LLD;Pressure LLD Error.  A Dispense with Pressure Liquid Level Detection is not allowed.
12;-----;No Teach in Signal;Calibrate Error.  No Capacitive Signal detected during carrier calibration procedure.  X-Movement to LLD reached maximum allowable position without detecting Teach in Signal.
13;-----;Loading Tray Error;Unload Error.  Not possible to unload the Carrier due to occupied loading tray position.  Position already occupied.
14;-----;Sequenced Aspiration with pressure LLD;Pressure LLD Error.  Pressure Liquid Level Detection in a consecutive aspiration is not allowed.
15;-----;Not allowed Parameter Combination;Parameter Error.  Dispense in jet mode with Pressure Liquid Level Detection is not allowed.  pLLD and Dispnese or wrong X-Drive assignment.
16;-----;Cover Close Error;Cover is not closed and cannot be locked.
17;-----;Improper Aspiration Error Improper Dispense Error;The pressure-based Aspirate / Dispense control reported an error (not enough liquid).  Aspiration liquid stream error detected.
18;-----;Wash Fluid or Waste Error;"Wash Liquid Error.  Waste full or no more Wash Liquid available. 1.   Missing Wash Fluid 2.   Waste of particular Washer is full"
19;-----;Incubation Error;Temperature Error.  Incubator Temperature out of limit or range.
20;-----;TADM Measurement Error;"TADM overshoot.  Overshot of limits during Aspirate or Dispense. Note:  On Aspirate, this error is returned as Main Error 17. On Dispense, this error is returned as Main Error 4"
21;-----;No Element;Expected element not detected.
22;-----;Element Still Holding;Get Command is sent twice or element is not discarded.
23;-----;Element Lost;Expected element is missing (lost).
24;-----;Illegal Target Plate Position;"Cannot place plate, plate was gripped in a wrong direction.1.   Overflow or underflow of iSWAP Positions 2.   iSWAP is not in Park Position during pipetting activities"
25;-----;Illegal User Access;Illegal Intervention Error.  Cover was opened or a Carrier was removed manually.  Immediate Stop is executed.
26;-----;TADM Measurement Error;"Exceeding limits during Aspirate or Dispense.Note:  On Aspirate, this error is returned as Main Error 4. On Dispense, this error is returned as Main Error 17"
27;-----;Position Not Reachable;Position Error.  The position is out of range.  The Position is out of mechanical limits using iSWAP, CO-RE Gripper or Pipetting Channels.
28;-----;Unexpected cLLD Error;The cLLD detected a liquid level above the start height of liquid level search (Using PIP or XL Channels).
99;-----;Slave Error;This Error Code indicates an error in one of the Slave (for Error Hanlding purposes using Service Software Macro Code).
100;-----;Wrong Carrier Error;Wrong Carrier Barcode detected.
101;-----;No Carrier Barcode Error;Carrier Barcode could not be read or is missing.
102;-----;Liquid Level Error;Liquid surface not detected.
103;-----;Not Detected Error;Carrier not detected at Deck end position.
104;-----;Not Aspirated Error;Dispense Volume exceeds the Aspirated Volume.
105;-----;Improper Dispensation Error;The Dispensed Volume is out of tolerance (may only occur for Nanopipettor Dispense steps).
106;-----;No Labware Error;"The Labware to be loaded was not detected by the Autoload Module. Note:  May only occur on a Reload Carrier step if the Labware property MLStarCarPosAreRecognizable is set to 1."
107;-----;Unexpected Labware Error;The Labware contains an unexpected Barcode (may only occur on a Reload Carrier step).
108;-----;Wrong Labware Error;The Labware to be reloaded contains a wrong Barcode (may only occur on a Reload Carrier step).
109;-----;Barcode Mask Error;The Barcode read doesnt match the Barcode Mask defined.
110;-----;Barcode Not Unique Error;The Barcode read is not unique.  Previously loaded Labware with the same Barcode was loaded without a unique Barcode Check.
111;-----;Barcode Already Used Error;The Barcode read is already loaded as a unique Barcode (its not possible to load the same Barcode twice).
112;-----;Kit Lot Expired Error;Kit Lot expired.

*********************	
*********************	
C0 Master Error Information
*********************	
*********************	
10;-----;CAN Error
11;-----;Slave Command Time Out
12;-----;Supply Out of Limits
20;-----;E2PROM Error
30;-----;Unknown Command
31;-----;Unknown Parameter
32;-----;Parameter Out of Range
33;-----;Parameter does not belong to command, or not all parameters wer sent
34;-----;Node Name Unknown
35;-----;ID Parameter Error
37;-----;Node Name Defined Twice
38;-----;Faulty XL Channel Settings
39;-----;Faulty Robotic Channel Settings
40;-----;PIP Task Busy
41;-----;Autoload Task Busy
42;-----;Miscellaneous Task Busy
43;-----;Incubator Task Busy
44;-----;Washer Task Busy
45;-----;iSWAP Task Busy
46;-----;CO-RE 96 Head Task Busy
47;-----;Carrier Sensor doesnt work properly
48;-----;CO-RE 384 Head Task Busy
49;-----;Nanopipettor Task Busy
50;-----;XL Channel Task Busy
51;-----;Tube Gripper Task Busy
52;-----;Imaging Channel Task Busy
53;-----;Robotic Channel Task Busy



*********************	
*********************	
Autoload Error Codes
*********************	
*********************	

ID;;Error Message;Trigger / Description;Possible Cause
General
0;-----;No Error;;

Transfer Check
20;-----;No Communication to EEPROM;I2C Bus Driver;I2C Bus or EEPROM not working

Syntax Check
30;-----;Undefined Command;Syntax Check;Unknown Command
31;-----;Undefined Parameter;Syntax Check;Unknown Parameter
32;-----;Parameter Out of Range;Syntax Check;Parameter Outside Permitted Range


During Execution of Commands
35;-----;Voltages Out of Permitted Range;Voltage Monitoring;Power Supply hardware not working properly
36;-----;Stop during Execution of a Command;Stop Command;

Parallelity
40;-----;No Parallel Process in Control Process 0 Permitted;Status Function;Two or more commands sent to the same control process in level 0, request or special command

Scanner X-Drive
50;-----;Initialization Position not found;Supervision, Maximum movement without Sensor Edge Recognition;"Drive Blocked, Initialization Sensor Fault May arise only on Initialization Command"
51;-----;Stepper Motor not initialized;Supervision, Status Function, Position Monitoring;"Movement Command sent before Drive Initialized May arise on all Movement Commands except Initialization Command and Relative Movement without Supervision"
52;-----;Movement Error;Supervision,  Step Monitoring, Incremental Sensor;"Drive Blocked, Incremental Sensor Fault, Step Loss May arise on all Movement Commands"

Scanner Rotation Drive
55;-----;Drive Blocked;Supervision, Maximum movement without Sensor Edge Recognition;"Drive Blocked, Initialization Sensor Fault May arise only on Initialization Command"

Carrier Y-Drive
60;-----;Initialization Position Not Found;Supervision, Maximum movement without Sensor Edge Recognition;"Drive Blocked, Initialization Sensor Fault May arise only on Initialization Command"
61;-----;Stepper Motor Not Initialized;Supervision, Status Function, Position Monitoring;"Movement Command sent before Drive Initialized May arise on all Movement Commands except Initialization Command and Relative Movement without Supervision"
62;-----;Movement Error;Supervision,  Step Monitoring, Incremental Sensor;"Drive Blocked, Incremental Sensor Fault, Step Loss May arise on all Movement Commands"

Carrier Z-Drive
65;-----;Initialization Position not found;Supervision, Maximum movement without Sensor Edge Recognition;"Drive Blocked, Initialization Sensor Fault May arise only on Initialization Command"
66;-----;Stepper Motor not Initialized;Supervision, Status Function, Position Monitoring;"Movement Command sent before Drive Initialized May arise on all Movement Commands except Initialization Command and Relative Movement without Supervision"
67;-----;Movement Error;Supervision,  Step Monitoring, Incremental Sensor;"Drive Blocked, Incremental Sensor Fault, Step Loss May arise on all Movement Commands"

Barcode Scanner
70;-----;Communication Error;Protocol;Hardware not working, Scanner dysfunction

Loading Indication (LED)
75;-----;Communication Error to Loading Indicator;Protocol;Communication to LEDs not working

Carrier Handling
80;-----;Identification Barcode not readable;Scanner;Missing or unreadable iddentification Barcode or wrong Barcode type definition
81;-----;No carrier present;Identification procedure;Carrier missing or sensor not working
82;-----;No Carrier Loaded;Status Administration;Load or Unload Command without identification of carrier
83;-----;Loading Tray is occupied;Test of presence or absence;At Unloading, Carrier detected on Loading Tray
"""
	return (text)
	

# projectOpenLi-Fi

An attempt to transfer useful data by varying the intensity of visible light using a cheap microcontroller and a singlecell Solarpanel.

Clone this repository by typing

`git clone https://github.com/jithinsankar/projectLI-FI.git`

## Prerequisites
1. Two computers running python 2.7 with pyserial and numpy modules installed
2. Two arduino,Two arduino serial cable
3. One LED light ,1K ohm resistor
4. One Solar Panel / Photo resistor , 1K Ohm resistor

## STEP 1 : 
Upload the ino files inside alpharx and alphatx into corresponding receiving and transmitting arduino boards
Copy the alpharx folder to receiver computer and alphax to transmitting computer.

## STEP 2 : 
Arrange the components as shown.
![alt text](/Diagram.png)

## STEP 3:
Direct the file to be sent by editing the 9th line of alphatx/main.py

## STEP 4:
Run alphatx/main.py and alpharx/main.py in transmitting and receiving computers respectively.( SUBLIMEREPL or PYTHON IDLE recommended ).Make sure you run alpharx/main.py

Viola !! Data is transmitted to the other computer. 


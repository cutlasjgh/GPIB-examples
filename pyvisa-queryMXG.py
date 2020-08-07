#!/usr/bin/env python3

# requires pyvisa at a minimum and you will also need a resource.
# A resource can either be pyvisa-sim or Kesight IO libraries or National Instruments NI visa library.
# if you only install a visa library such as keysight or NI, they become the default and you can leave 
# the ResouceManager() call arguments empty probably.
# To see any real instruments via the ResourceManager call, you must have NI or Keysight recognize them.
# to have Keysight recognize instruments, run io-ce aka Keysight Connection Explorer.
# to have NI recognize instruments, run either MAX (windows only) or visaconf (Linux and others)
# This all works under Centos 7 in the year 2020.. 

# I found Keysight IO libraries at https://www.keysight.com/main/software.jspx?ckey=2175637&nid=-32390.536881830&cc=eng&lc=eng
# I found NI libraries at https://www.ni.com/en-us/support/downloads/drivers.html 
 
#Below works over E5810A LAN/GPIB gateway to talk to an Agilent MXG Analog Signal Generator

# note you can use visa or pyvisa as the import and python module name
# Note you may have to run as root or correct permission to see actual list, unless you add the user to the pxisa or kt-iols group
# I had both NI-VISA and Keysight Visa libraries installed, and since NI was installed first
# I believe Keysight allowed NI to be default. So to get to Keysight resource manager,
# you have to specify the full path to libktvisa
# and if you dont see any resources, run io-ce (keysight) or visaconf or MAX for NI.


import pyvisa  # or visa works here also instead of pyvisa (as long as pyvisa is installed)

# rm = pyvisa.ResourceManager() # would print about 4 instruments
#prints out such as: ('ASRL1::INSTR', 'ASRL2::INSTR', 'ASRL3::INSTR', 'ASRL4::INSTR')
#rm = pyvisa.ResourceManager('@sim')  # pyvisa-sim prints about 15 instruments see pyvisa's default.yaml
#rm = pyvisa.ResourceManager('@ivi') 
#rm = pyvisa.ResourceManager('@ni')  # would end up using ni visa resources
#rm = pyvisa.ResourceManager('/opt/keysight/iolibs/libktvisa32.so')  # will list keystone visa resources
rm = pyvisa.ResourceManager('/opt/keysight/iolibs/libktvisa32.so.0.0.0') # says32 but ldd reports as 64bit
# if using windows try something like: 
#rm = pyvisa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')
rmlist = rm.list_resources()
print(rmlist)
print(rmlist[0])

inst = rm.open_resource(rmlist[0], read_termination='\n')

# query is equiv to write/read 
# I saw example that tried "?IDN" and thats an error waiting to happen, use "*IDN?" instead of course.
# Either:
#print(inst.query("*IDN?"))  
# OR:
reply = inst.write("*IDN?")
reply = inst.read()
print(reply)

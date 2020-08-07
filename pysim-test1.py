
# this code will try to use pyvisa-sim and it's default simulated resource
# to run it you must have pyvisa-sim and pyvisa

import pyvisa as visa
rm = visa.ResourceManager('@sim')
#rm.list_resources()
print(rm.list_resources())
#prints out such as: ('ASRL1::INSTR', 'USB0::0x1111::0x2222::0x1234::0::INSTR', 'TCPIP0::localhost::inst0::INSTR', 'GPIB0::8::0::INSTR', 'ASRL2::INSTR', 'USB0::0x1111::0x2222::0x2468::0::INSTR', 'TCPIP0::localhost:2222::inst0::INSTR', 'GPIB0::9::0::INSTR', 'ASRL3::INSTR', 'USB0::0x1111::0x2222::0x3692::0::INSTR', 'TCPIP0::localhost:3333::inst0::INSTR', 'GPIB0::10::0::INSTR', 'ASRL4::INSTR', 'USB0::0x1111::0x2222::0x4444::0::INSTR', 'TCPIP0::localhost:4444::inst0::INSTR', 'GPIB0::4::0::INSTR')

inst = rm.open_resource('ASRL1::INSTR', read_termination='\n')
print(inst.query("*IDN?"))
# results in : LSG Serial #1234

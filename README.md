# GPIB-examples
GPIB aka IEEE-4888 using pyvisa via VISA libraries such as Keysight IO and National Instruments NI

this is a year 2020 example that works under Centos 7 and should work under modern UBuntu etc.

I had trouble finding how to use Keysight Visa libraries, as most people use NI National Instruments it seems.

Bottom line is minimum you probably have to do is install visa libraries that are from the SAME manufacturer as your interface card or gateway.
example, if you have a keysight E5810A or B LAN/GPIB gateway then you install Keysight IO libraries..
If you have a NI USB to GPIB conveter, then install NI libraries. 
Both libraries can be installed at same time, and they coexist. The default is usually the first installed.

you can get Keysight IO libraries from
https://www.keysight.com/main/software.jspx?ckey=2175637&nid=-32390.536881830&cc=eng&lc=eng

or if you want to use NI libraries from https://www.ni.com/en-us/support/downloads/drivers.html 

And you will need pyvisa to run the python example. You do not need pyvisa-sim unless you want to simulate resources.
try: pip install pyvisa  
or pip3 install pyvisa 
to install pyvisa (or use your package manager such as apt or yum or anaconda etc)

To see any real instruments via the ResourceManager call, you must have NI or Keysight recognize them.
to have Keysight recognize instruments, run io-ce aka Keysight Connection Explorer, and make sure your instrument shows up, it should if it's connected via a Keysight interface such as a PCI card or LAN to GPIB gateway.

to have NI recognize instruments, run either MAX (windows only) or visaconf (Linux and others)

The only other trick is that you need to have the pyvisa.ResourceManager() call use the library as it's argument:
examples lacked and I had to search for a Keysight library to use via linux commandline in my case results in:
Here are different variants of a ResourceManager call that might be useful (choose one):

rm = pyvisa.ResourceManager() # will try default visa library

rm = pyvisa.ResourceManager('@sim')  # uses pyvisa-sim if installed and prints about 15 instruments see pyvisa's default.yaml

rm = pyvisa.ResourceManager('@ivi')  # uses a built in ivi visa library 

rm = pyvisa.ResourceManager('@ni')  # would end up using ni visa resources

rm = pyvisa.ResourceManager('/opt/keysight/iolibs/libktvisa32.so')  # will list keystone visa resources

rm = pyvisa.ResourceManager('/opt/keysight/iolibs/libktvisa32.so.0.0.0') # will list keystone visa resources, file name says32 but ldd reports as 64bit

if using windows try something like: 

rm = pyvisa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')

and I read somewhere that forward slashes are ok instead of double backslashes even for windows, so try that if needed.

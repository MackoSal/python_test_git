import serial
ser = serial.Serial(
	port='COM7',
	baudrate=1200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.EIGHTBITS
    )

# ser.open()
if ser.is_open:
    print("port otwarty")
else: 
    print("port nieotwarty")

"""
komendy:
SND_NKE (\x40) - polaczenie z normalizacja


-------------------------------------
ACK (\xe5)    - potwierdzenie przyjecia informacji



"""


command = [
    b'\x10\x40\x0B\x4B\x16',      #start, SND_NKE, adres urządzenia(11), suma sprawdzajaca, stop
    b'\x10\x7B\x0B\x86\x16',      #  odczyt danych
    b'\x80\x3F\x10\x08\x00\x3C\x00\x44\x03\xEC\x00\x56\x00\x57\x00\x59\x00\x50\x00\x4A\x81\x1C\x0D'

]
ser.write(command[2])
data = ser.read(100)            # odczytuje mi czesc znakow jako z ASCII   (trzeba znac z gory ile bajtow ma odczytac)         
print(type(data))
print(data)
# ser.write(command[0])
# data = ser.read()                       
# # print(type(data))
# print(data)









ser.close()
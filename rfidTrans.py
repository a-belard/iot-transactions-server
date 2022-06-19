import requests
import csv
import serial

#
# ser = serial.Serial(
#     port='COM17',
#     baudrate=9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1
# )
# ser.flush()


def read_file(file):
    jsonArray = []
    with open(file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    return jsonArray


data = read_file("transactions.txt")
res = requests.post(
    'http://localhost:3000/transaction', json=data)

if res.ok:
    print("Data Uploaded")
else:
    print("Failed uploading!")

# if __name__ == '__main__':
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').rstrip()
#             f = open("transactions.txt", "a")
#             f.write(line)
#             f.write("\n")
#             f.close()
#             data = readFile("transactions.txt")
#             res = requests.post(
#                 'http://localhost:5050/data', json=data)
#             if res.ok:
#                 print("Data uploaded")
#                 ser.write(bytes("Data uploaded"), 'utf-8')
#                 ser.flush()

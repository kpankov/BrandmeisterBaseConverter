import argparse

parser = argparse.ArgumentParser(description='Merge D-STAR bin and md380 csv.')

parser.add_argument('BIN', type=str, help='Input *.bin file path')
parser.add_argument('CSV_IN', type=str, help='Input *.csv file path')
parser.add_argument('CSV_OUT', type=str, help='Output *.csv file path')

args = parser.parse_args()

bin_file_buffer = open(args.BIN, 'r').readlines()
csv_in_file_buffer = open(args.CSV_IN, 'r').readlines()

csv_out_file = open(args.CSV_OUT, 'w')

base = {}
bin_file_buffer.pop(0) # Remove first line

for line in bin_file_buffer:
    dmrId = line.split("\t\t")[0]
    dmrCallsign = line.split("\t\t")[1].split('\n')[0]
    #print "ID: " + dmrId + ", CallSign: " + dmrCallsign
    base.update({int(dmrId):[dmrCallsign, "Private Call", "No"]})

for line in csv_in_file_buffer:
    dmrId = line.split(",")[0].split("\"")[1]
    dmrCallsign = line.split(",")[1].split("\"")[1]
    dmrType = line.split(",")[2].split("\"")[1]
    dmrAlert = line.split(",")[3].split("\"")[1]
    #print "ID: " + dmrId + ", CallSign: " + dmrCallsign + ", Type: " + dmrType + ", Alert: " + dmrAlert
    base.update({int(dmrId):[dmrCallsign, dmrType, dmrAlert]})

for line in base:
    output_line =  "\"" + str(line) + "\",\"" + base.get(line)[0] + "\",\"" + base.get(line)[1] + "\",\"" + base.get(line)[2] + "\",\"\",\"\",\"\",\"\",\"\"\n"
    csv_out_file.write(output_line)

#print base

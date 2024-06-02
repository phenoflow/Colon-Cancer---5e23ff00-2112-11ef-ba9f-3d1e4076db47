# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"B140.00","system":"readv2"},{"code":"B134.00","system":"readv2"},{"code":"B142000","system":"readv2"},{"code":"B131.00","system":"readv2"},{"code":"B136.00","system":"readv2"},{"code":"B132.00","system":"readv2"},{"code":"B130.00","system":"readv2"},{"code":"B137.00","system":"readv2"},{"code":"B142.00","system":"readv2"},{"code":"B133.00","system":"readv2"},{"code":"B13..00","system":"readv2"},{"code":"B135.00","system":"readv2"},{"code":"B138.00","system":"readv2"},{"code":"B143.00","system":"readv2"},{"code":"B13z.00","system":"readv2"},{"code":"B13y.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('colon-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["colon-cancer-malig---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["colon-cancer-malig---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["colon-cancer-malig---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

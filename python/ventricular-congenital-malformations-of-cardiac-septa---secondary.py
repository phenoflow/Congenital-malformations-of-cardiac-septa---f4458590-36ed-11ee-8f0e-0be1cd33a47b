# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"K09","system":"opcs4"},{"code":"K09.1","system":"opcs4"},{"code":"K09.2","system":"opcs4"},{"code":"K09.3","system":"opcs4"},{"code":"K09.5","system":"opcs4"},{"code":"K09.6","system":"opcs4"},{"code":"K09.8","system":"opcs4"},{"code":"K09.9","system":"opcs4"},{"code":"K11","system":"opcs4"},{"code":"K11.1","system":"opcs4"},{"code":"K11.2","system":"opcs4"},{"code":"K11.3","system":"opcs4"},{"code":"K11.4","system":"opcs4"},{"code":"K11.5","system":"opcs4"},{"code":"K11.6","system":"opcs4"},{"code":"K11.7","system":"opcs4"},{"code":"K11.8","system":"opcs4"},{"code":"K11.9","system":"opcs4"},{"code":"K13.1","system":"opcs4"},{"code":"K13.2","system":"opcs4"},{"code":"K14.5","system":"opcs4"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('congenital-malformations-of-cardiac-septa-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ventricular-congenital-malformations-of-cardiac-septa---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ventricular-congenital-malformations-of-cardiac-septa---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ventricular-congenital-malformations-of-cardiac-septa---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"101393.0","system":"med"},{"code":"109853.0","system":"med"},{"code":"18395.0","system":"med"},{"code":"19969.0","system":"med"},{"code":"20153.0","system":"med"},{"code":"23692.0","system":"med"},{"code":"246.0","system":"med"},{"code":"28174.0","system":"med"},{"code":"3255.0","system":"med"},{"code":"34067.0","system":"med"},{"code":"3625.0","system":"med"},{"code":"37816.0","system":"med"},{"code":"38967.0","system":"med"},{"code":"40025.0","system":"med"},{"code":"40673.0","system":"med"},{"code":"42132.0","system":"med"},{"code":"43049.0","system":"med"},{"code":"44896.0","system":"med"},{"code":"4864.0","system":"med"},{"code":"49702.0","system":"med"},{"code":"51053.0","system":"med"},{"code":"51649.0","system":"med"},{"code":"51897.0","system":"med"},{"code":"52607.0","system":"med"},{"code":"53088.0","system":"med"},{"code":"54196.0","system":"med"},{"code":"54243.0","system":"med"},{"code":"54772.0","system":"med"},{"code":"55535.0","system":"med"},{"code":"56575.0","system":"med"},{"code":"59144.0","system":"med"},{"code":"61715.0","system":"med"},{"code":"63046.0","system":"med"},{"code":"63340.0","system":"med"},{"code":"66401.0","system":"med"},{"code":"67657.0","system":"med"},{"code":"71252.0","system":"med"},{"code":"72577.0","system":"med"},{"code":"72604.0","system":"med"},{"code":"73816.0","system":"med"},{"code":"7474.0","system":"med"},{"code":"9011.0","system":"med"},{"code":"93161.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('congenital-malformations-of-cardiac-septa-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["malformations---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["malformations---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["malformations---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

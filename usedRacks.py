import csv
import re

def mfindRacks(facility_id):
    with open(r"C:\Users\A0715246\Music\Data_Netbox\netbox_racks.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if re.match(facility_id, str(row['facility_id'])):
                print(row['name'])
            else:pass

import csv
import re

def mfindRacks(facility_id):
    with open("netbox_racks.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if re.match(facility_id, row['facility_id']):
                print(row['name'])
            else:pass

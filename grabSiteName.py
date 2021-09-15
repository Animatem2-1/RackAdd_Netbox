import csv

def mSiteName(facility_id):
    with open(r"C:\Users\A0715246\Music\Data_Netbox\netbox_sites.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            facility_id_origin = row['facility'] + '.' + row['asn']
            if facility_id_origin == facility_id:
                return row['name']
                break

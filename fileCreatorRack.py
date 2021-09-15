import csv

def mcreate(facility_id, siteName, rackName, u_height, tack):
    status = "active"
    tenant = "ZHS"
    width = "19"
    comments = "Wspolrzedne geograficzne " + tack


    with open(r'C:\Users\A0715246\Music\Data_Netbox\netbox_racks.csv', 'a', newline='') as csvfile:
        fieldnames = ['site','group','name','facility_id','tenant','status','role','type','serial','asset_tag','width','u_height','desc_units','outer_width','outer_depth','outer_unit','comments']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


        writer.writerow({'site': siteName,'group': '','name': rackName,'facility_id': facility_id,'tenant': tenant,'status': status,'role': '','type': '','serial': '','asset_tag': '','width': width,'u_height': u_height,'desc_units': '','outer_width': '','outer_depth': '','outer_unit': '','comments': comments})

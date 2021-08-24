def mcreate(facility_id, siteName, rackName, u_height, tack):
    status = "active"
    tenant = "ZHS"
    width = "19"
    comments = "Wspolrzedne geograficzne " + tack
    fileAppend = open("netbox_racks.txt", "a")
    fileAppend.write("\r" + siteName +","+ rackName +","+ facility_id +","+ tenant + "," + status + "," + width + "," + u_height + "," + comments)
    fileAppend.close()
    #"site,name,facility_id,tenant,status,width,u_height,comments"

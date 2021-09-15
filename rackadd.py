import sys
import json
import grabSiteName
import usedRacks
import time
import fileCreatorRack
import re

print("Wprowadz FACILITY_ID (numer obiektu plus numer ASN):")
facility_id = input()
siteName = grabSiteName.mSiteName(facility_id)
print("Nazwa site'u: " + siteName)
print("Szafy w danym wezle: ")
usedRacks = usedRacks.mfindRacks(facility_id)
time.sleep(1)
print("Wprowadz kolejny numer szafy w danym wezle:")
rackNumber = input()
rackName = facility_id + "." + rackNumber
print("Wprowadz ilosc U w szafie lub nacisnij enter (wprowadzi domyslnie 42):")
u_height = input()
if u_height == "": u_height = "42"
print("Wprowadz wspolrzedne geograficzna lub nacisnij enter aby zostawic puste:")
old_tack = input()
tack = old_tack.replace(",", "")
fileCreatorRack.mcreate(facility_id, siteName, rackName, u_height, tack)

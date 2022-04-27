import boto3
import csv

session = boto3.Session()

all_services = session.get_available_services()
file = open("C:\\Users\\satishkr\\Downloads\\Satish\\Services_Regions.csv", 'w')
writer = csv.DictWriter(
        file, fieldnames=["Services", "Regions"])
writer.writeheader()
file.close()
for service in all_services:
    all_regions = session.get_available_regions(service)

    for region in all_regions:
        file = open("C:\\Users\\satishkr\\Downloads\\Satish\\Services_Regions.csv", 'a')
        file.write("%s %s \n" % (service, "," + region))
        file.close()

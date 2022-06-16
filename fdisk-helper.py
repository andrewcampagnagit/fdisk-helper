import os
import json

EXTENDED_PART = lambda size : "n\ne\n\n"+ size +"\n"
PRIMARY_PART= lambda size : "n\np\n\n"+ size +"\n\n"
WRITE_DISK_STRING = lambda size : "n\n\n"+ size +"\n"
FDISK_FULL_PARTITION_STRING_TABLE = {}

disk_manifest = json.load(open("disk-manifest.json"))
for device in disk_manifest["table"].keys():
	FDISK_FULL_PARTITION_STRING_TABLE[device] = ""

	if "extended" in disk_manifest["table"][device].keys():
		if disk_manifest["table"][device]["extended"]["e"] == ["ALL"]:
			FDISK_FULL_PARTITION_STRING_TABLE[device] += EXTENDED_PART("")
		else:
			for extended_part_size in disk_manifest["table"][device]["extended"]["e"]:
				FDISK_FULL_PARTITION_STRING_TABLE[device] += EXTENDED_PART(extended_part_size)

		if "parts" in disk_manifest["table"][device]["extended"].keys():
			for part in disk_manifest["table"][device]["extended"]["parts"]:
				size = list(part.keys())[0]
				multi = part[size]
				for n in range(0,multi):
					FDISK_FULL_PARTITION_STRING_TABLE[device] += WRITE_DISK_STRING(size)

for device in FDISK_FULL_PARTITION_STRING_TABLE.keys():
	FDISK_FULL_PARTITION_STRING_TABLE[device] += "w\n"

print(FDISK_FULL_PARTITION_STRING_TABLE)

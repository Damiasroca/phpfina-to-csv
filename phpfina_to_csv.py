import struct
import os
import csv

def read_phpfina_to_csv(feedid, dir_path, output_file):
    # Read meta
    with open(os.path.join(dir_path, f"{feedid}.meta"), 'rb') as metafile:
        metafile.seek(8)
        interval = struct.unpack("I", metafile.read(4))[0]
        start_time = struct.unpack("I", metafile.read(4))[0]

    # Open data
    data_file_path = os.path.join(dir_path, f"{feedid}.dat")
    with open(data_file_path, 'rb') as fh, open(output_file, 'w', newline='') as csvfile:
        filesize = os.path.getsize(data_file_path)
        npoints = filesize // 4

        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Time", "Value"])

        for i in range(npoints):
            val = struct.unpack("f", fh.read(4))[0]
            time = start_time + i * interval
            csv_writer.writerow([time, val])


dir_path = r'C:\PATH\OF\THE\EXTRACTED\BACKUP\emoncms-backup-emonpi-YYYY-MM-DD\phpfina' # Change this to the correct path
feedid = 1  # Change this to the correct feed ID
output_file = "output.csv"  # Name of the CSV file where data will be saved
read_phpfina_to_csv(feedid, dir_path, output_file)

#/bin/python3

#sudo tshark -l -i enp0s3 -T fields -E separator=" " -e ip.src -e frame.time_epoch -c 15 dst host 10.0.2.15 | python3 sql_common.py

import pymysql.cursors
import sys

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='puzzle',
                             db='ip_database',
                             #charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

for line in sys.stdin:
    lines= line.split()

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO ip_storage (ip_addr, first_visit, last_visit) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE last_visit=%s"

            for line in sys.stdin:

                n=line.split()
                cursor.execute(sql, (n[0], n[1], n[1], n[1]))

        connection.commit()
    finally:
        connection.close()

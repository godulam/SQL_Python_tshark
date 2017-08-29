#!/usr/bin/python3

import MySQLdb
import MySQLdb.cursors as cursors
import sys

# Connect to the database
connection = MySQLdb.connect(host='localhost',
                             user='root',
                             password='puzzle',
                             db='ip_database',
                             #charset='utf8mb4',
                             cursorclass=cursors.SSCursor)


cursor = connection.cursor()

f=open('/var/www/html/report.html', 'w')
f.write("<html><head><title>Report</title></head><body><table border=\'2\' width=\"500\"><tr><td colspan=\'2\'><center>IP addresses with shortest response times:</center></td></tr>")

def ip_shortest():
    cursor.execute('SELECT ip_addr, avg_rt FROM ip_storage ORDER BY avg_rt ASC LIMIT 3;')
    result = cursor.fetchall()

    print ("IP addresses with shortest response times:\n")
    for row in result:
        print("IP: ", row[0], " response time: ", row[1])
        f.write("<tr><td>IP: ")
        f.write(str(row[0]))
        f.write("</td><td>response time: ")
        f.write(str(row[1]))
        f.write("</td></tr>")
    print ('')


def ip_longest():
    cursor.execute('SELECT ip_addr, avg_rt FROM ip_storage ORDER BY avg_rt DESC LIMIT 3;')
    result = cursor.fetchall()

    print ("IP addresses with longest response times:\n")
    for row in result:
        print("IP: ", row[0], " response time: ", row[1])
        f.write("<tr><td>IP: ")
        f.write(str(row[0]))
        f.write("</td><td>response time: ")
        f.write(str(row[1]))
        f.write("</td></tr>")

ip_shortest()

f.write('</table></br><table border=\'2\' width=\"500\"><tr><td colspan=\'2\'><center>IP addresses with longest response times:</center></td></tr>')

ip_longest()

f.write("</table></body></html>")
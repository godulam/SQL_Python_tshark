import MySQLdb
import MySQLdb.cursors as cursors

# Connect to the database
connection = MySQLdb.connect(host='localhost',
                             user='root',
                             password='puzzle',
                             db='ip_database',
                             #charset='utf8mb4',
                             cursorclass=cursors.SSCursor)


cursor = connection.cursor()

def ip_shortests():
    cursor.execute('SELECT ip_addr, avg_rt FROM ip_storage ORDER BY avg_rt ASC LIMIT 3;')
    result = cursor.fetchall()

    print ("IP addresses with shortest response times:\n")
    for row in result:
        print("IP: ", row[0], " response time: ", row[1])
    print ('')

def ip_longest():
    cursor.execute('SELECT ip_addr, avg_rt FROM ip_storage ORDER BY avg_rt DESC LIMIT 3;')
    result = cursor.fetchall()

    print ("IP addresses with longest response times:\n")
    for row in result:
        print("IP: ", row[0], " response time: ", row[1])

ip_shortests()
ip_longest()

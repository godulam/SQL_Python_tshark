import MySQLdb
import MySQLdb.cursors as cursors
import subprocess
import time

# Connect to the database
connection = MySQLdb.connect(host='localhost',
                             user='root',
                             password='puzzle',
                             db='ip_database',
                             #charset='utf8mb4',
                             cursorclass=cursors.SSCursor)


cursor = connection.cursor()
cursor.execute('SELECT * FROM ip_storage ORDER BY test_time ASC LIMIT 10')
result = cursor.fetchall()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for row in result:
    output = subprocess.check_output("ping -c 4 %s | tail -1| awk \'{print $4}\' | cut -d \'/\' -f 2" % row[0], shell=True)
    epoch_time = int(time.time())
    if is_number(output):
        output = float(output.decode("UTF-8"))
        print(row[0])
        print (epoch_time)
        print(output)
        sql = "UPDATE ip_storage SET avg_rt=%s, test_time=%s WHERE ip_addr=%s"
        cursor.execute(sql, (output, epoch_time, row[0]))
    else:
        print ('trololo')

connection.commit()

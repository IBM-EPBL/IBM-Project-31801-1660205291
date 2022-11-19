import ibm_db

hostname="54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid="rwx41024"
pwd="Rbs1PB1BRYh6gK4Q"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="32733"
protocol="TCPIP"
cert="Certificate.crt"

dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
).format(db,hostname,port,uid,cert,pwd)
print(dsn)

try:
    db2=ibm_db.connect(dsn,"","")
    print("connectd to database")
except:
    print("unable to connect",ibm_db.conn_errormsg())
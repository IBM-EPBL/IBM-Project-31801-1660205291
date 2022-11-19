import ibm_db

hostname="9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid="ggf89034"
pwd="U56rYxppzwHIwcst"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="32459"
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
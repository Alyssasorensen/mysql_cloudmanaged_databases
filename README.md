# mysql_cloudmanaged_databases
## **HHA 504 HW Assignment 4**
This task centers around MySQL, delving into its deployment across prominent cloud platforms such as Azure and GCP. Upon completion, I will have acquired practical proficiency in configuring MySQL on these platforms. Additionally, I will become adept at employing MySQL Workbench for database design and management, and if desired, I can also learn to establish connections to my database using Python to retrieve data.
**Make sure that the instance is properly configued to allow inbound traffic from the world wide web. In GCP, we needed to configure a network that allowed any ip (0.0.0.0/0) - there is a similar configuration option that you need to find in Azure.**
## Setup process for Azure:
**Azure:**
**Azure Database for MySQL**
**Deployment option: Flexible,**
**Tier: Burstable**
**Compute: B1S [$6.21 p/month] or B1MS [$12.41 p/month]**
1. Sign in to Azure: Logged in to my Microsoft Azure account using my credentials.

2. In the Azure portal, click on the "+ Create a resource" button on the left-hand menu.

3. Search for MySQL Service:
In the "New" panel, type "Azure Database for MySQL" into the search box and click on it. 

4. Configure MySQL Settings:
-Clicked the "Create" or "Add" button and began setting up my MySQL instance. Subscription: Chose my Azure subscription. Resource Group: Created a new resource group. Instance Details: Set a unique name for MySQL instance, chose the region, and selected the MySQL version. Compute + Storage: Configured the compute and storage options according to my needs. I chose the tier that stated, "Burstable." Administrator Account: I set a username and password for MySQL server. Networking: Configure network settings, firewall rules, and public accessibility settings. I put a public IP address, but added the network, 0.0.0.0, which allows any IP. Additional Settings: Depending on your requirements, you may have other options to configure, such as backups, security, and tags.

5. Review and Create: After configuring all of my settings, I reviwed my choices to ensure they are correct. Then, I clicked the "Review + create" button.

6. Validation: Azure will validate your configuration to check for any errors or conflicts. If there are no issues, you can proceed to create the MySQL instance.

7. Create: Clicked the "Create" button to deploy MySQL instance.

8. Deployment: Azure will start deploying your MySQL instance based on the provided configuration. This process may take a few minutes.

9. Access and Management: Once the deployment is complete, I can access and manage my MySQL instance through the Azure portal. 

10. Connect to MySQL: I used MySQL Workbench to connect to my Azure MySQL instance. 

## Setup process for GCP:
**DB-standard-1 (vCPU 1, RAM 3.75gb)
10gb storage
No backups [$9.37 month]DB-standard-1 (vCPU 1, RAM 3.75gb)**
1. I logged into Google Cloud console.

2. I created a new project by clicking on the project name in the upper left corner of the console and selecting "New Project."

3. I clicked the navigation menu in the upper left corner and then went to "SQL" under "Databases."

4. I clicked the "Create Instance" button.

5. I created an instance ID which is a unique identifier for the instance.

6. I then set a password for MySQL.

7. I put the region where my instance will be hosted.

8. I selected MySQL version.

9. I chose the machine type. 

10. I also chose my storage type.

11. Under "Connectivity," I configured network options, including IP addresses, authorized networks, and SSL/TLS settings.

12. I reviewed my configuration settings to ensure they were correct and clicked the "Create" button to create my MySQL instance.

13. Google Cloud then started provisioning MySQL instance. This took a few minutes.

14. Once my deployment was complete, I managed MySQL instance from the Google Cloud Console.

15. I connected MySQL instance to MySQL Workbench.

## My experience with MySQL Workbench, including the ERD creation and database interactions: 
Overall my experience with GCP, Azure, and MySQL Workbench was successful. I was able to create a database and display the database. I was able to create tables that were placed into the database. I was then able to create two entity-relationship diagrams (ERD) using both GCP and Azure. From the screenshots, you can see that one ERD was done as a GCP instance and the other was done as an Azure instance. All of the screenshots from both the GCP database and Azure database are located within the folders.   

## Python Script for Database Interaction, Code Erros, and Troubleshooting Attempt:
I was able to develop a python script to connect to MySQL database however I kept encountering the same error when trying to push these changes into my GCP database. The following code is what I inserted into my python_connection.py file. 
```
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from pandas import read_sql

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)

# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM your_table_name"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, db_engine)
print(df)
```
Below is the error message I kept receiving when trying top push these changes to my GCP database. 
```
/alyssa_sorensen/mysql_cloudmanaged_databases/python_connection.pyn/python /home/
Python-dotenv could not parse statement starting at line 1
Traceback (most recent call last):
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 644, in connect
    sock = socket.create_connection(
  File "/usr/lib/python3.9/socket.py", line 843, in create_connection
    raise err
  File "/usr/lib/python3.9/socket.py", line 831, in create_connection
    sock.connect(sa)
OSError: [Errno 99] Cannot assign requested address

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 145, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3288, in raw_connection
    return self.pool.connect()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 452, in connect
    return _ConnectionFairy._checkout(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 1267, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 716, in checkout
    rec = pool._do_get()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 170, in _do_get
    self._dec_overflow()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 167, in _do_get
    return self._create_connection()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 393, in _create_connection
    return _ConnectionRecord(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 678, in __init__
    self.__connect()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 903, in __connect
    pool.logger.debug("Error on connect(): %s", e)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 898, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 637, in connect
    return dialect.connect(*cargs, **cparams)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 615, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 358, in __init__
    self.connect()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 711, in connect
    raise exc
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'localhost' ([Errno 99] Cannot assign requested address)")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/alyssa_sorensen/mysql_cloudmanaged_databases/python_connection.py", line 37, in <module>
    tables = get_tables(db_engine)
  File "/home/alyssa_sorensen/mysql_cloudmanaged_databases/python_connection.py", line 28, in get_tables
    inspector = inspect(engine)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/inspection.py", line 145, in inspect
    ret = reg(subject)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/reflection.py", line 303, in _engine_insp
    return Inspector._construct(Inspector._init_engine, bind)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/reflection.py", line 236, in _construct
    init(self, bind)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/reflection.py", line 247, in _init_engine
    engine.connect().close()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3264, in connect
    return self._connection_cls(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 147, in __init__
    Connection._handle_dbapi_exception_noconnection(
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2426, in _handle_dbapi_exception_noconnection
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 145, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3288, in raw_connection
    return self.pool.connect()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 452, in connect
    return _ConnectionFairy._checkout(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 1267, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 716, in checkout
    rec = pool._do_get()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 170, in _do_get
    self._dec_overflow()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 167, in _do_get
    return self._create_connection()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 393, in _create_connection
    return _ConnectionRecord(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 678, in __init__
    self.__connect()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 903, in __connect
    pool.logger.debug("Error on connect(): %s", e)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 898, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 637, in connect
    return dialect.connect(*cargs, **cparams)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 615, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 358, in __init__
    self.connect()
  File "/home/alyssa_sorensen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 711, in connect
    raise exc
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'localhost' ([Errno 99] Cannot assign requested address)")
(Background on this error at: https://sqlalche.me/e/20/e3q8)
```
I was able to create a .env file and a .gitignore file. Initially, I thought the information inputted into my .env file was incorrect, so I tried relabeling each of the components of the .env file from the database. I finally realized I properly labeled the information in my .env file, but I was still receiving the same error message. 

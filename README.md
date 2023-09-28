# mysql_cloudmanaged_databases
## **HHA 504 HW Assignment 4**
This task centers around MySQL, delving into its deployment across prominent cloud platforms such as Azure and GCP. Upon completion, I will have acquired practical proficiency in configuring MySQL on these platforms. Additionally, I will become adept at employing MySQL Workbench for database design and management, and if desired, I can also learn to establish connections to my database using Python to retrieve data.
## Setup process for Azure.
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

## Setup process for GCP.
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

## My experience with MySQL Workbench, including the ERD creation and database interactions. 



## My Python to database interaction approach and findings.



## Documented code errors and your troubleshooting attempts.
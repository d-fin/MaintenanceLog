# MaintenanceLog
David Finley 
Description: An app that keep tracks of maintenance schedules and inventory logs. 

# Installation Instructions 

# Install mysql
    ```
    sudo apt install mysql-server
    ```

- create database 

    ```
    $ mysql -u root -p
    mysql> CREATE database maintenancelog;
    ```
  
- navigate to sql file location 

    ```
    $ mysql -u root -p maintenancelog < maintenancelog.sql
    ```

- Create user 

    ```
    mysql> CREATE USER 'djangouser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    mysql> GRANT ALL ON maintenancelog.* TO 'djangouser'@'localhost';
    mysql> FLUSH PRIVILEGES;
    ```

# Install virtual enviornment 

    ```
    $ sudo apt install virtualenv -y
    $ virtualenv <envname> -p  python3
    ```

- Activate mysql and virtual enviornment 

    ```
    $ sudo service mysql start
    ```

- Navigate to env 

    ```
    $ source bin/activate 
    ```

# Install python dependencies 

- Navigate to "requirements.txt" file location

    ```
    $ python3 install -r requirements.txt
    ```

# Running the test server 

- Make DB migrations 

    ```
    (env)$ python3 manage.py makemigrations 
    (env)$ python3 manage.py migrate 
    ```

- Start django server 

    ```
    (env)$ python3 manage.py runserver 
    ```

# Deploy
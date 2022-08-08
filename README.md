# MaintenanceLog
# David Finley 

- Description: An app that keep tracks of maintenance schedules and inventory logs. 
- Install instructions are for Ubuntu Linux. Most commands will work on macOS with minor tweaks. 

# Installation Instructions 
# -----------------------------------------------------------
# Install mySQL Server and create database 

- Install 

    ```
    sudo apt-get install mysql-server
    ```

- Create database 

    ```
    $ mysql -u root -p
    mysql> CREATE database maintenancelog;
    ```
  
- Navigate to sql file location 

    ```
    $ mysql -u root -p maintenancelog < maintenancelog.sql
    ```

- Create user 

    ```
    mysql> CREATE USER 'djangouser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    mysql> GRANT ALL ON maintenancelog.* TO 'djangouser'@'localhost';
    mysql> FLUSH PRIVILEGES;
    ```

# -----------------------------------------------------------
# Install/create/activate virtual enviornment 

- Install virtualenv 

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

# -----------------------------------------------------------
# Install python + python dependencies 

- Install python 

    ```
    (env)$ sudo apt-get install python3
    ```

- Navigate to "requirements.txt" file location (make sure pip is up to date)

    ```
    (env)$ python3 install -r requirements.txt
    ```

# -----------------------------------------------------------
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

# -----------------------------------------------------------
# Deploy
# SQL Databases

In JetDeploy console you can start a fully dedicated SQL Database instance. Supported types are:

- PostgreSQL <span><img src="_images/postgresql.png" alt="PostgreSQL" width="28px"></span>
- MariaDB <span><img src="_images/mariadb.png" alt="MariaDB" width="28px"></span>
- MySQL <span><img src="_images/mysql.png" alt="MySQL" width="28px"></span>

### Create

During service creation you need to select:

- __Engine__  
  
  Choose one of the supported database type and version

- __Service name__  
  
  A unique service ident name. This name cannot be changed after creation. A random string is filled as initial default value

Click _Next_ button to add few more specifications:

- __Database name__  
  
  Choose a database name that will be created on setup

- __Storage size__  
  
  Define the initial max storage size of the database

```{note}
Connection and authentication data (e.g. username, password, FQDN) will be visible in the detail page after database creation success.
```

Click _Next_ button and the database creation process will start.


### Details

In the _Service Detail_ page you can access to various information of your database:

- __Engine__  
  
  Engine of your database (e.g. PostgreSQL, MariaDB, etc.)

- __Version__  
  
  Full version of your running database engine (e.g. `13.8` for PostgreSQL, `10.7` for MariaDB, etc.)

- __Status__  
  
  Status of your database engine. To be fully operational your database must be in `Ready` state.

- __External Endpoint__
  
  It is the external endpoint of your database instance, reachable by your laptop, external services or apps running out of JetDeploy infrastructure. `<External-Host>`:`<External-Port>` you find here can be used to connect by client utilities (_psql_ for PostgreSQL, _mysql_ for MariaDB/MySQL) for database administration tasks.

  ```{note}
  Visible only when <span><img src="_images/expose.png" alt="PostgreSQL" width="60px"></span> action done
  ```

- __Internal Endpoint__  
  
  It is the internal endpoint of your database instance, reachable by other Services or Apps you create in JetDeploy. `<Host>`:`<Port>` you find here can be used as _Environment variables_ in your App to connect to this database instance.

- __Database Name__  
  
  Name of the custom database (created at startup) you choose during the creation process. `<name>` of the database you find here can be used as _Environment variable_ in your App to connect to this database instance.

- __Username__  
  
  Root username of the database instance (e.g. `postgres` for PostgreSQL engine, `root` for MariaDB/MySQL).

```{tip}
For security reason we suggest you to create a new application-specific username and password, using a strong password and the least privilege principle
```

In the _Operations_ section, at bottom, you can view information of the tasks created by various Actions you can run on your SQL database using JetDeploy console.

### Actions

Different types of _Action_ can be executed on a SQL database instance:

<span><img src="_images/expose.png" alt="PostgreSQL" width="80px"> Use this action when you need to connect to your SQL database instance from external, e.g. your development computer or an application or service not running in JetDeploy platform.  
For security reasons we suggest you to keep _external access_ active for a short period of time, limited to the time necessary for data migration or database maintenance.</span>

<span><img src="_images/restart.png" alt="PostgreSQL" width="80px"> Invoke a restart of your SQL database instance.</span>

<span><img src="_images/destroy.png" alt="PostgreSQL" width="80px"> Request a service destroy of your SQL databse instance.</span>

```{warning}
`Destroy` action is risky and you will lose all your data. Please be absolutely sure when run this action.
```


### Settings

```{note}
JetDeploy is **in closed alpha** *status*, so at the moment to increase the Storage size after service creation you need to open a Support Request
```

### Usage examples


- `psql` utility for PostgreSQL

    First of all you should _Expose_ your Service if you run the utility on your local laptop.  
    Then check connection details in the _Service Detail_ page:

    ```{note}
    SQL Databases: `PostgreSQL`  
    Version: `13.8`  
    Status: `Ready`  
    External Endpoint: `creaky-pelting.gw1.jetdeploy.app:19184`  
    Internal Endpoint: `creaky-pelting:5432`  
    Database Name: `database-0` (created on setup)  
    Username: `postgres` (created on setup)  
    Password: `726221f8f95042e5be434df1a906bb5c`  
    ```
    
    Now you're ready to connect:

    ```bash
    $ psql -h creaky-pelting.gw1.jetdeploy.app -p 19184 -U postgres database-0
    ```
    
    Press enter. The utility will ask for a password:

    ```bash
    Password for user postgres:
    ```
    
    Insert the password and press Enter

    ```bash
    psql (13.8)
    Type "help" for help.

    database-0=#
    ```

    Great! You're connected to your SQL database instance!

 - `mysql` utility for MariaDB or MySQL

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
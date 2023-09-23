# SQL Database

In JetDeploy console you can start a fully dedicated SQL Database instance. Supported platforms are:

- PostgreSQL <span><img src="/_static/images/postgresql.png" alt="PostgreSQL" width="28px"></span>
- MariaDB <span><img src="/_static/images/mariadb.png" alt="MariaDB" width="28px"></span>

### Create

During service creation you need to select:

- __Type__
  
  Choose one of the supported database type and version

- __Service name__
  
  A unique service ident name. This name cannot be changed after creation. A random string is filled as initial default value

Click _Next_ button to add few more specifications:

- __Database name__
  
  Choose a database name that will be created on setup

- __Storage size__
  
  Define the initial max storage capacity of the database instance

```{note}
Connection and authentication data (e.g. host, port, username and password) will be visible in the detail page after database creation success.
```

Click _Next_ button and the database creation process will start.

### Details

In the _Service Detail_ page you can access to various information of your database:

- __Type__
  
  Type of your database instance (e.g. PostgreSQL, MariaDB, etc.)

- __Version__
  
  Full version of your running database instance (e.g. `13.8` for PostgreSQL, `10.7` for MariaDB, etc.)

- __Status__
  
  Status of your database instance. To be fully operational it must be in `Ready` state.

- __External Endpoint__
  
  It is the external endpoint of your database instance, reachable by your laptop, external services or apps running out of JetDeploy infrastructure. `<External-Host>`:`<External-Port>` you find here can be used to connect by client utilities (_psql_ for PostgreSQL, _mysql_ for MariaDB) for database administration tasks.

  ```{note}
  Visible only when <span><img src="/_static/images/expose.png" alt="Expose" width="60px"></span> action done
  ```

- __Internal Endpoint__
  
  It is the internal endpoint of your database instance, reachable by other Services or Apps you create in JetDeploy. `<Host>`:`<Port>` you find here can be used as _Environment variables_ in your App to connect to this service.

- __Database Name__
  
  Name of the custom database (created at startup) you choose during the creation process. `<name>` of the database you find here can be used as _Environment variable_ in your App to connect to this database instance.

- __Username__
  
  Root user of the database instance (e.g. `postgres` for PostgreSQL, `root` for MariaDB).

- __Password__
  
  Random generated password of the root user.

```{tip}
For security reason we suggest you to create a new application-specific username and password, using password policy recommendations and the least privilege principle
```

You could find additional fields in the _Service Detail_ page that are specific for the type of Service you're running.

In the _Operations_ section, at bottom, you can view information of the tasks created by various Actions you can run on your SQL database using JetDeploy console.

### Actions

Different types of _Action_ can be executed on your instance:

<span><img src="/_static/images/expose.png" alt="Expose" width="80px"> Use this action when you need to connect to your instance from external, e.g. your development computer or an application or service not running in JetDeploy platform.  
For security reasons we suggest you to keep _external access_ active for a short period of time, limited to the time necessary for data migration, troubleshooting or maintenance tasks.</span>

<span><img src="/_static/images/view-logs.png" alt="View Logs" width="80px"> Use this action when you need to view logs of your instance.</span>

<span><img src="/_static/images/start.png" alt="Start" width="30px"> Start of your instance, usually when your instance has been previously stopped.</span>

<span><img src="/_static/images/stop.png" alt="Stop" width="30px"> Stop of your instance</span>

<span><img src="/_static/images/restart.png" alt="Restart" width="30px"> Restart of your instance.</span>

<span><img src="/_static/images/destroy.png" alt="Destroy" width="30px"> Request a service destroy of your instance.</span>

```{warning}
`Destroy` action is risky and you will lose all your data. Please be absolutely sure when run this action.
```

### Settings

```{note}
JetDeploy is **in closed alpha** *status*, so at the moment to increase the Storage size after service creation you need to open a Support Request
```

### Usage examples

#### PostgreSQL

- `psql` utility

    First of all you should _Expose_ your Service if you run the utility on your local laptop.  
    Then check connection details in the _Service Detail_ page:

    ```{note}
    Type: `PostgreSQL`  
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

    Great! You're now ready to use your SQL database instance!

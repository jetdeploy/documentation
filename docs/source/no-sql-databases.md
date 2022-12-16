# No-SQL Databases

In JetDeploy console you can start a fully dedicated No-SQL database instance. Supported platforms are:

- MongoDB <span><img src="/_static/images/mongodb.png" alt="MongoDB" width="28px"></span>
- Elasticsearch <span><img src="/_static/images/elasticsearch.png" alt="Elasticsearch" width="28px"></span>

### Create

During service creation you need to select:

- __Type__
  
  Choose one of the supported platform type and version

- __Service name__
  
  A unique service ident name. This name cannot be changed after creation. A random string is filled as initial default value

Click _Next_ button to add few more specifications:

- __Storage size__
  
  Define the initial max storage capacity of the database instance

```{note}
Connection and authentication data (e.g. host, port, username and password) will be visible in the detail page after database creation success.
```

Click _Next_ button and the database creation process will start.

### Details

In the _Service Detail_ page you can access to various information of your database:

- __Type__
  
  Type of your database instance (e.g. MongoDB, Elasticsearch)

- __Version__
  
  Full version of your running database instance (e.g. `6.0.2` for MongoDB, `8.4.3` for Elasticsearch)

- __Status__
  
  Status of your database instance. To be fully operational it must be in `Ready` state.

- __External Endpoint__
  
  It is the external endpoint of your database instance, reachable by your laptop, external services or apps running out of JetDeploy infrastructure. `<External-Host>`:`<External-Port>` you find here can be used to connect by client utilities (_mongosh_ for MongoDB, _curl_ or _curator_ for Elasticsearch) for database administration tasks.

  ```{note}
  Visible only when <span><img src="/_static/images/expose.png" alt="Expose" width="60px"></span> action done
  ```

- __Internal Endpoint__
  
  It is the internal endpoint of your database instance, reachable by other Services or Apps you create in JetDeploy. `<Host>`:`<Port>` you find here can be used as _Environment variables_ in your App to connect to this service.

- __Username__
  
  Root user of the database instance (e.g. `root` for MongoDB, `elastic` for Elasticsearch).

- __Password__
  
  Random generated password of the root user.

```{tip}
For security reason we suggest you to create a new application-specific username and password, using password policy recommendations and the least privilege principle
```

You could find additional fields in the _Service Detail_ page that are specific for the type of Service you're running. For example in Elasticsearch detail page you can find the `Kibana Endpoint` too.

In the _Operations_ section, at bottom, you can view information of the tasks created by various Actions you can run on your SQL database using JetDeploy console.

### Actions

Different types of _Action_ can be executed on your instance:

<span><img src="/_static/images/expose.png" alt="Expose" width="80px"> Use this action when you need to connect to your SQL database instance from external, e.g. your development computer or an application or service not running in JetDeploy platform.  
For security reasons we suggest you to keep _external access_ active for a short period of time, limited to the time necessary for data migration or database maintenance.</span>

<span><img src="/_static/images/restart.png" alt="Restart" width="80px"> Invoke a restart of your SQL database instance.</span>

<span><img src="/_static/images/destroy.png" alt="Destroy" width="80px"> Request a service destroy of your SQL databse instance.</span>

```{warning}
`Destroy` action is risky and you will lose all your data. Please be absolutely sure when run this action.
```

### Settings

```{note}
JetDeploy is **in closed alpha** *status*, so at the moment to increase the Storage size after service creation you need to open a Support Request
```

### Usage examples

#### MongoDB

- `mongosh` (MongoDB shell)

    First of all you should _Expose_ your Service if you run the utility on your local laptop.  
    Then check connection details in the _Service Detail_ page:

    ```{note}
    Type: `MongoDB`  
    Version: `6.0.2`  
    Status: `Ready`  
    External Endpoint: `journal-savagery.gw1.jetdeploy.app:42747`  
    Internal Endpoint: `journal-savagery:5432`  
    Database Name: `database-0` (created on setup)  
    Username: `root` (created on setup)  
    Password: `e79e4727acba497fb5c03bab02c1baa6`  
    ```

    Now you're ready to connect:

    ```bash
    $ mongosh -u root "mongodb://journal-savagery.gw1.jetdeploy.app:42747"
    ```
    
    Press enter. The utility will ask for a password:

    ```bash
    Enter password:
    ```
    
    Insert the password and press Enter

    ```bash
    Current Mongosh Log ID: 639c504aa274055dbe10548a
    Connecting to:          mongodb://<credentials>@journal-savagery.gw1.jetdeploy.app:42747/?directConnection=true&appName=mongosh+1.6.1
    Using MongoDB:          6.0.2
    Using Mongosh:          1.6.1
    ...
    test> show dbs
    admin   100.00 KiB
    config   12.00 KiB
    local    72.00 KiB
    test>
    ```

    Great! You're now ready to use your MongoDB instance!

#### Elasticsearch

- Kibana

    Simply visit your instance Kibana endpoint and insert credentials to authenticate!

- `curl` command line tool

    First of all you should _Expose_ your Service if you run the utility on your local laptop.  
    Then check connection details in the _Service Detail_ page:

    ```{note}
    Type: `Elasticsearch`  
    Version: `8.4.3`  
    Status: `Ready`  
    External Endpoint: `https://blustery-morose.jetdeploy.app`  
    Internal Endpoint: `blustery-morose-elasticsearch:9200`  
    Username: `elastic` (created on setup)  
    Password: `037ffa5790ae42439d113c83bd16587e`  
    Kibana Endpoint: `https://blustery-morose-kibana.jetdeploy.app`  
    ```

    Now you're ready to connect:

    ```bash
    $ curl -X GET -u elastic:037ffa5790ae42439d113c83bd16587e 'https://blustery-morose.jetdeploy.app/_cat/indices?v'
    health status index uuid pri rep docs.count docs.deleted store.size pri.store.size  
    
    $ curl -X GET -u elastic:037ffa5790ae42439d113c83bd16587e 'https://blustery-morose.jetdeploy.app/_cat/shards?pretty'
    .geoip_databases                                              0 p STARTED  40  38.2mb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .kibana-event-log-8.4.3-000001                                0 p STARTED   1   6.2kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .security-7                                                   0 p STARTED 110 321.1kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .kibana_task_manager_8.4.3_001                                0 p STARTED  25   400kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .security-profile-8                                           0 p STARTED   1   7.9kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .ds-ilm-history-5-2022.12.16-000001                           0 p STARTED   9  20.1kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .kibana_security_session_1                                    0 p STARTED   1   5.7kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .apm-custom-link                                              0 p STARTED   0    225b 10.42.1.198 blustery-morose-elasticsearch-master-0
    .kibana_8.4.3_001                                             0 p STARTED 272   2.6mb 10.42.1.198 blustery-morose-elasticsearch-master-0
    .apm-agent-configuration                                      0 p STARTED   0    225b 10.42.1.198 blustery-morose-elasticsearch-master-0
    .ds-.logs-deprecation.elasticsearch-default-2022.12.16-000001 0 p STARTED   1  12.6kb 10.42.1.198 blustery-morose-elasticsearch-master-0
    ```

    Great! You're now ready to use your Elasticsearch instance!
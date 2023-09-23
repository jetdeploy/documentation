# No-SQL Database

In JetDeploy console you can start a fully dedicated No-SQL database instance. Supported platforms are:

- Opensearch <span><img src="/_static/images/opensearch.png" alt="Opensearch" width="28px"></span>

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
  
  Type of your database instance (e.g. Opensearch)

- __Version__
  
  Full version of your running database instance

- __Status__
  
  Status of your database instance. To be fully operational it must be in `Ready` state.

- __External Endpoint__
  
  It is the external endpoint of your database instance, reachable by your laptop, external services or apps running out of JetDeploy infrastructure. `<External-Host>`:`<External-Port>` you find here can be used to connect by client utilities for database administration tasks.

  ```{note}
  Visible only when <span><img src="/_static/images/expose.png" alt="Expose" width="60px"></span> action done
  ```

- __Internal Endpoint__
  
  It is the internal endpoint of your database instance, reachable by other Services or Apps you create in JetDeploy. `<Host>`:`<Port>` you find here can be used as _Environment variables_ in your App to connect to this service.

- __Username__
  
  Root user of the database instance (e.g. `admin` for Opensearch).

- __Password__
  
  Random generated password of the root user.

```{tip}
For security reason we suggest you to create a new application-specific username and password, using password policy recommendations and the least privilege principle
```

You could find additional fields in the _Service Detail_ page that are specific for the type of Service you're running. For example in Opensearch detail page you can find the `Dashboards Endpoint` too.

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

#### Opensearch

- Dashboards

    Simply visit your instance Dashboards endpoint and insert credentials to authenticate!

- `curl` command line tool

    First of all you should _Expose_ your Service if you run the utility on your local laptop.  
    Then check connection details in the _Service Detail_ page:

    ```{note}
    Type: `Opensearch`  
    Version: `8.4.3`  
    Status: `Ready`  
    External Endpoint: `https://blustery-morose.jetdeploy.app`  
    Internal Endpoint: `blustery-morose-opensearch:9200`  
    Username: `elastic` (created on setup)  
    Password: `037ffa5790ae42439d113c83bd16587e`  
    Dashboards Endpoint: `https://blustery-morose-dashboards.jetdeploy.app`  
    ```

    Now you're ready to connect:

    ```bash
    $ curl -X GET -u elastic:037ffa5790ae42439d113c83bd16587e 'https://blustery-morose.jetdeploy.app/_cat/indices?v'
    health status index uuid pri rep docs.count docs.deleted store.size pri.store.size  
    
    $ curl -X GET -u elastic:037ffa5790ae42439d113c83bd16587e 'https://blustery-morose.jetdeploy.app/_cat/shards?pretty'
    .geoip_databases                                              0 p STARTED  40  38.2mb 10.42.1.198 blustery-morose-opensearch-master-0
    .dashboards-event-log-8.4.3-000001                                0 p STARTED   1   6.2kb 10.42.1.198 blustery-morose-opensearch-master-0
    .security-7                                                   0 p STARTED 110 321.1kb 10.42.1.198 blustery-morose-opensearch-master-0
    .dashboards_task_manager_8.4.3_001                                0 p STARTED  25   400kb 10.42.1.198 blustery-morose-opensearch-master-0
    .security-profile-8                                           0 p STARTED   1   7.9kb 10.42.1.198 blustery-morose-opensearch-master-0
    .ds-ilm-history-5-2022.12.16-000001                           0 p STARTED   9  20.1kb 10.42.1.198 blustery-morose-opensearch-master-0
    .dashboards_security_session_1                                    0 p STARTED   1   5.7kb 10.42.1.198 blustery-morose-opensearch-master-0
    .apm-custom-link                                              0 p STARTED   0    225b 10.42.1.198 blustery-morose-opensearch-master-0
    .dashboards_8.4.3_001                                             0 p STARTED 272   2.6mb 10.42.1.198 blustery-morose-opensearch-master-0
    .apm-agent-configuration                                      0 p STARTED   0    225b 10.42.1.198 blustery-morose-opensearch-master-0
    .ds-.logs-deprecation.opensearch-default-2022.12.16-000001 0 p STARTED   1  12.6kb 10.42.1.198 blustery-morose-opensearch-master-0
    ```

    Great! You're now ready to use your Opensearch instance!

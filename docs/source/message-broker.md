# Message Broker

In JetDeploy console you can start a fully dedicated Message Broker instance to accomplish Publish/Subscribe pattern in your webapp architecture. Supported platform is:

- RabbitMQ <span><img src="/_static/images/rabbitmq.png" alt="RabbitMQ" width="20px"></span>

### Create

During service creation you need to select:

- __Type__
  
  Choose one of the supported platform type and version

- __Service name__
  
  A unique service ident name. This name cannot be changed after creation. A random string is filled as initial default value

Click _Next_ button to add few more specifications:

- __Storage size__
  
  Define the initial max storage capacity of the instance

```{note}
Connection and authentication data (e.g. host, port, username, password and management console) will be visible in the detail page after database creation success.
```

### Details

In the _Service Detail_ page you can access to various information of your database:

- __Type__
  
  Type of your message broker instance (e.g. RabbitMQ)

- __Version__
  
  Full version of your running message broker instance (e.g. `3.10.11` for RabbitMQ)

- __Status__
  
  Status of your message broker instance. To be fully operational it must be in `Ready` state.

- __External Endpoint__
  
  It is the external endpoint of your message broker instance, reachable by your laptop, external services or apps running out of JetDeploy infrastructure. `<External-Host>`:`<External-Port>` you find here can be used to connect by clients using TCP (AMQP) protocol.

  ```{note}
  Visible only when <span><img src="/_static/images/expose.png" alt="Expose" width="60px"></span> action done
  ```

- __Internal Endpoint__
  
  It is the internal endpoint of your message broker instance, reachable by other Services or Apps you create in JetDeploy. `<Host>`:`<Port>` you find here can be used as _Environment variables_ in your App to connect to this service.

- __Console Endpoint__
  
  URL of management console of the instance. The endpoint you find here can be used for troubleshooting or administration tasks. 

  ```{note}
  Visible only when Service type provide a management console
  ```

- __Username__
  
  Administrator username of the message broker instance (e.g. `admin` for RabbitMQ).

- __Password__
  
  Random generated password of the Administrator user.

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

#### RabbitMQ

- Management `console` of RabbitMQ

    Simply visit your instance Console endpoint and insert credentials to authenticate!

- `rabbitmqadmin` command line tool

    Check connection details in the _Service Detail_ page:

    ```{note}
    Type: `RabbitMQ`  
    Version: `3.10.11`  
    Status: `Ready`  
    External Endpoint: `bards-tats.gw1.jetdeploy.app:18154`  
    Internal Endpoint: `bards-tats:5672`  
    Console Endpoint: `https://bards-tats.jetdeploy.app`  
    Username: `admin` (created on setup)  
    Password: `26f9a4ae79e64a4e804056561ca32be4`  
    ```

    Download _rabbitmqadmin_ command line tool; it can be downloaded directly from your RabbitMQ instance.  
    Navigate to [https://bards-tats.jetdeploy.app/cli/rabbitmqadmin](https://bards-tats.jetdeploy.app/cli/rabbitmqadmin) to download it. The tool requires a supported version of Python to be installed on your machine, so we suggest to use a Linux machine, OSX or WSL2 for Windows.

    ><small> (read more: [https://www.rabbitmq.com/management-cli.html](https://www.rabbitmq.com/management-cli.html))</small>

    Now you're ready to connect:

    ```bash
    $ rabbitmqadmin \
      --host bards-tats.jetdeploy.app \
      --port 443 \
      --ssl \
      --vhost / \
      --username admin \
      --password 26f9a4ae79e64a4e804056561ca32be4 \
      list users
    +-------+--------------------------------+--------------------------------------------------+---------------+
    | name  |       hashing_algorithm        |                  password_hash                   |     tags      |
    +-------+--------------------------------+--------------------------------------------------+---------------+
    | admin | rabbit_password_hashing_sha256 | Sg4nE8NveZ/PzK1QHyDftr2tU2OPz1ae2ciyqd88byKur9BC | administrator |
    +-------+--------------------------------+--------------------------------------------------+---------------+
    ```

    Great! You're now ready to use your message broker instance!
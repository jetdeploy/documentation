# S3 Object Storage

In JetDeploy console you can start a fully dedicated S3-compatible Object Storage instance. Supported platform is:

- MinIO <span><img src="/_static/images/minio.png" alt="MinIO" width="32px"></span>

### Create

During service creation you need to select:

- __Type__
  
  Choose one of the supported platform type and version

- __Service name__
  
  A unique service ident name. This name cannot be changed after creation. A random string is filled as initial default value

Click _Next_ button to add few more specifications:

- __Storage size__
  
  Define the initial max storage size of the database

```{note}
Connection and authentication data (e.g. host, port, username, password and management console) will be visible in the detail page after database creation success.
```

### Details

In the _Service Detail_ page you can access to various information of your database:

- __Type__
  
  Type of your Object Storage instance (e.g. MinIO)

- __Version__
  
  Full version of your running Object Storage instance (e.g. `2022.11.8` for MinIO)

- __Status__
  
  Status of your Object Storage instance. To be fully operational it must be in `Ready` state.

- __External Endpoint__
  
  It is the external endpoint of your Object Storage instance, reachable by your laptop, external services or apps running out of JetDeploy infrastructure. `<External-Host>`:`<External-Port>` you find here can be used to connect by client utilities (_s3cmd_ or _mc_ for MinIO) for transfering data or some administration tasks.

  ```{note}
  Visible only when <span><img src="/_static/images/expose.png" alt="Expose" width="60px"></span> action done
  ```

- __Internal Endpoint__
  
  It is the internal endpoint of your Object Storage instance, reachable by other Services or Apps you create in JetDeploy. `<Host>`:`<Port>` you find here can be used as _Environment variables_ in your App to connect to this service.

- __Console Endpoint__
  
  URL of management console of the instance. The endpoint you find here can be used for troubleshooting or administration tasks. 

  ```{note}
  Visible only when Service type provide a management console
  ```

- __Console Username / S3 AccessKey__
  
  S3 Access Key ID of the Object Storage instance (e.g. `root` for MinIO).

- __Console Password / S3 SecretKey__
  
  S3 Secret Access Key of the Object Storage instance.

```{tip}
For security reason we suggest you to create a new application-specific Access Key ID and Secret Access Key, using password policy recommendations and the least privilege principle
```

In the _Operations_ section, at bottom, you can view information of the tasks created by various Actions you can run on your SQL database using JetDeploy console.

### Actions

Different types of _Action_ can be executed on a SQL database instance:

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

- Management `Console` of MinIO

    Simply visit your instance Console endpoint and insert credentials to authenticate!

- `s3cmd` or `mc` utility for MinIO

    First of all you should _Expose_ your Service if you run the utility on your local laptop.  
    Then check connection details in the _Service Detail_ page:

    ```{note}
    Type: `MinIO`  
    Version: `2022.11.8`  
    Status: `Ready`  
    External Endpoint: `https://dampened-bouts.jetdeploy.app`  
    Internal Endpoint: `http://dampened-bouts:9000`  
    Console Endpoint: `https://dampened-bouts-console.jetdeploy.app`  
    Console Username / S3 Access Key ID: `root` (created on setup)  
    Console Password / S3 Secret Access Key: `VTy5LPHnutiGT8/V8Waf3zfy8Qug+BoV8OzsJIAs`  
    ```

    Now you're ready to connect:

    - S3 command line tool `s3cmd`

        ```bash
        $ s3cmd \
        --host="dampened-bouts.jetdeploy.app" \
        --host-bucket="dampened-bouts.jetdeploy.app" \
        --access_key="root" \
        --secret_key="VTy5LPHnutiGT8/V8Waf3zfy8Qug+BoV8OzsJIAs" \
        mb s3://test-bucket
        Bucket 's3://test-bucket/' created
        ```
        
        Alternatively you can set a static configuration using `s3cmd --configure`.

        ><small> (read more: [https://s3tools.org/s3cmd-howto](https://s3tools.org/s3cmd-howto))</small>

    - MinIO client `mc`
    
        ```bash
        $ mc alias set dampened-bouts https://dampened-bouts.jetdeploy.app
        Enter Access Key: root  
        Enter Secret Key:
        Added `dampened-bouts` successfully.

        $ mc mb dampened-bouts/test-bucket2
        Bucket created successfully `dampened-bouts/test-bucket2`.
        $ mc ls dampened-bouts
        [2022-12-16 09:56:41 CET]     0B test-bucket/
        [2022-12-16 10:03:38 CET]     0B test-bucket2/
        ```
        
        ><small> (read more: [https://min.io/docs/minio/linux/reference/minio-mc.html](https://min.io/docs/minio/linux/reference/minio-mc.html))</small>

    Great! You're now ready to use your S3 Object Storage instance!
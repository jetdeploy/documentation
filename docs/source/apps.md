## Apps

### Components

Putting it simply, in JetDeploy world an _app_ is a web-app that you can deploy and spin-up to serve your clients. An app has an execution-context which contains

*   **app domain** - like e.g. `your-app.{{ settings.DOMAIN_APP }}`
*   **environment variables** - they are accessible in your code
*   **running logs** - common runtime logs, depending on your app or DBMS
*   **black box operations** - a list of the operation that are been performed on that app (e.g. boot up, destroy, etc.). The _post-mortem_ logs of the operations are always available to read.

**Please note** an app is a stateless container, that is, it can't hold anything, it's a mere code executor. If you need to persist data (and clearly you do) please attach to it a [Database](#resources-databases)

#### Environment Variables

JetDeploy supports declaring environment variables and lets you store data such as configuration settings, encryption keys, etc in such environment variables.  
A nice form makes them easy to define, share and update for your services. At runtime, environment variables are exposed to the application inside the app context.

**For example** if you insert a row in the environment form like that: _SOME\_KEY -> SOME\_VALUE_ then in your code you will get _SOME\_VALUE_ with something like: `os.getenv('SOME_KEY')`

*   [Resources](#resources)
    *   [Apps](#resources-apps)
    *   [Platforms supported](#resources-platforms)
    *   [Databases](#resources-databases)
*   [Environment Variables](#envs)

#### Platforms supported

You can freely deploy and spin-up your web app in one of the following platforms:

*   Node.js support
*   Ruby support
*   Python support ( both 2.x & 3.x runtimes )
*   PHP support
*   Go support

### Databases

A _database_ is, in JetDeploy world specific definition, an entity that simply represents a DBMS SQL/noSQL service that could be attached to an app.

Creating a new database is simple as choice one of the available DBMS.

Databases supported:

*   MariaDB
*   Memcached
*   PostgreSQL
*   RabbitMQ
*   Redis
*   Opensearch

When attached to an app, your code can access to the database service and data through the typicals `user:password@host:port` parameters that you'll find in you database detail page.

**Please note** you can easily connect to DB also from outside. To do it, simply _"expose"_ the service from the database detail page.

This is not supported for `Memcached` DBMS.

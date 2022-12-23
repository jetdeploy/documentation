## Resources

In JetDeploy you can create different kind of services that allow you to store your data and run your web application to serve your clients.

Our supported services are:

* [Apps](#apps)
* [SQL Databases](#sql-databases)
* [No-SQL Databases](#no-sql-databases)
* [In-Memory DB](#in-memory-db)
* [Message Brokers](#message-brokers)
* [S3 Object Storage](#s3-object-storage)

### Apps

Putting it simply, in JetDeploy world an _App_ is a running instance of your web-app, built from your source code and containerized using your application runtime.  
Connect your App with one or more services below you can create with e few clicks!

> Create new {doc}`apps`!

### SQL Databases

A _SQL database_ is a dedicated DBMS engine instance you can use to store your data. If your web-app is backed by a database like PostgreSQL, MariaDB, MySQL or other relational DBMS, this kind of service is the right choice for you.

> Create a {doc}`sql-database`!

### No-SQL Databases

A _No-SQL database_ is usually related to a non-tabular database engine. With this kind of service you can run your dedicated instance of MongoDB or Elasticsearch.

> Create a {doc}`no-sql-database`!

### In-Memory DB

An _In-Mememory DB_ refers to a database sytem that rely primarily on memory for data storage. This service, like Redis or Memcached, is mostly used for caching or to speed up specific tasks of your web application.

Depending on how your application is made up, you may also benefit from this kind of services.

> Create an {doc}`in-memory-db`!

### Message Brokers

A _Message Broker_ refers to a software component used for applications to communicate with each other. It provides the exchange of information between applications by transmitting messages received from the producer to consumer.

With this kind of service you simplify coding of decoupled applications, make communication asynchronous between your components while improving performance, reliability and scalability.

> Create a {doc}`message-broker`!

### S3 Object Storage

An _Object storage_ is a data storage architecture for storing unstructured data; the data is broken into discrete units called objects and you can put or retrieve these objects through HTTP and REST API calls.

Your application architecture may need this kind of service to store flat data, for backup purposes or to serve static content.

> Create an {doc}`s3-object-storage`!
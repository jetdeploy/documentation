# Welcome to JetDeploy's documentation!

- Create Foundation services
- Get connection data of Foundation services

	PostgreSQL

	Internal Endpoint: helluva-caption:5432
	Database Name: celero
	Username: postgres
	Password: ******************

	Elastic

	Internal Endpoint: diaspora-dittos-elasticsearch:9200
	Username: elastic
	Password: ******************

	RabbitMQ

	Internal Endpoint: slim-saddle:5672
	Username: admin
	Password: ******************

	MinIO S3

	Internal Endpoint: http://payable-commando:9000
	Console Username / S3 AccessKey: root (created on setup)
	Console Password / S3 SecretKey: ******************
	
- ONLY IN MIGRATION SCENARIOS

	- Expose your new Foundation services (when needed) to be reachable from your resources located outside of JetDeploy
	- Restore your data to new Foundation services (when needed)
	- Adjust application settings upon connection data of the previous Foundation services

- Create your App

- Push your code to JetDeploy
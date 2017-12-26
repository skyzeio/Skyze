# Skyze Messaging Architecture

## protocols
### Advanced Message Queuing Protocol
http://www.amqp.org/

## Libraries

### Lists of Libraries
http://queues.io/

###RabbitMQ
is the most widely deployed open source message broker.

With more than 35,000 production deployments of RabbitMQ world-wide at small startups and large enterprises, RabbitMQ is the most popular open source message broker.

RabbitMQ is lightweight and easy to deploy on premises and in the cloud. It supports multiple messaging protocols. RabbitMQ can be deployed in distributed and federated configurations to meet high-scale, high-availability requirements.

### Celery: Distributed Task Queue
Celery is an asynchronous task queue/job queue based on distributed message passing.	It is focused on real-time operation, but supports scheduling as well.
The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet,	or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

### Redis Queue (RQ)
Redis Queue (RQ) is a Python task queue implementation that uses Redis to keep track of tasks in the queue that need to be executed.

**Con**
relied on polling meant that it would not scale as they needed, and replication would need to be manually built out, adding additional work to implement it. Also, Redis is an in-memory solution, which in events where the queues built up if the machines ran out of memory, there was risk to lose the tasks.

### Dramatiq
Dramatiq is a fast and reliable Python task queue that came about as an alternative to Celery. It supports RabbitMQ and Redis as message brokers.
https://dramatiq.io/

### Mongo
Mongo has two main features which make it possible to easily implement a durable, replicated message queue on top of it: very simple replication setup (we’ll be using a 3-node replica set), and various document-level atomic operations, like find-and-modify. The implementation is just a handful of lines of code; take a look at MongoMq.


# Skyze Architecutre
Draft v0.1

## Contents
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Skyze Architecutre](#skyze-architecutre)
	- [Contents](#contents)
	- [Design Principles](#design-principles)
	- [Project values](#project-values)
	- [Service architecture](#service-architecture)
		- [Microservices goals](#microservices-goals)
		- [Microservices Architecture Patterns Used](#microservices-architecture-patterns-used)
		- [MicroServices and GAE](#microservices-and-gae)
		- [Services Design - Business / Functional](#services-design-business-functional)
		- [Services Design - Non-Functional](#services-design-non-functional)
		- [Services Existing Examples](#services-existing-examples)
			- [Apps](#apps)
			- [Screener](#screener)
	- [Class architecture](#class-architecture)
	- [Data Types](#data-types)
		- [numpy floating point](#numpy-floating-point)
			- [How python works with FP numbers](#how-python-works-with-fp-numbers)
			- [Solution - Decimal](#solution-decimal)
	- [Python](#python)
		- [Language](#language)
		- [Modules](#modules)
		- [Typing](#typing)
		- [Performance](#performance)
			- [Python function call overhead](#python-function-call-overhead)
	- [Virtual Environment](#virtual-environment)
		- [VE Manager](#ve-manager)
			- [pipenv](#pipenv)
		- [Development Environment](#development-environment)
		- [Production environment](#production-environment)
	- [Persistence](#persistence)
		- [Database](#database)
			- [MongoDB](#mongodb)
		- [File System](#file-system)
			- [csv](#csv)
			- [Excel](#excel)
	- [Code Resository](#code-resository)
		- [GitHub](#github)
	- [Code Quality](#code-quality)
		- [Standards](#standards)
			- [PEP8](#pep8)
		- [Linter](#linter)
			- [PyLint](#pylint)
		- [General code quality?](#general-code-quality)
			- [Code Climate](#code-climate)
			- [PyCodeStyle](#pycodestyle)
			- [PyDocStyle](#pydocstyle)
			- [coverage.py](#coveragepy)
	- [Testing](#testing)
		- [Test running](#test-running)
			- [nose](#nose)
				- [Doc](#doc)
				- [Install](#install)
			- [Test coverage](#test-coverage)
				- [Doc](#doc)
				- [Install](#install)
		- [Unit Testing](#unit-testing)
			- [unittest2](#unittest2)
		- [Continuous Integration](#continuous-integration)
	- [Documentation](#documentation)
		- [Requirements](#requirements)
		- [Solutions](#solutions)
			- [UML and other modelling](#uml-and-other-modelling)
				- [StarUML](#staruml)
				- [PieNSource](#piensource)
			- [Markdown](#markdown)
			- [Sphynx](#sphynx)
			- [GitWiki](#gitwiki)
	- [Project Management](#project-management)
		- [Requirement Management](#requirement-management)
			- [Trello](#trello)
		- [Defect Management](#defect-management)
			- [Production error reporting](#production-error-reporting)
			- [GIT Issues](#git-issues)
		- [Work Management](#work-management)
			- [Trello](#trello)
		- [Team Communications](#team-communications)
			- [Slack](#slack)
	- [Deployment Management](#deployment-management)
		- [Deployment Process](#deployment-process)
		- [Deployment Tools](#deployment-tools)

<!-- /TOC -->

## Design Principles
1. Hosted cloud architecture e.g. AWS, GCS, Azure
2. MicroService architecture
3. Open Source - choose OS Libraries over proprietary libraries and technologies
4. Flexibility and Agility e.g. don't use hosted prop tech to avoid lock in
5. Performant - certain components need high performance - e.g. the back tester ... design for performance first here e.g. may design it as a larger module rather than break it down into micro-services to avoid messaging latency
6. Free - look to use free hosting and other technologies over paid
7. Automation of development tasks - testing, continuous-integration, code-quality, repository, etc
8. Early and continuous delivery of value
9. Maintainable
10. Testable
11. Pythonic - suits the idioms of the technology we are using

## Project values
1. Self organising teams
2. Design and technical excellence
3. Collaboration
4. Open Source
5. Passionate contributors
6. Simplicity
7. Social Enterprise - People, Profit and Purpose
8. Agility


## Service architecture
__MicroService Architecture__: collection of loosely coupled services, which implement business capabilities
### Microservices goals
A properly implemented microservices-based application can achieve the following goals:
1. Define strong contracts between the various microservices.
2. Allow for independent deployment cycles, including rollback.
3. Facilitate concurrent, A/B release testing on subsystems.
4. Minimize test automation and quality-assurance overhead.
5. Improve clarity of logging and monitoring.
6. Provide fine-grained cost accounting.
7. Increase overall application scalability and reliability.

### Microservices Architecture Patterns Used
1. __Microservices__ - http://microservices.io/patterns/microservices.html
2. __Persistence__
	1. Database per service - Each service has it's own database http://microservices.io/patterns/data/database-per-service.htm
	2. SAGA - Data consistency between services is maintained using the Saga pattern. A saga is a sequence of local transactions each generating a message to trigger the next transaction. http://microservices.io/patterns/data/saga.html
3. __Deployment__
	1. Serverless deployment - lamda etc http://microservices.io/patterns/deployment/serverless-deployment.html
	2. Multiple service instances per host - EC2 VM etc http://microservices.io/patterns/deployment/multiple-services-per-host.html
	3. __Not sure where GAE fits in here__
4. __Inter-Services Communication__
	1. Messaging -  asynchronous messaging ... Services communicating by exchanging messages over messaging channels. http://microservices.io/patterns/communication-style/messaging.html
2. __Service Discovery__
		1. Service Registry - a database of services, their instances and their locations. http://microservices.io/patterns/service-registry.html
		2. Self Registration - A service instance is responsible for registering itself on startup with the service registry http://microservices.io/patterns/self-registration.html
		3. 3rd Party Registration - A 3rd party registrar is responsible for registering and unregistering a service instance with the service registry. http://microservices.io/patterns/3rd-party-registration.html
6. __Cross Cutting__
	1. Microservice Chasis - http://microservices.io/patterns/microservice-chassis.html
2. __Health Check__
	1. Health Check API - Sometimes a service instance can be incapable of handling requests yet still be running. A health check client - a monitoring service, service registry or load balancer - periodically invokes the endpoint to check the health of the service instance. http://microservices.io/patterns/observability/health-check-api.html
2. __Circuit Breaker__ http://microservices.io/patterns/reliability/circuit-breaker.html





### MicroServices and GAE
https://cloud.google.com/appengine/docs/standard/python/microservices-on-app-engine

### Services Design - Business / Functional
1. __Market data Updater__ - connects to external sources (exchanges, brokers and other data providers), extracts, transforms (to Skyze format) and loads data to Market data stores e.g Artic, CSV, etc - runs hourly
2. __Market Data Store__ - Serves data to other internal services on an adhoc basis - will exract data from various stores e.g. artic, sql, csv etc...
3. Portfolios
4. __Statistics__ - Creates _Market_ and _Portfolio_ statistics on back test results
5. __BackTester__ - runs _Strategies_ over a _Portfolio_ and collects results
	1. Optimizer
6. __Trading Engine__ - takes real time _order_ notifications and executes them
7. __Screener__ - runs a screener signal on a portfolio at regular intervals and triggers notifications
8. __Notifications__ - Sends SMS, emails etc
4. __Front End__ - web and mobile, simple data entry and graphs
5. __Adhoc Reporting__ - generating on the fly reports

### Services Design - Non-Functional
1. __Services Registrar__ - etcd (Opensource used by Kubernetes)
2. __Messaging Bus__ between services using a publish subscribe messaging pattern
3. __User Data Store__ - user data
4. __Load Balancer__ -
5. __Logging__ -
	1. Logging of normal application activity - Information, Debug, Warning.
	2. Logging of transactions for audit and compliance
	3. Aggregated across services
5. __Error Logging__ - Exceptions and Errors as they occur with debug info
6. __Load Balancer__ - HA Proxy

### Services Existing Examples
#### Apps
1. https://cryptotrader.org/

#### Screener
	1. https://finance.google.com/finance#stockscreener
	2. https://finviz.com/futures.ashx
	3. https://www.roburir.com/stock-screener.html
	4. https://www.zacks.com/screening/stock-screener
	5. https://markets.ft.com/data/equities?expandedScreener=true


## Class architecture

2. Indicator
3. Strategy
4. Portfolio

## Data Types

### numpy floating point
Problem with equality with very small differences. Have ben finding this problem
when comparing dataframes of timeseries of the output of indicators. It reports
that 13.84 != 13.84. When the difference is taken it is x*10^-15 ... so very
small diferences. Documented in github:
https://stackoverflow.com/questions/33549193/pandas-dataframe-comparison-and-floating-point-precision
https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python

PEP485: https://docs.python.org/3/whatsnew/3.5.html#pep-485-a-function-for-testing-approximate-equality
				https://www.python.org/dev/peps/pep-0485/

Documentation: Python: https://docs.python.org/3/library/math.html
							 Numpy:  https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.isclose.html

#### How python works with FP numbers
Python built on C. FP numbers go from python floating point to C as a fractoin and then back to Python as floating point. These conversions are not always accurate.

Numbers like 1.1 and 2.2 do not have exact representations in binary floating point. End users typically would not expect 1.1 + 2.2 to display as 3.3000000000000003 as it does with binary floating point.

#### Solution - Decimal
https://www.youtube.com/watch?v=JOGPAduCC7c

a = decimal.decimal(7.6)+decimal.decimal(7.9)
a.quantize("0.00")
a.quantize(decimal.Decimal("0.00"), rounding=decimal.ROUND_UP)


## Python

### Language
version 3.6

### Modules
Modules are documented in pipenv file at: https://github.com/SkyzeTrading/Skyze/blob/develop/Pipfile

Key packages are:

__Database__
1. pymongo   http://api.mongodb.com/python/current/index.html
2. AHL Artic https://github.com/manahl/arctic
3. MongoEngine ODM http://mongoengine.org/

__Adhac Reporting__ https://redash.io/

__Messaging Bus__
	1. 0MQ - http://zeromq.org/
	2. PyZMQ - Python bindings for 0MQ https://github.com/zeromq/pyzmq, doco https://pyzmq.readthedocs.io/en/latest/

What is ZeroMQ? According to Wikipedia: “ZeroMQ is a high-performance asynchronous messaging library aimed at use in scalable distributed or concurrent applications. It provides a message queue, but unlike message-oriented middleware, a ØMQ system can run without a dedicated message broker. The library is designed to have a familiar socket-style API.”
_Reading_
1. http://wiki.secondlife.com/wiki/Message_Queue_Evaluation_Notes
2. http://nichol.as/zeromq-an-introduction
3. https://stefan.sofa-rockers.org/2012/02/01/designing-and-testing-pyzmq-applications-part-1/

__Numerical Datatypes and scientific calculations__
1. pandas
2. numpy
3. scipy

http://www.scipy-lectures.org/

__Financial Markets__
1. TA Lib https://github.com/mrjbq7/ta-lib

__Code quality__
1. pylint

__Visualisation__
1. matplotlib
2. seaborn: statistical data visualization http://seaborn.pydata.org/

__Scheduler__
1. Advanced Pythn Scheduler - apscheduler http://apscheduler.readthedocs.io/

__Error Logging__
	1. Sentry https://sentry.io and Raven https://github.com/getsentry/raven-python
	2. Rollbar www.rollbar.io

__Testing__
1. SimPy -  discrete event-simulation library for Python https://stefan.sofa-rockers.org/2013/12/03/how-simpy-works/

__Notifications__
1. Twitter - Twython https://github.com/ryanmcgrath/twython
2. SMS - tweet to Skyze_IO, personal account subscribe to Skyze_io and
 have twitter notification send SMS for all skyze_io tweets in personal account
 3. eMail -



### Typing
Dropbox, Facebook have mandated static typing for their Python projets

__Dropbox Pycon Talk__  https://www.youtube.com/watch?v=7ZbwZgrXnwY&feature=youtu.be

__MyPy library__ http://mypy-lang.org/

__Static typing in Python__  https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b

### Performance
#### Python function call overhead
Function call overhead in Python is relatively high, especially compared with the execution speed of builtin functions. The overhead in Python is mainly due to the dynamic type checking of function arguments that must be performed before and after the function call. This strongly suggests that, where appropriate, functions should handle data aggregation rather than being called on a per element basis.

Testing in a Jupyter notebook:
http://localhost:8888/notebooks/Jupyter/Function%20Call%20Overhead.ipynb#Function-Call-Overhead

shows 10e8 function calls took 2.4 times longer than a single call over 10e8 iteration

## Virtual Environment
### VE Manager
#### pipenv
https://pypi.python.org/pypi/pipenv

### Development Environment
Set up like: ....

### Production environment
when we have one

## Persistence
### Database
#### MongoDB

### File System
#### csv
#### Excel

## Storing Confidential Information
### Environment variables
Used to store access keys and other sensitive environment specific data.
**on Mac in the shell** e.g. `~/.zshrc`
**on AWS ....** e.g. 

## Code Repository
### GitHub
https://github.com/SkyzeTrading/Skyze/

## Code Quality

### Standards
#### PEP8

### Linter
#### PyLint

### General code quality?
#### Code Climate
Used by over 100,000 projects, and analyzing over 2 billion lines of code daily, Code Climate incorporates fully-configurable test coverage and maintainability data throughout the development workflow, making quality improvement explicit, continous, and ubiquitous.

#### PyCodeStyle

#### PyDocStyle

#### coverage.py

## Testing

### Test running
#### nose
test runner and a great one at that. It can run tests created using unittest, py.test or doctest.

##### Doc
 http://nose.readthedocs.io/en/latest/index.html

##### Install
pipenv install nose --dev

#### Test coverage
Nose supports the coverage module:
##### Doc
https://coverage.readthedocs.io/en/coverage-4.4.1/

##### Install
pipenv install coverage --dev


### Unit Testing
#### unittest2


### Continuous Integration
http://docs.python-guide.org/en/latest/scenarios/ci/

## Documentation
### Requirements
1. Would love to get away from boring black and white!
2. General documentation - manuals, how to's, architecture etc
3. Code documentation - inline documentation mapped into code documents
4. Tags - to do 's etc
5. UML and other design tools

### Solutions
#### UML and other modelling
1. Looking for round trip class diagrams
##### StarUML
* generates Python
##### PieNSource
* Reverse engineers an image of a UML diagram

#### Markdown

#### Sphynx
Seems to be a favourite in the pythoniverse
http://www.sphinx-doc.org/en/stable/

#### GitWiki
Do we do this? How does this fit in?

## Project Management

### Requirement Management
#### Trello
https://trello.com/b/VdJ7MOCk/skyze-the-limit
Wishlist / Backlog

### Defect Management

#### Production error reporting
rollbar.com

#### GIT Issues
https://github.com/SkyzeTrading/Skyze/issues

### Work Management
#### Trello
https://trello.com/skyze2

### Team Communications
#### Slack
https://skyze.slack.com

## Deployment Management
### Deployment Process

### Deployment Tools

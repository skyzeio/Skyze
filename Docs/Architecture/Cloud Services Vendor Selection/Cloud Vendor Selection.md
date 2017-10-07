# <span style="color:DarkOrange">Cloud Vendor Selection</span>

<span style="color:limegreen">Version 1
Date: 4 October 2017 </span>

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [<span style="color:DarkOrange">Cloud Vendor Selection</span>](#span-stylecolordarkorangecloud-vendor-selectionspan)
	- [Contacts](#contacts)
	- [<span style="color:Fuchsia">Services</span>](#span-stylecolorfuchsiaservicesspan)
	- [First year Free](#first-year-free)
		- [Amazon](#amazon)
		- [Google](#google)
		- [Microsoft](#microsoft)
		- [Mongo Atlas - for ever](#mongo-atlas-for-ever)
	- [Compute](#compute)
		- [Pricing](#pricing)
	- [Storage](#storage)
	- [Amazon](#amazon)
		- [Reserved Instances](#reserved-instances)
	- [MongoDB Atlas](#mongodb-atlas)
		- [MongoDB Atlas: Hosted MongoDB on AWS](#mongodb-atlas-hosted-mongodb-on-aws)
		- [MongoDB Cloud Manager: Hosted Management Platform](#mongodb-cloud-manager-hosted-management-platform)
			- [Pricing](#pricing)

<!-- /TOC -->

## Contacts
Microsoft Auzre Australia	1-800-765-471
Google https://cloud.google.com/contact/
Amazon https://aws.amazon.com/contact-us/aws-sales/

## <span style="color:Fuchsia">Services</span>
|   | Amazon  | Google  | Azure  |
|---|---|---|---|
| Compute  | Amazon EC2  | Google Compute Engine  | Virtual Machine  |
| Pre-Config   | Y  | Y  | VMSets  |
| Serverless  | Lambda  | x  | x  |
| Storage   | S3  | Google Cloud Storage | Microsoft Azure Storage  |
| Docker Container Service  | x  | x  | x?  |
| Locations  | 42  | 33  | 32  |
| Database   |   |   |   |

## First year Free

### Amazon
12 MONTHS FREE		
EC2 .. T2.Micro 	750 hours / month
Quick Insight BI	1 GB
RDS	750 hours / month
S3	5 GB
Lambda	1 million /month

### Google
Access to all Cloud Platform Products
Get everything that you need to build and run your apps, websites and services, including Firebase and the Google Maps API.
$300 credit for free
Sign up and get $300 to spend on Google Cloud Platform over the next 12 months.
No autocharge after free trial ends
We ask you for your credit card details to make sure that you are not a robot. You won’t be charged unless you manually upgrade to a paid account.

### Microsoft
Get started with a $260 credit
Start free with $260 in credit to use on any Azure products for 30 days.

Keep going with free products
Build your next great idea with free access to our most popular products for 12 months and to more than 25 always free products.

Pay nothing until you choose
We use your credit card information for identity verification, but you will not be charged until you choose to upgrade.

### Mongo Atlas - for ever
Free

Learn, prototype, and start building immediately with your hosted MongoDB sandbox.


512 MB of storage / Shared RAM

Highly available replica set
End to end encryption
Secure authentication
Fully managed upgrades
Monitoring and alerts
Management API
Start free



## Compute
### Pricing
GCP pricing page: https://cloud.google.com/pricing/
Microsoft Azure pricing page: https://azure.microsoft.com/en-us/pricing/
AWS pricing page: https://aws.amazon.com/ec2/pricing/

## Storage
Amazon best and most expensive

## Amazon
### Reserved Instances
Reserved Instances provide you with a significant discount (up to 75%) compared to On-Demand instance pricing. In addition, when Reserved Instances are assigned to a specific Availability Zone, they provide a capacity reservation, giving you additional confidence in your ability to launch instances when you need them.

For applications that have steady state or predictable usage, Reserved Instances can provide significant savings compared to using On-Demand instances. See How to Purchase Reserved Instances for more information.

Reserved Instances are recommended for:
Applications with steady state usage
Applications that may require reserved capacity
Customers that can commit to using EC2 over a 1 or 3 year term to reduce their total computing costs

t2.nano

STANDARD 1-YEAR TERM
Payment Option	Upfront	Monthly*	Effective Hourly**	Savings over On-Demand	On-Demand Hourly
No Upfront	$0	$3.58	$0.005	33%	$0.0073 per Hour
Partial Upfront	$20	$1.68	$0.005	37%
All Upfront	$40	$0	$0.005	37%

## MongoDB Atlas
Available on AWS, GCP and Azure
https://www.mongodb.com/cloud/atlas

### MongoDB Atlas: Hosted MongoDB on AWS

With MongoDB Atlas, it's easier than ever to get started with the fastest growing NoSQL technology on Amazon Web Services. MongoDB Atlas is a hosted database as a service from the creators of MongoDB and is offered on-demand; pay only for what you use for dev & testing or easily scale precisely for your production applications.

### MongoDB Cloud Manager: Hosted Management Platform

MongoDB Cloud Manager is a hosted database management platform for monitoring, automation, and backup & failure recovery. With Cloud Manager, you can configure and provision your database servers as well as the underlying instances on Amazon Web Services directly through the platform UI.

#### Pricing

Cheapest is $80/month on Google with 1.75 GM RAM and 10GB storage

Azure ... $288/mth 3.75 GB RAM and 128GB Disk ....


**For example**, if you deploy on AWS a 3-node replica set of M40s and run it 24/7 for one month using the included 80GB of standard block storage, and you have exactly 80GB, your costs would be:

Per server hourly cost1: ~$0.34
Total servers: 3

Total hours: 720

Backup data: 80GB @ $2.50/GB/month

Total monthly fees paid to MongoDB: $946.79

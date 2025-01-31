# Real-time-news-search


brew install pipx

pipx install poetry

brew install pyenv

pyenv install 3.9.18

python3.9 --version

Python 3.9.21

python3.9 -m venv env
source env/bin/activate

poetry env use python3.9

poetry install

poetry env info


[confluent.cloud](https://confluent.cloud/)

For learning and exploring Kafka and Confluent Cloud.
Ingress	up to 250 MB/s
Egress	up to 750 MB/s
Storage	up to 5,000 GB
Client connections	up to 1,000
Partitions	up to 4,096 (includes 10 free partitions)
Uptime SLA	up to 99.5%


Base cost	$0 /hr
Write	$0.1265 /GB
Read	$0.1265 /GB
Storage	$0.00012603 /GB-hour
Partitions	$0.0046 /Partition-hour (includes 10 free partitions)



brew install kcat

kcat -b pkc-n3603.us-central1.gcp.confluent.cloud:9092 -X security.protocol=SASL_SSL -X sasl.mechanisms=PLAIN -X sasl.username="" -X sasl.password="" -L

%6|1738321072.611|GETSUBSCRIPTIONS|rdkafka#producer-1| [thrd:main]: Telemetry client instance id changed from AAAAAAAAAAAAAAAAAAAAAA to nAvUYESwSEihvQFE037FBg
Metadata for all topics (from broker -1: sasl_ssl://pkc-n3603.us-central1.gcp.confluent.cloud:9092/bootstrap):
 6 brokers:
  broker 0 at b0-pkc-n3603.us-central1.gcp.confluent.cloud:9092
  broker 1 at b1-pkc-n3603.us-central1.gcp.confluent.cloud:9092
  broker 2 at b2-pkc-n3603.us-central1.gcp.confluent.cloud:9092
  broker 3 at b3-pkc-n3603.us-central1.gcp.confluent.cloud:9092
  broker 4 at b4-pkc-n3603.us-central1.gcp.confluent.cloud:9092
  broker 5 at b5-pkc-n3603.us-central1.gcp.confluent.cloud:9092 (controller)
 1 topics:
  topic "topic_0" with 6 partitions:
    partition 0, leader 2, replicas: 2,3,1, isrs: 2,3,1
    partition 1, leader 3, replicas: 3,1,5, isrs: 3,1,5
    partition 2, leader 1, replicas: 1,5,0, isrs: 1,5,0
    partition 3, leader 5, replicas: 5,0,4, isrs: 5,0,4
    partition 4, leader 0, replicas: 0,4,2, isrs: 0,4,2
    partition 5, leader 4, replicas: 4,2,3, isrs: 4,2,3
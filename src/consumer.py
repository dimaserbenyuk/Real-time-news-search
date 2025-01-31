import json
from typing import List

from bytewax.connectors.kafka import KafkaSinkMessage, KafkaSource

from logger import get_logger
from models import CommonDocument
from settings import settings

logger = get_logger(__name__)


def build_kafka_stream_client():
    """
    Build a Kafka stream client to read messages from the Upstash Kafka topic using the ByteWax KafkaSource connector.
    """
    kafka_config = {
        "bootstrap.servers": settings.UPSTASH_KAFKA_ENDPOINT,
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": settings.UPSTASH_KAFKA_UNAME,
        "sasl.password": settings.UPSTASH_KAFKA_PASS,
        "auto.offset.reset": "earliest",  # Start reading at the earliest message
    }
    kafka_input = KafkaSource(
        topics=[settings.UPSTASH_KAFKA_TOPIC],
        brokers=[settings.UPSTASH_KAFKA_ENDPOINT],
        add_config=kafka_config,
    )
    logger.info("KafkaSource client created successfully.")
    return kafka_input


def process_message(message: KafkaSinkMessage):
    """
    On a Kafka message, process the message and return a list of CommonDocuments.
    - message: KafkaSinkMessage(key, value) where value is the message payload.
    """
    documents: List[CommonDocument] = []
    try:
        json_str = message.value.decode("utf-8")
        data = json.loads(json_str)
        documents = [CommonDocument.from_json(obj) for obj in data]
        logger.info(f"Decoded into {len(documents)} CommonDocuments")
        return documents
    except StopIteration:
        logger.info("No more documents to fetch from the client.")
    except KeyError as e:
        logger.error(f"Key error in processing document batch: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from message: {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error in next_batch: {e}")

# import json
# import pandas as pd
# import bytewax.operators as op
# from bytewax.dataflow import Dataflow
# from bytewax.connectors.kafka import KafkaSource
# from bytewax.outputs import DynamicSink, StatelessSinkPartition
# from settings import settings
# from logger import get_logger

# logger = get_logger(__name__)

# def build_kafka_stream_client():
#     kafka_config = {
#         "bootstrap.servers": settings.UPSTASH_KAFKA_ENDPOINT,
#         "security.protocol": "SASL_SSL",
#         "sasl.mechanisms": "PLAIN",
#         "sasl.username": settings.UPSTASH_KAFKA_UNAME,
#         "sasl.password": settings.UPSTASH_KAFKA_PASS,
#         "auto.offset.reset": "earliest",
#     }
#     return KafkaSource(
#         topics=[settings.UPSTASH_KAFKA_TOPIC],
#         brokers=[settings.UPSTASH_KAFKA_ENDPOINT],
#         add_config=kafka_config,
#     )

# def process_news_data(news_message):
#     try:
#         news_json = news_message.value  # Получаем JSON строку

#         # Проверяем, что данные не пустые
#         if not news_json or news_json.strip() == "":
#             logger.error("Получено пустое сообщение из Kafka")
#             return None

#         news_data = json.loads(news_json)  # Парсим JSON

#         # Если данные - это список, берем первый элемент (или итерируем по ним)
#         if isinstance(news_data, list):
#             news_data = news_data[0] if news_data else {}

#         if not isinstance(news_data, dict):
#             logger.error(f"Ожидался JSON-объект, но получено: {type(news_data)}")
#             return None

#         return {
#             "article_id": news_data.get("article_id"),
#             "title": news_data.get("title"),
#             "description": news_data.get("description"),
#             "content": news_data.get("content"),
#             "published_at": news_data.get("published_at"),
#             "source_name": news_data.get("source_name"),
#             "author": news_data.get("author"),
#             "url": news_data.get("url"),
#             "image_url": news_data.get("image_url"),
#         }
#     except json.JSONDecodeError as e:
#         logger.error(f"Ошибка декодирования JSON: {e} - входные данные: {news_json}")
#         return None


# class CsvSinkPartition(StatelessSinkPartition):
#     """Записывает данные в CSV-файл в одном потоке."""

#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.data = []

#     def write_batch(self, items):
#         """Метод, который требует реализация от StatelessSinkPartition."""
#         self.data.extend(items)

#     def close(self):
#         if self.data:
#             df = pd.DataFrame(self.data)
#             df.to_csv(self.file_path, index=False, encoding="utf-8")
#             logger.info(f"Данные сохранены в {self.file_path}")

# class CsvSink(DynamicSink):
#     """Оборачивает CsvSinkPartition для Bytewax."""

#     def __init__(self, file_path="news_data.csv"):
#         self.file_path = file_path

#     def build(self, worker_index, worker_count, _resume_state):
#         return CsvSinkPartition(self.file_path)

# flow = Dataflow("news-to-csv")

# stream = op.input("kafka_input", flow, build_kafka_stream_client())
# processed_stream = op.map("process_news", stream, process_news_data)
# op.output("csv_output", processed_stream, CsvSink("news_data.csv"))







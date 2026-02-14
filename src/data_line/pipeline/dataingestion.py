from src.data_line.config.configuration import ConfigurationManager
from src.data_line.components.data_ingestion import DataIngestion

from src.data_line import logger

STATE_NAME = "data_ingestion"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_pipeline(self):
        logger.info(f"{'>>'*20} Stage {STATE_NAME} started. {'<<'*20}")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        logger.info(f"{'>>'*20} Stage {STATE_NAME} completed. {'<<'*20}")


if __name__ == "__main__":
    try:
        obj = DataIngestionPipeline()
        obj.initiate_data_pipeline()
    except Exception as e:
        logger.exception(e)
        raise e    
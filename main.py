from src.data_line import logger

logger.info("Starting the main application...")

from src.data_line.pipeline.dataingestion import DataIngestionPipeline


STATE_NAME = "data_ingestion"

try:
    logger.info(f"{'>>'*20} Stage {STATE_NAME} started. {'<<'*20}")
    obj = DataIngestionPipeline()
    obj.initiate_data_pipeline()
    logger.info(f"{'>>'*20} Stage {STATE_NAME} completed. {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e      



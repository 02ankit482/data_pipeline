from src.data_line import logger

logger.info("Starting the main application...")

from src.data_line.pipeline.dataingestion import DataIngestionPipeline
from src.data_line.pipeline.datavalidation import DataValidationPipeline

STATE_NAME = "data_ingestion"

try:
    logger.info(f"{'>>'*20} Stage {STATE_NAME} started. {'<<'*20}")
    ingestion_pipeline = DataIngestionPipeline()
    ingestion_pipeline.initiate_data_pipeline()
    logger.info(f"{'>>'*20} Stage {STATE_NAME} completed. {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e    
STATE_NAME = "data_validation"
try:
    logger.info(f"{'>>'*20} Stage {STATE_NAME} started. {'<<'*20}")
    validation_pipeline = DataValidationPipeline()
    validation_pipeline.initiate_data_validation()
    logger.info(f"{'>>'*20} Stage {STATE_NAME} completed. {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e      



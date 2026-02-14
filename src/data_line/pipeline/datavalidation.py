from src.data_line.config.configuration import ConfigurationManager
from src.data_line.components.data_validation import DataValidation
from src.data_line import logger

STATE_NAME = "data_validation"

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        logger.info(f"{'>>'*20} Stage {STATE_NAME} started. {'<<'*20}")
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        logger.info(f"{'>>'*20} Stage {STATE_NAME} completed. {'<<'*20}")


if __name__ == "__main__":
    try:
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
    except Exception as e:
        logger.exception(e)
        raise e        
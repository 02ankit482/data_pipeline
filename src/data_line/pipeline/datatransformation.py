from src.data_line.config.configuration import ConfigurationManager
from src.data_line.components.data_transformation import DataTransformation
from src.data_line import logger


STATE_NAME=" Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation_pipeline(self):
        logger.info(f"Starting {STATE_NAME}")
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split_save_data()
        logger.info(f"{'>>'*20} Stage {STATE_NAME} completed. {'<<'*20}")



    if __name__ == "__main__":
        try:
            obj=DataTransformationPipeline()
            obj.initiate_data_transformation_pipeline()
        except Exception as e:
            logger.exception(e)
            raise e
       
from src.data_line.constants import *
from src.data_line.utils.common import read_yaml, create_directories
from src.data_line.entity.config_entity import (DataIngestionConfig, DataValidationConfig)
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion   # extracts the data_ingestion section from the config.yaml file
        create_directories([config.root_dir])  # creates the root_dir directory if it doesn't exist
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.columns

        create_directories([
            config.root_dir,
            Path(config.report_file).parent
        ])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            data_dir=Path(config.data_dir),
            report_file=config.report_file,
            all_schema=schema
        )

        return data_validation_config 

import os
import pandas as pd
from src.data_line import logger
from src.data_line.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    def validate_all_columns(self)->bool:
        try:
            validation_status=None
            data = pd.read_csv(self.config.data_dir)    
            for column in data.columns:
                if column not in self.config.all_schema.keys():
                    validation_status=False
                    with open(self.config.report_file, "w") as f:
                        f.write(f"Column {column} is not in the schema. hence validation Status is {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.report_file, "w") as f:
                        f.write(f"Column {column} is in the schema. hence validation Status is {validation_status}")
            return validation_status
        except Exception as e:
            logger.exception(e)                         
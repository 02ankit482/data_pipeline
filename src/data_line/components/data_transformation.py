import os
import pandas as pd
from src.data_line import logger
from sklearn.model_selection import train_test_split
from src.data_line.entity.config_entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_split_save_data(self):
        try:
            data = pd.read_csv(self.config.data_dir)

            # 🔹 Apply transformations BEFORE split
            data = self.apply_transformations(data)

            train, test = train_test_split(
                data, test_size=0.2, random_state=42
            )

            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Data transformation completed successfully.")

        except Exception as e:
            logger.error(f"Error during data transformation: {e}")
            raise e


    def apply_transformations(self, data):
        # Impute Age
        data['Age'] = data['Age'].fillna(data['Age'].mean())

        # Impute Embarked
        data['Embarked'] = data['Embarked'].fillna('S')

        # Convert types
        data['Survived'] = data['Survived'].astype('category')
        data['Pclass'] = data['Pclass'].astype('category')
        data['Sex'] = data['Sex'].astype('category')
        data['Embarked'] = data['Embarked'].astype('category')

        return data

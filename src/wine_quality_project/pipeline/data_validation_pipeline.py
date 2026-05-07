from src.wine_quality_project.config.configration import ConfigrationManager
from src.wine_quality_project import logger
from src.wine_quality_project.components.data_validation import DataValidation

STAGE_NAME= "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigrationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===============x")
    except Exception as e:
        raise e
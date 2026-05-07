
from src.wine_quality_project.config.configration import ConfigrationManager
from src.wine_quality_project.components.data_transformation import DataTransformation
from src.wine_quality_project import logger
from pathlib import Path
STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
                print(status)

                if status == "True":
                    config = ConfigrationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    ata_transformation = DataTransformation(config=data_transformation_config)
                    ata_transformation.train_test_splitting()
                else:
                    raise Exception("Data Schema is not valid check data col and its types!")
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===============x")
    except Exception as e:
        raise e
from src.wine_quality_project.config.configration import ConfigrationManager
from src.wine_quality_project import logger
from src.wine_quality_project.components.model_evaluation import ModelEvaluation

STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigrationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation()
        logger.info(">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===============x")
    except Exception as e:
        raise e
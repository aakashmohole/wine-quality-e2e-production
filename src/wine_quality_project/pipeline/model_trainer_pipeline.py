
from src.wine_quality_project.config.configration import ConfigrationManager
from src.wine_quality_project.components.model_trainer import ModelTrainer
from src.wine_quality_project import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigrationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
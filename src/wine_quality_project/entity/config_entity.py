
from dataclasses import dataclass
from pathlib import Path
from src.wine_quality_project.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path
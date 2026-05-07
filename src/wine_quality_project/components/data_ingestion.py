import os
import urllib.request as request
from src.wine_quality_project import logger
import zipfile
from src.wine_quality_project.entity.config_entity import (DataIngestionConfig)


# components - DataIngestion
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    #DOWNLOAD FILE
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers= request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} download! with following information : \n{headers}" )
        else:
            logger.info(f"file aready exits of size!")
    
    #EXTRACT FILE
    def extract_zip_file(self):
        """
        zip_file_path = str
        extract zip file into data dir
        Function return none
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

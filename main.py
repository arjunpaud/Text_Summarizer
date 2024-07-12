from Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.logging import logger 
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Text_Summarizer.pipeline.stage_04_model_training import ModelTrainingPipeline
from Text_Summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>> stage{STAGE_NAME} started<<<")
    # data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion=DataIngestionTrainingPipeline()
    # data_ingestion.main()
    data_ingestion.main()
    logger.info(f">>> stage{STAGE_NAME} completed <<<<\n\n====x")


except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>> stage{STAGE_NAME} started<<<")
    # data_ingestion=DataIngestionTrainingPipeline()
    data_validation=DataValidationTrainingPipeline()
    # data_ingestion.main()
    data_validation.main()
    logger.info(f">>> stage{STAGE_NAME} completed <<<<\n\n====x")


except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>> stage{STAGE_NAME} started<<<")
    # data_ingestion=DataIngestionTrainingPipeline()
    data_transformation=DataTransformationTrainingPipeline()
    # data_ingestion.main()
    data_transformation.main()
    logger.info(f">>> stage{STAGE_NAME} completed <<<<\n\n====x")


except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Training Stage"

try:
    logger.info(f">>>> stage{STAGE_NAME} started<<<")
    # data_ingestion=DataIngestionTrainingPipeline()
    model_trainer=ModelTrainingPipeline()
    # data_ingestion.main()
    model_trainer.main()
    logger.info(f">>> stage{STAGE_NAME} completed <<<<\n\n====x")


except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

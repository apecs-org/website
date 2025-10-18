from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def sample_task():
    """
    A simple task example
    """
    logger.info("Executing sample_task.")
    return "Sample task completed."


@shared_task
def test_beat_task():
    print("Celery Beat task executed!")
    return "Beat task completed."


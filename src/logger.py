import logging
import os


def setup_logger():

    os.makedirs("Logs", exist_ok=True)

    logging.basicConfig(
        filename="Logs/payroll.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a"
    )

    return logging
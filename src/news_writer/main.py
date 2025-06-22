#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from crew import NewsWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from dotenv import load_dotenv

load_dotenv()

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    inputs_array = [
        {
            'topic': 'AI LLMs',
            'date': datetime.now().strftime("%Y-%m-%d_%H-%M"),
            'to_email': os.getenv('RECIPIENT_EMAIL')
        },
        {
            'topic': 'Expected AI Weather Model Advances',
            'date': datetime.now().strftime("%Y-%m-%d_%H-%M"),
            'to_email': os.getenv('RECIPIENT_EMAIL')
        }
    ]
    try:
        NewsWriter().crew().kickoff_for_each(inputs=inputs_array)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
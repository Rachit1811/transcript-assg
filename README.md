# pepsales_assg
 This project is designed to analyze sales transcripts using NLP and LLMs to extract structured insights based on a lead qualification framework. The system evaluates Ideal Customer Profile (ICP) Fitment, Needs & Deal Completion Time, and Budget & Authority using a scoring mechanism.

To run the code first set up a virtual environment by running a "python -m venv venv" in terminal opened in this transcript assg folder, activate it using "venv\Scripts\Activate"
Install the dependencies in requirements.txt, by running the "pip install -r requirements.txt"
To do the data preprocessing use the data_preprocessing.py code, change the transcript.txt fetch to test path if needed this generates a processed transcript
Use the OpenRouter website to access some API, make an .env and write OPENROUTER_API_KEY = "Your_API_key"
Run the model in model.ipynb to get the desired output


# Introduction

This documentation provides information and usage instructions for the "YouTube Video Summarizer" application. The application utilizes the OpenAI API, YouTube Transcript API, gTTS (Google Text-to-Speech), and Streamlit to generate a concise summary of a given YouTube video's content.


#  Prerequisites

Before using the application, ensure that you have the following prerequisites installed:

-   Python 3.x
-   pip (Python package installer)
-   The required Python libraries specified in the `requirements.txt` file.

    Install the required libraries using the following command:
 `pip install -r requirements.txt
`


## Getting Started

1.  Obtain OpenAI API key:
    
    -   Visit [OpenAI](https://beta.openai.com/signup/) to sign up for an account.
    -   Retrieve your API key from the OpenAI dashboard.
2.  Set up environment variables:
    
    -   Create a `.env` file in the project directory.
    -   Add the OpenAI API key to the `.env` file:
        
       `OPENAI_API_KEY=<your_openai_api_key>` 
        
3.  Run the application:
      `streamlit run your_script_name.py`

## Usage

1.  Enter a YouTube Video URL in the provided text input and press Enter.
    
2.  View Full Transcript:
    
    -   The application fetches the video transcript using the YouTube Transcript API.
    -   The full transcript is displayed under the "Full Transcript" section.
3.  Generate Summary:
    
    -   The application utilizes the OpenAI API to generate a concise summary of the video content.
    -   The summary is displayed under the "Summary" section.
4.  Listen to Summary:
    
    -   The application converts the generated summary into an MP3 audio file using gTTS.
    -   An audio player is provided to listen to the summary.

```

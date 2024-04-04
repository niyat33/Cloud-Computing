# GenAI - Containerized video transcription and chat app
Prerequisites
- An OpenAI API Key.
- Pinecone API Key.
- Latest version of Docker Desktop.(Or Docker Engine if you are a Linux user and are planning to use GPU acceleration)
- A Git client.

1. Clone the sample application. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:
_git clone https://github.com/Davidnet/docker-genai.git_

2.  Build and Run the Application using the command: docker-compose up --build
This command builds the Docker images and starts the containers specified in the docker-compose.yaml file.

3. Specify your API keys. In the docker-genai directory, create a text file called .env and specify your API keys inside.
   The following is the contents of the .env.example file that you can refer to as an example.

    ----------------------------------------------------------------------------
    **#OpenAI
    **#----------------------------------------------------------------------------
    OPENAI_TOKEN=your-api-key # Replace your-api-key with your personal API key
    **#----------------------------------------------------------------------------
    **# Pinecone
    ----------------------------------------------------------------------------
    PINECONE_TOKEN=your-api-key # Replace your-api-key with your personal API key


5. Build and run the application. In a terminal, change directory to your docker-genai directory and run the following command.
$ docker compose up --build
   * This builds the docker images and starts the containers specified in the docker-compose.yaml file.
5. Using the yt-whisper Service:Open a browser and access the yt-whisper service at: http://localhost:8503
   
7. Once the application appears, in the Youtube URL field specify a Youtube video URL and select Submit.
   
9. The yt-whisper service downloads the audio of the video, uses Whisper to transcribe it into a WebVTT (*.vtt) format then uses the text-embedding-3-small model to create embeddings, and finally uploads those embeddings into the Pinecone database.
    
11. After processing the video, a video list will appear in the web app showing the videos that have been indexed in Pinecone. You can click the button to download the transcript.
    
13. Using the dockerbot Service: Access the dockerbot service on port 8504 and ask questions about the videos that were processed by the yt- whisper service. Open a browser and access the service at http://localhost:8504

14. Press ctrl+C in the terminal to stop the application.





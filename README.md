# Jarvis_My_VA

`Jarvis_My_VA` is a voice-activated personal assistant developed using Python. It performs a range of tasks such as opening web pages, fetching news, playing music, and responding with the current time. The assistant activates upon hearing the wake word `Jarvis` and provides a conversational experience for users.

## Features

**Voice-activated Commands:** Jarvis responds to voice commands and performs various tasks.

**Time-based Greetings:** Depending on the time of day, Jarvis greets the user accordingly.

**Time Retrieval:** Jarvis can tell the current time upon request.

**Web Navigation:** Open commonly used websites like Google, Facebook, YouTube, and LinkedIn.

**Play Music:** Jarvis can play songs based on the user's command.

**News Headlines:** Fetches the latest news headlines for the user.

## Setup

**Prerequisites**:

Ensure you have Python installed.

This project requires the following Python packages:

    speech_recognition for voice recognition
    pyttsx3 for text-to-speech
    requests for API calls (for news fetching)
    webbrowser for web navigation

You can install these packages using:

    pip install speechrecognition pyttsx3 requests

### Additional Configuration:

For `news headlines`, you need an API key from NewsAPI. Update newsapi in the code with your API key:

    newsapi = "Your_News_API_Key"
    
### Music Library Setup

Customize the `musicLibrary` with song titles and URLs.

**Example:**

    musicLibrary = {
        "song_name": "url_to_song",
        "another_song": "another_url"
    }

### Usage

Run the main Python script to activate Jarvis:

    python jarvis.py
    
Upon activation, say "Jarvis" to initiate a command sequence, followed by any of the supported commands.

### Commands List

**Basic Commands:**

    "Open Google" - Opens Google in the default web browser.
    "Open Facebook" - Opens Facebook in the default web browser.
    "Open YouTube" - Opens YouTube in the default web browser.
    "Open LinkedIn" - Opens LinkedIn in the default web browser.
    "Open Netflix" - Opens Netflix in the default web browser.
    "You can add some extra commands according to your wish"
    
**Time Command:**

    "What’s the time?" or "Tell me the time" - Jarvis announces the current time.
    
**Music**:

    "Play [song name]" - Jarvis plays the specified song if it exists in the musicLibrary.
    
**News:**

    "News" - Jarvis reads the latest news headlines using NewsAPI.
    
## Code Structure

**speak():** Text-to-speech function.

**wishMe():** Greets the user based on the time of day.

**tellTime():** Announces the current time.

**processCommand():** Processes commands and triggers the appropriate response.

## Error Handling

The program includes error handling for:

**Timeout and recognition errors**

**Unrecognized commands**

## License

This project is licensed under the MIT License.

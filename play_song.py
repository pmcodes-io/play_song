import urllib.parse
import webbrowser

try:
    song = input("Enter the song name: ")
    
    # Safely format the song name for a web search query
    query = urllib.parse.quote(song)
    url = f"https://www.youtube.com/results?search_query={query}"
    
    # Opens the YouTube search results directly in your browser
    webbrowser.open(url)
    print("Opening YouTube search results in your browser.")
    
except Exception as e:
    print(f"An error occurred: {e}")
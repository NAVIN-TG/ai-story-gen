import urllib.parse

def create_download_link(text: str, filename: str = "generated_story.txt") -> str:
    encoded = urllib.parse.quote(text)
    return f"data:text/plain;charset=utf-8,{encoded}"

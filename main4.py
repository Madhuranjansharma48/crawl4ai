from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h2>Enter Website URL to fetch sitemap.xml</h2>
            <form action="/get-sitemap" method="post">
                <input type="text" name="url" placeholder="Enter website URL" style="width:400px;">
                <button type="submit">Get Sitemap</button>
            </form>
        </body>
    </html>
    """

@app.post("/get-sitemap", response_class=HTMLResponse)
def get_sitemap(url: str = Form(...)):
    # Ensure proper formatting
    if not url.startswith("http"):
        url = "https://" + url
    
    # Add sitemap.xml
    if not url.endswith("/"):
        url += "/"
    sitemap_url = url + "sitemap.xml"

    try:
        response = requests.get(sitemap_url, timeout=10)
        if response.status_code == 200:
            return f"""
            <h3>Sitemap Found:</h3>
            <p><a href='{sitemap_url}' target='_blank'>{sitemap_url}</a></p>
            <pre>{response.text[:2000]}...</pre>
            """
        else:
            return f"<h3>No sitemap.xml found at {sitemap_url}</h3> (Status: {response.status_code})"
    except Exception as e:
        return f"<h3>Error:</h3> {str(e)}"

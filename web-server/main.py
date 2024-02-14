import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4,5]


@app.get("/contact")
def get_contact():
    return {
        "name": "<NAME>",
        "email": "<EMAIL>",
        "phone": "<PHONE>",
        "city": "<CITY>",
    }

@app.get("/form", response_class=HTMLResponse)
def get_form():
    return """
        <html>
            <head>
                <title>Contact</title>
            </head>
            <body>
                <h1>Contact</h1>
                <p>Name: <NAME></p>
                <p>Email: <EMAIL></p>
                <p>Phone: <PHONE></p>
                <p>City: <CITY></p>
            </body>
        </html>
        """



def run():
    store.get_categories();

if __name__ == '__main__':
    run()
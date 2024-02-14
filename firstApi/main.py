from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(name):
    try:
        return {
            "status": 200,
            "message": "first Api",
            "object": {
                "name": name,
                "age": "<AGE>",
            }
        }
    except Exception as error:
        return {
            "status": 500,
            "message": "Internal Server Error",
            "error": str(error)
        }
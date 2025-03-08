from fastapi import FastAPI

app = FastAPI()

@app.get('/Hello-world')
def read_root():

    data = {
        "message": "hello world",
        "details": {
            "author": {
                "name": "Ant1b1ot1k",
                "email": "random_email@gmail.com"
            },
            "tags": ["fastapi", "python", "web"]
        }
    }
    return data

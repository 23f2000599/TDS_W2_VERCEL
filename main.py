from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock student marks database
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}

@app.get("/api")
def get_marks(name: list[str]):
    marks = [student_marks.get(n, "Not Found") for n in name]
    return {"marks": marks}

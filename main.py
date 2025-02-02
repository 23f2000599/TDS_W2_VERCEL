from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the student data
student_data = [
    {"name": "tMBTx3Nd", "marks": 97},
    {"name": "WOXpY9M9K", "marks": 79},
    {"name": "UYRuhfT0BG", "marks": 54},
    {"name": "leMYVzUO", "marks": 18},
    {"name": "P0gB", "marks": 27},
    {"name": "kp2MCNz5oa", "marks": 67},
    {"name": "ip", "marks": 13},
    {"name": "m", "marks": 72},
    {"name": "xk70", "marks": 40},
    {"name": "kEv2MdAt", "marks": 37},
    {"name": "c8yGBPVT", "marks": 10},
    {"name": "kMwPtqKwYK", "marks": 68},
    {"name": "2MeDKBze", "marks": 38},
    {"name": "omb0YtMbe", "marks": 10},
    {"name": "jaxgpo", "marks": 80},
    {"name": "EA86E", "marks": 43},
    {"name": "wNWcK0gM", "marks": 44},
    {"name": "ynYKRc4x8", "marks": 64},
    {"name": "zjxHQwcIz", "marks": 8},
    {"name": "GwGE", "marks": 29},
    {"name": "9Yq24go", "marks": 61},
    {"name": "3", "marks": 80},
    {"name": "iNczv", "marks": 85},
    {"name": "GArC", "marks": 33},
    {"name": "0qvAVknR0T", "marks": 14},
    {"name": "d", "marks": 53},
    {"name": "9iml36ceh", "marks": 38},
    {"name": "p5dAWnyD", "marks": 77},
    {"name": "m8yPRNsu", "marks": 23},
    {"name": "6RBxLz", "marks": 35},
    {"name": "qAZ48fM", "marks": 81},
    {"name": "ijK", "marks": 54},
    {"name": "2P8", "marks": 68},
    {"name": "7KVBLnfyK4", "marks": 14},
    {"name": "s", "marks": 1},
    {"name": "Ok8", "marks": 69},
    {"name": "9XgeLHU", "marks": 45},
    {"name": "e88RR4X", "marks": 37},
    {"name": "X0xP", "marks": 38},
    {"name": "voJ4W", "marks": 24},
    {"name": "nTBIgEz", "marks": 19},
    {"name": "foZQD", "marks": 65},
    {"name": "o", "marks": 97},
    {"name": "OHEZ", "marks": 66},
    {"name": "LgFzs3V", "marks": 10},
    {"name": "L6VAuAY24x", "marks": 64},
    {"name": "hnNB", "marks": 48},
    {"name": "M9X7nQPyYn", "marks": 26},
    {"name": "iY8pbHLvW", "marks": 62},
    {"name": "fBzRBw", "marks": 14},
    {"name": "oG", "marks": 76},
    {"name": "n637", "marks": 32},
    {"name": "J3bG5SRY", "marks": 83},
    {"name": "FJq", "marks": 90},
    {"name": "7RuyRy", "marks": 44},
    {"name": "cVYeBK", "marks": 49},
    {"name": "vDvZ2pvJ", "marks": 47},
    {"name": "oupuZ", "marks": 96},
    {"name": "3uHvL5", "marks": 45},
    {"name": "EmR", "marks": 35},
    {"name": "UQHCa7t", "marks": 7},
    {"name": "MaOhl59F", "marks": 35},
    {"name": "a9", "marks": 39},
    {"name": "6qkT", "marks": 14},
    {"name": "XakWPlf", "marks": 88},
    {"name": "v43eLfq", "marks": 65},
    {"name": "GRfT", "marks": 97},
    {"name": "EfXgsSBnHo", "marks": 53},
    {"name": "K6", "marks": 21},
    {"name": "3m", "marks": 53},
    {"name": "MkZhtpy2", "marks": 15},
    {"name": "nZ1", "marks": 22},
    {"name": "XD5q8p", "marks": 64},
    {"name": "u6uxxcP", "marks": 31},
    {"name": "Z9", "marks": 88},
    {"name": "pZAcZ", "marks": 67},
    {"name": "8a2o9LD7A", "marks": 6},
    {"name": "FvuYD0", "marks": 62},
    {"name": "cBrXh9I1k", "marks": 76},
    {"name": "iqwYuA", "marks": 7},
    {"name": "BZsDS2", "marks": 31},
    {"name": "5m", "marks": 86},
    {"name": "3bB0x", "marks": 54},
    {"name": "8TQmRsA", "marks": 61},
    {"name": "bc6M", "marks": 25},
    {"name": "6ETJjqJ", "marks": 24},
    {"name": "1jYQfU", "marks": 24},
    {"name": "DwQToThh", "marks": 86},
    {"name": "FLmO", "marks": 63},
    {"name": "N", "marks": 32},
    {"name": "KQKL9K9", "marks": 28},
    {"name": "3V837", "marks": 96},
    {"name": "UhP", "marks": 92},
    {"name": "7tXs8dJE", "marks": 53},
    {"name": "AWXt", "marks": 2},
    {"name": "iuW1", "marks": 32},
    {"name": "DvwF", "marks": 90},
    {"name": "2Qx09Z9Td", "marks": 82},
    {"name": "mppV1", "marks": 85},
    {"name": "IQE", "marks": 97},
]

# Convert JSON to dictionary for quick lookup
student_marks = {s["name"]: s["marks"] for s in student_data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    """
    Accepts multiple names as query parameters and returns their marks.
    
    Example Request:
    /api?name=Alice&name=Bob
    
    Example Response:
    { "marks": [85, 90] }
    """
    marks = [student_marks.get(n, {"error": f"{n} not found"}) for n in name]
    return {"marks": marks}

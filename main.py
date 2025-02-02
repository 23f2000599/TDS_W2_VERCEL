from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

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
    # Add more students here...
]

# Convert to dictionary for quick lookup
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
    # Fetch marks for the requested names, return "Not Found" if name is not in data
    marks = [student_marks.get(n, {"error": f"{n} not found"}) for n in name]
    return {"marks": marks}

# HDiscover
User Discovery &amp; Ranking System


MiniProject

Author: Harshith Chegondi

Duration: 17-Dec'2025 to 26-Dec'2025

Programming Language: Python


## Overview
HDiscover is a prototype system that fetches user data from [randomuser.me](https://randomuser.me), 
calculates distances between users, and ranks them using a custom Merge Sort algorithm. 
The system demonstrates API integration, algorithm design, and user ranking logic.

## Current Features
- Fetch random user data via API
- Fetch multiple users
- Calculate Euclidean distances
- Sort users by distance using Merge Sort
- Display nearest 100 opposite-gender users

## Requirements

- Python 3.9 or higher (Download from [python.org](https://www.python.org/downloads/))
- pip (Python package manager, included with Python)

### Install dependencies
Clone the repository and install required packages:

```bash
git clone https://github.com/MistyEyed/HDiscover.git
cd HDiscover
pip install -r requirements.txt
```

## Usage
Clone the repo and run:
```bash
python HDiscover_SourceCode.py
```

## Roadmap
- [x] Fetch random user from API
- [x] Fetch multiple users
- [x] Calculate Euclidean distances
- [x] Sort users with Merge Sort
- [x] Integrate database (SQLite3)
- [x] Add Streamlit frontend
- [x] Update distance calculation (Haversine)

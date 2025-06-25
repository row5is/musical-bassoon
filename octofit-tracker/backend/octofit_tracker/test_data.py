# Test data for OctoFit Tracker

TEST_USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "age": 25, "team": "Team A"},
    {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30, "team": "Team B"},
    {"email": "alice.jones@example.com", "name": "Alice Jones", "age": 22, "team": "Team A"},
]

TEST_TEAMS = [
    {"name": "Team A", "description": "A team focused on endurance training."},
    {"name": "Team B", "description": "A team focused on strength training."},
]

TEST_ACTIVITIES = [
    {"name": "Running", "description": "Endurance activity."},
    {"name": "Weightlifting", "description": "Strength activity."},
]

TEST_LEADERBOARD = [
    {"user": "john.doe@example.com", "score": 150},
    {"user": "jane.smith@example.com", "score": 200},
    {"user": "alice.jones@example.com", "score": 180},
]

TEST_WORKOUTS = [
    {"user": "john.doe@example.com", "activity": "Running", "duration": 30},
    {"user": "jane.smith@example.com", "activity": "Weightlifting", "duration": 45},
    {"user": "alice.jones@example.com", "activity": "Running", "duration": 25},
]

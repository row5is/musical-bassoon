from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": [users[0], users[1]]},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": users[0], "type": "Running", "duration": 60},
            {"user": users[1], "type": "Cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"team": teams[0], "points": 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Yoga", "description": "A relaxing yoga session to start the day."},
            {"name": "HIIT Training", "description": "High-intensity interval training for advanced fitness."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data'))

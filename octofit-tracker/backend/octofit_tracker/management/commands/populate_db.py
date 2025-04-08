from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users'

    def handle(self, *args, **kwargs):
        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
        ]
        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS('Users created successfully.'))

        # Create a team
        team = Team(_id=ObjectId(), name='Blue Team')
        team.save()

        self.stdout.write(self.style.SUCCESS('Team created successfully.'))

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
        ]
        Activity.objects.bulk_create(activities)

        self.stdout.write(self.style.SUCCESS('Activities created successfully.'))

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        self.stdout.write(self.style.SUCCESS('Leaderboard entries created successfully.'))

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Workouts created successfully.'))

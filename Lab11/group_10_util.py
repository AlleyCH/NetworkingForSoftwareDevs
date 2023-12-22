#Lab 11
import time
import random
import json

start_id = 111


def create_data():
    data = {
        'id': start_id,
        'player': 'Player1',
        'timestamp': time.asctime(),
        'score': random.randint(0, 10000),
        'level': random.randint(1, 10),
        'achievements': {
            'high_score': random.choice([True, False]),
            'completed_mission': random.choice([True, False]),
            'new_level_unlocked': random.choice([True, False])
        },
        'power-ups': {
            'speed_boost': random.randint(0, 5),
            'health_boost': random.randint(0, 3),
            'shield': random.choice([True, False])
        },
        'game_duration': random.uniform(10.0, 300.0),  # in seconds
        'game_mode': random.choice(['Single Player', 'Multiplayer'])
    }

def print_data(data):  
      print(json.dumps(data, indent=2))

import random
# import time
from datetime import datetime, timedelta

# Sample lists for synthetic data
users = [f"user_{i}" for i in range(1, 1000)]
devices = ["Smartphone", "Smart TV", "Desktop", "Tablet", "Browser", "Gaming Console", "Set-Top Box"]
operating_systems = ["iOS", "Android", "Windows", "macOS", "Linux", "Fire OS", "Tizen", "Roku OS"]
browsers = ["Chrome", "Safari", "Firefox", "Edge", "Opera", "Brave", "IE"]
genres = ["Action", "Drama", "Comedy", "Horror", "Romance", "Thriller", "Documentary", "Sci-Fi", "Fantasy", "Mystery"]
subscription_tiers = ["Free", "Basic", "Premium", "VIP", "Family", "Student", "Business", "Enterprise", "Lifetime"]
content_ratings = ["PG-13", "TV-MA", "R", "G", "TV-14", "TV-PG", "TV-Y7", "TV-G", "NC-17", "TV-Y", "NR", "Unrated"]
languages = ["English", "Spanish", "Hindi", "French", "German", "Japanese", "Chinese", "Arabic", "Russian", "Portuguese"]
content_types = ["movie", "series", "live stream", "documentary", "short film", "web series", "music video", "podcast"]

# Function to generate a random timestamp
def generate_timestamp():
    return (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()

# Generate User Behavior Data
def generate_user_behavior_data():
    user_id = random.choice(users)
    session_id = f"session_{random.randint(10000, 99999)}"
    device_id = f"device_{random.randint(1000, 9999)}"
    content_id = random.randint(1000, 9999)
    event_type = random.choice(["Search", "Click", "Play", "Pause", "Like", "Share", "Add to Favorites", "Exit", "Buffering"])
    completion_status = random.choice(["watched completely", "abandoned", "paused", "buffered", "skipped"])
    time_spent = random.randint(1, 180)  # Time spent in minutes

    return {
        "User ID": user_id,
        "Session ID": session_id,
        "Device ID": device_id,
        "Action Type": event_type,
        "Timestamp": generate_timestamp(),
        "Content ID": content_id,
        "Interaction Source": random.choice(["homepage", "search page", "recommendation carousel", "trending list", "watchlist", "history", "genre page", "actor/director page"]),
        "Completion Status": completion_status,
        "Time Spent Watching": time_spent,
        "Scroll or Browse Pattern": random.randint(1, 10),  # Pages visited
        "Search Query": random.choice(["Action", "Drama", "Comedy", "Horror", "Romance", "Thriller", "Documentary", "Sci-Fi", "Fantasy", "Mystery"]),
        "Search Type": random.choice(["manual", "voice search", "auto-suggest", "popular search", "trending search"]),
        "Search Category": random.choice(["movie", "series", "live stream", "documentary", "short film", "web series", "music video", "podcast"]),
        "Playback Time": random.randint(0, 120),
        "Quality Selected": random.choice(["720p", "1080p","4K", "SD", "HD", "HDR"]),
        "Buffering Events": random.randint(0, 5),
        "Device Type": random.choice(devices),
        "Exit Reason": random.choice(["manual stop", "network failure", "app close", "device shutdown", "battery low", "call received", "notification"]),
    }

# Generate Content Metadata
def generate_content_metadata():
    content_id = random.randint(1000, 9999)
    return {
        "Content ID": content_id,
        "Title": f"Content_{content_id}",
        "Genre(s)": random.sample(genres, 2),
        "Sub-Genre(s)": random.choice(["Thriller", "Romantic-Comedy", "Action-Comedy", "Psychological", "Historical", "Biographical", "Adventure", "Crime", "Mystery", "Sci-Fi", "Fantasy"]),
        "Language": random.choice(languages),
        "Content Type": random.choice(content_types),
        "Popularity Metrics": {
            "Global Popularity Score": round(random.uniform(1.0, 10.0), 2),
            "Trending Status": random.choice([True, False]),
            "Watch Count": random.randint(100, 10000),
        },
        "Video Features": {
            "Duration (minutes)": random.randint(30, 180),
            "Content Rating": random.choice(content_ratings),
            "Release Date": generate_timestamp(),
            "Production Studio": f"Studio_{random.randint(1, 20)}",
        },
        "Series-Specific Details": {
            "Season and Episode Numbers": f"S{random.randint(1, 5)}E{random.randint(1, 20)}",
            "Series Runtime (minutes)": random.randint(300, 1500),
        },
        "User-Enriched Features": {
            "User Ratings": round(random.uniform(1.0, 5.0), 2),
            "Likes/Dislikes Count": {
                "Likes": random.randint(100, 1000),
                "Dislikes": random.randint(0, 100),
            },
            "Tags": random.sample(["must-watch", "classic", "blockbuster", "cult"], 2),
        },
    }

# Generate Platform Usage Data
def generate_platform_usage_data():
    session_start = datetime.now() - timedelta(minutes=random.randint(5, 180))
    session_duration = random.randint(5, 180)  # in minutes
    session_end = session_start + timedelta(minutes=session_duration)

    return {
        "Session Data": {
            "Session Start Time": session_start.isoformat(),
            "Session Duration (minutes)": session_duration,
            "Session End Time": session_end.isoformat(),
            "Time of Day": random.choice(["morning", "afternoon", "evening", "night"]),
        },
        "Device Information": {
            "Device Type": random.choice(devices),
            "Operating System": random.choice(operating_systems),
            "Browser/App Version": random.choice(browsers),
        },
        "Geolocation": {
            "User Location": random.choice(["New York, US", "London, UK", "Berlin, DE", "Mumbai, IN", "Tokyo, JP", "Sydney, AU", "Dubai, UAE", "Cape Town, ZA", "Rio de Janeiro, BR", "Toronto, CA", "Moscow, RU", "Beijing, CN", "Riyadh, SA", "Mexico City, MX", "Buenos Aires, AR", "Nairobi, KE", "Singapore, SG", "Seoul, KR", "Istanbul, TR", "Paris, FR"]),
            "Timezone": random.choice(["UTC-5", "UTC+1", "UTC+5:30", "UTC+9", "UTC+10", "UTC+2", "UTC+3", "UTC+8", "UTC+4", "UTC+11", "UTC+6", "UTC+7", "UTC+12", "UTC+3:30", "UTC+4:30", "UTC+5", "UTC+6:30", "UTC+7:30", "UTC+8:30", "UTC+9:30", "UTC+10:30", "UTC+11:30", "UTC+12:30", "UTC-1", "UTC-2", "UTC-3", "UTC-4", "UTC-6", "UTC-7", "UTC-8", "UTC-9", "UTC-10", "UTC-11", "UTC-12"]),
        },
        "Login/Account": {
            "Login Method": random.choice(["social login", "manual login", "guest login", "biometric login"]),
            "Subscription Tier": random.choice(subscription_tiers),
        },
    }

# Generate Derived Metrics
def generate_derived_metrics(user_behavior_data):
    return {
        "Engagement Metrics": {
            "Average Watch Time": random.randint(10, 120),  # minutes
            "Completion Rate (%)": round(random.uniform(50, 100), 2),
            "Binge-Watching Tendency": random.choice([True, False]),
            "Pause Frequency": random.randint(0, 5),
            "Repeat Views": random.randint(0, 10),
        },
        "User Preferences": {
            "Preferred Genres": random.sample(genres, 3),
            "Most Active Time of Day": random.choice(["morning", "afternoon", "evening", "night"]),
            "Favorite Actors/Directors": random.sample(["Actor_1", "Actor_2","Actor_3", "Actor_4", "Actor_5", 
                                                        "Actor_6", "Actor_7", "Actor_8", "Actor_9", "Actor_10", 
                                                        "Director_1", "Director_2","Director_3", "Director_4", "Director_5", 
                                                        "Director_6", "Director_7", "Director_8", 
                                                        "Director_9", "Director_10"], 2),
        },
        "Content Performance Indicators": {
            "Abandonment Rate (%)": round(random.uniform(0, 50), 2),
            "Popular Watch Window": random.choice(["7 PM - 10 PM", "12 PM - 2 PM", "9 PM - 12 AM", 
                                                   "3 PM - 6 PM", "10 AM - 12 PM", "6 PM - 9 PM", 
                                                   "12 AM - 3 AM", "6 AM - 9 AM", "3 AM - 6 AM",]),
            "Skipping Behavior": round(random.uniform(0.1, 0.5), 2),
        },
        "Churn Prediction Factors": {
            "Days of Inactivity": random.randint(0, 60),
            "User Dissatisfaction Metrics": random.choice(["Search Failed", "Poor Playback", "App Crash", "Content Unavailability", 
                                                           "Subscription Issue", "Payment Failure", "Account Hacked", 
                                                           "Too Many Ads", "Privacy Concerns", "Other"]),
        },
    }

# Function to generate and print data samples continuously
# def generate_synthetic_data_continuously():
#     while True:
#         user_behavior = generate_user_behavior_data()
#         content_metadata = generate_content_metadata()
#         platform_usage = generate_platform_usage_data()
#         derived_metrics = generate_derived_metrics(user_behavior)

#         synthetic_data = {
#             "User Behavior Data": user_behavior,
#             "Content Metadata": content_metadata,
#             "Platform Usage Data": platform_usage,
#             "Derived Metrics": derived_metrics,
#         }

#         # Print the generated data
#         print(synthetic_data)

#         # Sleep for 2 seconds before generating new data
#         time.sleep(2)

# # Start generating data continuously
# generate_synthetic_data_continuously()
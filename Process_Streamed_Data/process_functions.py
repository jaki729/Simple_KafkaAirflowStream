from datetime import datetime
import mysql.connector

# MySQL Configuration
DB_CONFIG = {
    'host': 'localhost',          # Update with your server IP or hostname
    'database': 'customer_data',  # Update with your database name
    'user': 'root',               # Update with your username
    'password': 'password',      # Update with your password
}

def calculate_engagement_ratio(time_spent_watching, session_duration):
    """
    Calculate the engagement ratio for a user: time spent watching / session duration.
    Avoid division by zero by returning 0 if session_duration is 0.
    """
    return time_spent_watching / session_duration if session_duration else 0

def calculate_user_retention(user_id, action_type, session_count):
    """
    Calculate user retention score based on `action_type` and `session_count`.
    Retention is marked as 1 if the user shares content and has more than one session.
    """
    return 1 if action_type == 'Share' and session_count > 1 else 0

def process_user_behavior_data(user_behavior, content_metadata, platform_usage, derived_metrics):
    """
    Process the user behavior data and apply business-specific logic.
    """
    # Extracting user behavior data
    user_id = user_behavior.get('User ID', '')
    session_id = user_behavior.get('Session ID', '')
    action_type = user_behavior.get('Action Type', 'unknown')
    time_spent_watching = user_behavior.get('Time Spent Watching', 0)
    completion_status = user_behavior.get('Completion Status', 'unknown')
    content_id = user_behavior.get('Content ID', '')
    device_type = platform_usage.get('Device Information', {}).get('Device Type', 'unknown')
    session_duration = platform_usage.get('Session Data', {}).get('Session Duration (minutes)', 0)

    # Derived metrics
    avg_watch_time = derived_metrics.get('Engagement Metrics', {}).get('Average Watch Time', 0)
    binge_watching_tendency = derived_metrics.get('Engagement Metrics', {}).get('Binge-Watching Tendency', False)

    # Metric calculations
    engagement_ratio = calculate_engagement_ratio(time_spent_watching, session_duration)
    session_count = 1 if engagement_ratio > 0.5 else 0
    user_retention = calculate_user_retention(user_id, action_type, session_count)
    personalized_metric = "High Engagement" if binge_watching_tendency else "Low Engagement"

    # Forming processed data
    processed_data = {
        'user_id': user_id,
        'session_id': session_id,
        'content_id': content_id,
        'time_spent_watching': time_spent_watching,
        'completion_status': completion_status,
        'device_type': device_type,
        'session_duration': session_duration,
        'avg_watch_time': avg_watch_time,
        'binge_watching_tendency': int(binge_watching_tendency),  # Store boolean as int (0/1)
        'engagement_ratio': engagement_ratio,
        'session_count': session_count,
        'user_retention': user_retention,
        'personalized_metric': personalized_metric,
        'time_stamp': user_behavior.get('Timestamp', datetime.now().isoformat()),
    }
    return processed_data

def store_in_mysql(processed_data):
    """
    Store the processed data into MySQL.
    """
    insert_query = """
        INSERT INTO user_behavior_data (
            user_id, session_id, content_id, time_spent_watching, completion_status,
            device_type, session_duration, avg_watch_time, binge_watching_tendency,
            engagement_ratio, session_count, user_retention, personalized_metric, time_stamp
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data_tuple = (
        processed_data['user_id'],
        processed_data['session_id'],
        processed_data['content_id'],
        processed_data['time_spent_watching'],
        processed_data['completion_status'],
        processed_data['device_type'],
        processed_data['session_duration'],
        processed_data['avg_watch_time'],
        processed_data['binge_watching_tendency'],
        processed_data['engagement_ratio'],
        processed_data['session_count'],
        processed_data['user_retention'],
        processed_data['personalized_metric'],
        processed_data['time_stamp']
    )

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Insert data into MySQL
        cursor.execute(insert_query, data_tuple)
        conn.commit()
        print("Data inserted successfully:", processed_data)

    except mysql.connector.Error as e:
        print(f"Error inserting data into MySQL: {e}")

    finally:
        # Ensure resources are closed properly
        if cursor:
            cursor.close()
        if conn:
            conn.close()
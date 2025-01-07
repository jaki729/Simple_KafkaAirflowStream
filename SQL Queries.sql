CREATE TABLE user_behavior_data (
    user_id VARCHAR(255),
    session_id VARCHAR(255),
    content_id VARCHAR(255),
    time_spent_watching FLOAT,
    completion_status VARCHAR(255),
    device_type VARCHAR(255),
    session_duration FLOAT,
    avg_watch_time FLOAT,
    binge_watching_tendency BOOLEAN,
    engagement_ratio FLOAT,
    session_count INT,
    user_retention INT,
    personalized_metric VARCHAR(255),
    time_stamp DATETIME
);

select * from user_behavior_data;

GRANT ALL PRIVILEGES ON user_engagement.* TO 'root'@'localhost';
FLUSH PRIVILEGES;


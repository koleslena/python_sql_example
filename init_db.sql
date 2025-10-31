CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F')),
    date_of_birth TIMESTAMP NOT NULL
);
CREATE INDEX idx_gender_name ON users (gender, full_name text_pattern_ops);

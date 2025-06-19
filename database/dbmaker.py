import os
import sqlite3
import faker
import random

def add_data_pation(num_records=2):
    print(f"Adding {num_records} fake records to the database...")
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('database/clinic.db')
    cursor = conn.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            condition TEXT,
            phone_number TEXT,
            doctor_name TEXT,
            patient_gender TEXT,
            room TEXT,
            created_at TEXT,
            code TEXT
        )
    ''')
    
    # Create faker instance
    fake = faker.Faker()
    
    # Generate and insert fake data
    for _ in range(num_records):
        def generate_random_code(length=30):
            characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%@'
            return ''.join(random.choice(characters) for _ in range(length))

        cursor.execute('''
            INSERT INTO patients (name, age, condition, phone_number, doctor_name,
                    patient_gender, room, created_at, code)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            fake.name(),
            fake.random_int(min=1, max=100),
            fake.word(),
            fake.phone_number(),
            "",
            fake.random_element(['Male', 'Female']),
            fake.random_int(min=100, max=999),
            fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            generate_random_code()
        ))
    
    conn.commit()
    conn.close()
    print("Data addition completed.")

add_data_pation(43)


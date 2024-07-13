import sqlite3

def add_user_to_db(user_id, username, fullname):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT is_active FROM users WHERE user_id = ?
    ''', (user_id,))
    result = cursor.fetchone()

    if result is not None:
        if result[0] == 0:  
            cursor.execute('''
            UPDATE users
            SET is_active = 1
            WHERE user_id = ?
            ''', (user_id,))
    else:
        cursor.execute('''
        INSERT OR IGNORE INTO users (user_id, username, fullname, is_active) VALUES (?, ?, ?, 1)
        ''', (user_id, username, fullname))

    conn.commit()
    conn.close()

def delete_user_from_db(user_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM users WHERE user_id = ?
    ''', (user_id,))
    conn.commit()
    conn.close()

def get_video (code):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT video_id FROM videos WHERE id = ?
    ''', (code,))  
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None



def add_video(video_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO videos (video_id) VALUES (?)
    ''', (video_id,))
    conn.commit()
    cursor.execute('''
    SELECT id FROM videos WHERE video_id = ?
    ''', (video_id,))  
    result = cursor.fetchone()
    conn.close()
    if result:
        return int(result[0])
    else:
        return None

def count_video():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT COUNT(*) FROM videos;
    ''')  
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None


def count_user():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT COUNT(*) FROM users;
    ''')  
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
    
def get_all_user():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT user_id FROM users;
    ''')  
    result = cursor.fetchall()
    conn.close()

    return result

def set_inactive(user_id):
    if not isinstance(user_id, int):
        raise ValueError("user_id must be an integer")

    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        UPDATE users
        SET is_active = 0
        WHERE user_id = ?
        ''', (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def active_users():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT COUNT(*) FROM users WHERE is_active = 1;
    ''')  
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def inactive_users():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT COUNT(*) FROM users WHERE is_active = 0;
    ''')  
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

 
def count_videos():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT COUNT(*) FROM videos;
    ''')  
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None   

def delete_video(id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM videos WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    ask = input("Do you want to delete all VIDEOS(yes/no): ")
    if ask == "yes":
        cursor.execute('''DROP TABLE videos ''')
        print("All vidoes deleted successfully")
    
    ask = input("Do you want to delete all USERS(yes/no): ")
    if ask == "yes":
        cursor.execute('''DROP TABLE users ''')
        print("All users deleted successfully")

    conn.commit()
    conn.close()
    

    


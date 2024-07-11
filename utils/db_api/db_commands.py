import sqlite3

def add_user_to_db(user_id, username, fullname):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO users (user_id, username, fullname) VALUES (?, ?, ?)
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
    
if __name__ == "__main__":
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE videos ''')
    cursor.execute('''DROP TABLE users ''')
    conn.commit()
    conn.close()
    

    


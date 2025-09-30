def registrar_usuario(nombre, email, conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()

    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE email = ?", (email,))
    return cursor.fetchone()

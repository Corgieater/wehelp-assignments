from website import createApp, connection, mycursor

app = createApp()

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    connection.close()
    mycursor.close()


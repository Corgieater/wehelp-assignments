from website import createApp, mydb, mycursor

app = createApp()

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    mydb.close()
    mycursor.close()

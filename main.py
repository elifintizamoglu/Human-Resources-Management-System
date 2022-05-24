from website import create_app

app = create_app()

if __name__ == "__main__":  # only if we run this file, execute line below
    app.run(host='localhost', port=5000, debug=True, threaded=True)

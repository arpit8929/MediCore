from website import create_app

app = create_app()

# No need to call app.run() for Vercel
# Vercel will automatically find 'app'

if __name__ == "__main__":
    app.run(debug=True)

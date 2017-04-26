from betterapis.app import api, db

if __name__ == '__main__':
    db.create_all()
    api.run(port=8080, debug=True)

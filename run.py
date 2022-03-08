#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#.\env\Scripts\activate.ps1

from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
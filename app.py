from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from pymongo import MongoClient
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(10)

username = "user_42ugex9bj"
password = "p42ugex9bj"
host = "ocdb.app"
port = 5050
database = "db_42ugex9bj"

connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database}"

my_client = MongoClient(connection_string)
my_db = my_client[database]
users = my_db["users"]

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        name = request.form["user_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        users.insert_one({"name":name, "phone":phone, "email":email})
        flash("Data Has Been Stored")
        response = get_flashed_messages()
        return render_template("index.html", messages=response)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
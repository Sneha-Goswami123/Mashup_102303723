from flask import Flask, request
import zipfile
import yagmail
import os
from mashup import run_mashup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = int(request.form["videos"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        output_file = "web_output.mp3"

        run_mashup(singer, videos, duration, output_file)

        zip_name = "result.zip"
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(output_file)

        yag = yagmail.SMTP(
            os.environ.get("email_user"),
            os.environ.get("email_pass")
        )

        yag.send(email, "Mashup File", "Here is your mashup.", zip_name)

        return "Mashup sent successfully!"

    return '''
    <form method="post">
        Singer: <input name="singer"><br>
        Videos: <input name="videos"><br>
        Duration: <input name="duration"><br>
        Email: <input name="email"><br>
        <input type="submit">
    </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

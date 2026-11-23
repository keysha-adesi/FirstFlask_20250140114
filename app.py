
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")

        if nama:
            pesan = "Halo, " + nama + "!"
        else:
            pesan = "Nama tidak boleh kosong."

        return render_template("index.html", pesan=pesan)

    return render_template("index.html", pesan="")

if __name__ == "__main__":
    app.run(debug=True)




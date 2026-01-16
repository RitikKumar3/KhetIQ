from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# ------------------------
# HOME
# ------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# ------------------------
# ABOUT
# ------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# ------------------------
# SERVICES
# ------------------------
@app.route("/services")
def services():
    return render_template("services.html")


# ------------------------
# SOLUTIONS
# ------------------------
@app.route("/solutions")
def solutions():
    return render_template("solutions.html")


# ------------------------
# INSIGHTS
# ------------------------
@app.route("/insights")
def insights():
    return render_template("insights.html")


# ------------------------
# CONTACT (LEAD FORM)
# ------------------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # TODO: store/send lead (DB, email, CRM, etc.)
        print("New Lead:", name, email, message)

        # Flash message for UX
        flash("Thank you! We'll get back to you soon.")

        # 🔹 TRUE CONVERSION REDIRECT
        return redirect(url_for("thank_you"))

    return render_template("contact.html")


# ------------------------
# THANK YOU (CONVERSION PAGE)
# ------------------------
@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


# ------------------------
# TEST ROUTES (UNCHANGED)
# ------------------------
@app.route("/test-video")
def test_video():
    return render_template("test_video.html")

@app.route("/video-direct")
def video_direct():
    return render_template("video_test_direct.html")

@app.route("/test-minimal")
def test_minimal():
    return render_template("home_minimal.html")

@app.route("/video-test")
def video_test():
    return render_template("home_video_test.html")


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=10000)

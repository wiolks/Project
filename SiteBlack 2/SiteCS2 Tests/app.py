from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

# Пример данных о видео (можно заменить на данные из базы данных)
video_categories = {
    "Inferno": {
        "Smokes": [
            "Smoke - Banana Start.mp4",
            "Smoke - Coffins.mp4",
            "Smoke - CT (From Woods).mp4",
            "Smoke - CT + Boost.mp4",
            "Smoke - Long.mp4",
            "Smoke + Flash (CT) - Banana T from coffins.mp4",
            "Smoke CT - Banana Start from Fountain.mp4",
        ],
        "Flashes": [
            "Flash - Flash - Banana.mp4",
            "Flash - B site.mp4",
            "Flash - CT - Start Banana.mp4",
            "Flash CT - CAR.mp4",
            "Flash CT - to Banana Support.mp4",
        ],
        "Molotovs": [
            "Molotov - 1st.Mp4",
            "Molotov - Dark.mp4",
            "Molotov - in 3rd.mp4",
            "Molotov CT - Car from fountain.mp4",
        ],
    },
    "Mirage": {
        "Smokes": [],
        "Flashes": [],
        "Molotovs": []
    },
    "Dust2": {
        "Smokes": [],
        "Flashes": [],
        "Molotovs": []
    },
}

@app.route("/")
def index():
    return render_template("index.html", categories=video_categories.items())

@app.route("/category/<category_name>")
def show_category(category_name):
    category = video_categories.get(category_name)
    if (
        category
        and isinstance(category, dict)
    ):
        return render_template(
            "category_index.html",
            category_name=category_name,
            subcategories=category.items(),
        )
    else:
        abort(404)

@app.route("/category/<category_name>/<subcategory_name>")
def show_subcategory(category_name, subcategory_name):
    category = video_categories.get(category_name)
    if (
        category
        and isinstance(category, dict)
        and subcategory_name in category
    ):
        videos = category.get(subcategory_name, [])
        if not videos:
            abort(404)
        return render_template(
            "video_category.html",
            category=category_name,
            videos=videos,
            subcategory=subcategory_name,
        )
    else:
        abort(404)

@app.route("/videos/<filename>")
def serve_video(filename):
    return send_from_directory("static/videos", filename)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
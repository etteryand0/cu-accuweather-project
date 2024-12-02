from flask import (
    Blueprint,
    flash,
    render_template,
    request,
)

bp = Blueprint("weather", __name__, url_prefix="/weather")


@bp.route("/", methods=("GET", "POST"))
def weather():
    if request.method == "GET":
        return render_template("weather.html")

    start_city = request.form.get("start_city")
    end_city = request.form.get("end_city")

    return render_template("weather.html", result=f"{start_city=}, {end_city=}")


def check_bad_weather(
    temperature, wind_speed, precipitation_probability, humidity, pressure
):
    if (
        temperature < 0
        or temperature > 35
        or wind_speed > 50
        or precipitation_probability > 70
        or humidity > 90
        or pressure < 1000
    ):
        return "Плохие погодные условия"
    else:
        return "Хорошие погодные условия"

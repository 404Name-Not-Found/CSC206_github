from jinja2 import Template
display = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>

<body>
<div class="columns m-5 is-multiline">
    {% for car in all_cars %}

<!-- The columns that present the car information in boxes -->
    <div class="column p-4 is-one-third">
        <div class="box">
            <figure class="image is-200x200">
                <img src="/static/images/simplecar.jpg">
            </figure>
            <div class="media-content">
                <p class="is-size-3 mb-1"><strong>{{ car.Model }}</strong></p>
                <p class="is-size-5 mb-1">
                    {{ car.Year }} - {{ car.Make }}<br>
                    {{ car.Color }}<br>
                </p>
                <br>
            </div>
        </div>
    </div>

    {% endfor %}
</div>
</body>

<html>
""")
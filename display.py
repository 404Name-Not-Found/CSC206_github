from jinja2 import Template
display = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>

<!-- The columns that present the car information in boxes -->
<div class="columns m-5">

    <div class="colum p-4">
        <div class="box">
            <figure class"image is-128x128">
                <img src="/static/images/simplecar.jpg">
            </figure>
            <div class="media-content">
                <p>
                    <p class="is-size-3"><strong>Car 1</strong></p>
                    <br>
                </p>
            </div>
        </div>
    </div>
    
    <div class="colum p-4">
        <div class="box">
            <figure class"image is-128x128">
                <img src="/static/images/simplecar.jpg">
            </figure>
            <div class="media-content">
                <p>
                    <p class="is-size-3"><strong>Car 2</strong></p>
                    <br>
                </p>
            </div>
        </div>
    </div>
    
    <div class="colum p-4">
        <div class="box">
             <figure class"image is-128x128">
                <img src="/static/images/simplecar.jpg">
            </figure>
            <div class="media-content">
                <p>
                    <p class="is-size-3"><strong>Car 3</strong></p>
                    <br>
                </p>
            </div>
        </div>
    </div>
</div>

<html>
""")
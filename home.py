from jinja2 import Template
header = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css">
    
</head>

<nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-menu m-4">
    
        <!-- Heading -->
        <div class="navbar-start">
            <p class="is-size-3">Ben's Automobiles</p>
        </div>
        
        <!-- Sign In Button -->
        <div class="navbar-end>
            <div class="navbar-item">
                <div class="buttons is-centered">
                    <a class="button is-medium is-primary" href="/page1">Sign In</a>
                </div>
            </div>
        </div>
        
    </div>
</nav>

<body class="has-background-info"></body>

 <main class="content site-content">{{ content }}</main>
    
<footer class="footer">
    <p>2025 Ben Schuck</p>
</footer>
""")

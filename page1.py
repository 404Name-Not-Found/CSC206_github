header = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1"
    
    <!-- Link to Bulma -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css">
</head>

<!-- I found the hero element allows me to make banner that I can center for the login information-->
<section class="hero is-fullheight is-white">
    <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-4 is-offset-4">
            <div class="mt-4">
            
                <!-- Found information about this box on the bulma website and it looked like a login format -->
                <form class="box">
                
                  <div class="field">
                    <label class="label has-text-left">User</label>
                    <div class="control">
                      <input class="input" type="email" placeholder="Admin, Buyer, Seller" />
                    </div>
                  </div>
                
                  <div class="field">
                    <label class="label has-text-left">Password</label>
                    <div class="control">
                      <input class="input" type="password" placeholder="Password" />
                    </div>
                  </div>
                  
                  <!-- Linking an a tag and formatting it to look like a button was easier than making a button work -->  
                  <a class="button is-medium is-fullwidth" href="/home">Login</a>
                  
                </form>
'''

footer = '''
            </div>
          </div>
        </div>
    </div>
    
    <footer class="footer">
        <p>2025 Ben Schuck</p>
    </footer>
</section>
'''

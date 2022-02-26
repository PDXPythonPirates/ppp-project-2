"""Plotly Dash HTML layout override."""


html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            <title>Crypto News</title>
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <h3>Return Home</h3>
                  </a>
                <nav>
                </nav>
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""

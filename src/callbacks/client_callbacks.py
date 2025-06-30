from dash import Input, Output


def register_client_callback(app):
    # Force scroll to top on page load
    app.clientside_callback(
        """
        function(pathname) {
            // Small delay to ensure DOM is fully rendered
            setTimeout(() => {
                const scrollContainer = document.querySelector('.scroll-container');
                if (scrollContainer) {
                    scrollContainer.scrollTop = 0;
                }
            }, 100);
            return null;
        }
        """,
        Output("url", "search"),
        Input("url", "pathname"),
    )

    app.clientside_callback(
        """
        function(href) {
        const [path, hash] = href.split('#');
        if (!hash) return '';

        // If not on Home page, redirect
        if (path !== '/' && path !== window.location.origin + '/') {
            window.location.href = '/' + '#' + hash;
            return '';
        }

        // Already on Home — scroll to section smoothly
        const section = document.getElementById(hash);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        return '';
        }
        """,
        Output("anchor-jump", "children"),
        Input("url", "href"),
    )

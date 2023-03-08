#requirements: None

#imports
from reactor import ReactSite

#code
if __name__ == "__main__":
    # Create the ReactSite object 
    site = ReactSite("my_react_site")

    # Setup the initial site structure
    site.setup()

    # Update the site with custom components and libraries
    site.add_react_components(["MyComponent"])
    site.add_react_libraries(["bootstrap"])
    site.update()

    # Create new dynamic pages
    pages_dict = {"about": "<h1>About Us</h1><p>Welcome to our site!</p>",
                "contact": "<h1>Contact Us</h1><p>Get in touch with us!</p>"}
    site.create_dynamic_pages(pages_dict)

    # Add custom CSS and JavaScript files to the site
    css_files = ["custom.css"]
    js_files = ["custom.js"]
    site.add_css_links(css_files)
    site.update_js_files(js_files)
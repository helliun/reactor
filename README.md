To use the ReactSite class in the reactor.py module, follow these instructions:

1. Import the ReactSite class from reactor.py using the statement: 
   from reactor import ReactSite

2. To create a new React site, instantiate the ReactSite class with the desired site name like this:
    my_site = ReactSite('my_site_name')
    This will create a new directory with the specified site name and all the necessary files and directories for a basic React app in it.

3. To update the site files with dynamic content, use the various methods of the ReactSite class:
    - To update the package.json, index.html and index.js files with the site name, use the 'update' method with no arguments:
        my_site.update()
    - To add links to external css files, use the 'add_css_links' method with a list of css file names:
        my_site.add_css_links(['style.css', 'custom.css'])
    - To add links to external javascript files, use the 'update_js_files' method with a list of js file names:
        my_site.update_js_files(['script.js'])
    - To create new dynamic pages using a dictionary with page names and html content, use the 'create_dynamic_pages' method:
        page_dict = {'about': '<h1>About Page</h1>', 'contact': '<h1>Contact Page</h1>'}
        my_site.create_dynamic_pages(page_dict)
    - To create new React components using a list of component names, use the 'add_react_components' method:
        my_site.add_react_components(['Header', 'Footer', 'Navigation'])
    - To link to external React.js libraries (e.g. bootstrap), use the 'add_react_libraries' method:
        my_site.add_react_libraries(['bootstrap', 'font-awesome'])
        
Note: All file names and directory structures assume the default configuration of react.js projects. If additional customization is required, modify the code accordingly.
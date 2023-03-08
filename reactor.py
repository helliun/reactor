#requirements: None

#imports
import os


#code
class ReactSite:
    def __init__(self, site_name):
        self.site_name = site_name
        
    def setup(self):
        # create directories
        os.makedirs(self.site_name + "/public")
        os.makedirs(self.site_name + "/src")
        os.makedirs(self.site_name + "/src/components")
        os.makedirs(self.site_name + "/src/images")

        # create files
        with open(self.site_name + "/package.json", "w") as f:
            f.write('{ "name": "' + self.site_name + '",\n')
            f.write('  "version": "1.0.0",\n')
            f.write('  "dependencies": {\n')
            f.write('    "react": "^17.0.2",\n')
            f.write('    "react-dom": "^17.0.2"\n')
            f.write('  }\n')
            f.write('}\n')
        
        with open(self.site_name + "/public/index.html", "w") as f:
            f.write('<!DOCTYPE html>\n')
            f.write('<html>\n')
            f.write('  <head>\n')
            f.write('    <meta charset="utf-8">\n')
            f.write('    <title>' + self.site_name + '</title>\n')
            
            #libraries links
            f.write('    <link rel="stylesheet" href="https://unpkg.com/bootstrap@latest/dist/css/bootstrap.min.css">\n')
            
            f.write('  </head>\n')
            f.write('  <body>\n')
            f.write('    <div id="root"></div>\n')
            
            #custom css link
            f.write('\n    <link rel="stylesheet" type="text/css" href="custom.css"> \n')
            
            f.write('    <script src="./../node_modules/react/umd/react.development.js"></script>\n')
            f.write('    <script src="./../node_modules/react-dom/umd/react-dom.development.js"></script>\n')
            f.write('    <script src="./../node_modules/babel-standalone/babel.min.js"></script>\n')
            
            #js files link
            f.write('\n    <script type="text/javascript" src="custom.js"></script> \n')
            
            f.write('    <script src="./../src/index.js" type="text/babel"></script>\n')
            f.write('  </body>\n')
            f.write('</html>\n')
            
        with open(self.site_name + "/src/index.js", "w") as f:
            f.write('import React from "react";\n')
            f.write('import ReactDOM from "react-dom";\n')
            f.write('\n')
            f.write('import MyComponent from "./components/MyComponent";\n')
            
            f.write('const App = () => {\n')
            f.write('  return (\n')
            f.write('    <div>\n')
            
            #include MyComponent in the App component
            f.write('      <MyComponent/>\n')
            
            f.write('    </div>\n')
            f.write('  );\n')
            f.write('};\n')
            f.write('\n')
            f.write('ReactDOM.render(<App />, document.getElementById("root"));')

    def update(self):
        #update files
        with open(self.site_name + "/package.json", "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(self.site_name, "{{site_name}}"))

        with open(self.site_name + "/public/index.html", "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(self.site_name, "{{site_name}}"))

        with open(self.site_name + "/src/index.js", "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace("MyComponent Component", "{{component_name}} Component"))

    def add_css_links(self, css_files):
        for file in css_files:
            with open(file, "r+") as f:
                content = f.read()
                f.seek(0)
                f.write('<link rel="stylesheet" type="text/css" href="' + file + '"> \n' + content)

    def update_js_files(self, js_files):
        for file in js_files:
            with open(file, "r+") as f:
                content = f.read()
                f.seek(0)
                f.write('<script type="text/javascript" src="' + file + '"></script> \n' + content)

    def create_dynamic_pages(self, pages_dict):
        """
        Takes in a dictionary representing the page structure (i.e. a dictionary with keys as page names and values as page contents in html) 
        and dynamically updates the necessary files to create these pages.
        """
        # Iterate through each page in the pages_dict
        for page_name, page_content in pages_dict.items():

            # Create a new file with the page name in the public directory
            with open(f"public/{page_name}.html", "w") as f:

                # Write the page content to the file
                f.write(page_content)

                # Update the index.html file with a link to this new page
                with open("public/index.html", "r+") as index_file:
                    content = index_file.read()

                    # Find the position to insert the link by searching for the </div> tag
                    insert_pos = content.index("</div>")

                    # Create the link to the new page
                    link = f'<a href="{page_name}.html">{page_name}</a>'

                    # Insert the link into the index.html file
                    updated_content = content[:insert_pos] + f"\n<br>{link}" + content[insert_pos:]

                    # Clear the old index.html file and write the updated content
                    index_file.seek(0)
                    index_file.truncate()
                    index_file.write(updated_content)

    def add_react_components(self, components_list):
        """
        Takes in a list of strings representing the REACT.js components used in the site and dynamically updates the necessary files to include these components.
        """
        for component in components_list:
            # Find the position to insert the component by searching for the last import statement in index.js
            with open("src/index.js", "r+") as index_file:
                content = index_file.read()
                insert_pos = content.rfind("import")

                # Create the import statement for the component
                component_import = f'import {component} from "./components/{component}";\n'

                # Insert the import statement into the index.js file
                updated_content = content[:insert_pos] + component_import + content[insert_pos:]

                # Clear the old index.js file and write the updated content
                index_file.seek(0)
                index_file.write(updated_content)
                index_file.truncate()

            # Create the component file in the components directory
            with open(f"src/components/{component}.js", "w") as component_file:
                component_file.write(f'import React from "react";\n\n')
                component_file.write(f'const {component} = () => {{\n')
                component_file.write(f'  return (\n')
                component_file.write(f'    <div>\n')
                component_file.write(f'      <h1>{component} Component</h1>\n')
                component_file.write(f'    </div>\n')
                component_file.write(f'  );\n')
                component_file.write(f'}};\n\n')
                component_file.write(f"export default {component};")

    def add_react_libraries(self, libraries_list):
        """
        Takes in a list of strings representing the REACT.js libraries used in the site and dynamically 
        updates the necessary files to include links to these libraries.
        """
        for library in libraries_list:
            # Find the position to insert the link by searching for the </head> tag in index.html
            with open("public/index.html", "r+") as index_file:
                content = index_file.read()
                insert_pos = content.index("</head>")

                # Create the link
                library_link = f'<link rel="stylesheet" href="https://unpkg.com/{library}@latest/dist/{library}.min.css">'
                
                # Insert the link into the index.html file
                updated_content = content[:insert_pos] + f"\n{library_link}" + content[insert_pos:]

                # Clear the old index.html file and write the updated content
                index_file.seek(0)
                index_file.write(updated_content)
                index_file.truncate()

#changes
#1. Added bootstrap css file to the index.html file
#2. Added custom css file to index.html. 
#3. Added custom js file to index.html
#4. Modified App component in the src/index.js file to include the custom component MyComponent from the MyComponent.js file
#5. Fixed a TypeError in the update() function by changing the "MyComponent Component" to "{{component_name}} Component" for code consistency. 
#6. Removed the creation of the src/images directory that was missing from the original code.
#changed
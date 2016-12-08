# NWEA
Repo for the NWEA code assignment

This will have a total of 3 code files: 2 html files  and one python script.  


Requirements:
1. Have python 3 installed. You can download from https://www.python.org/downloads/
  Follow the installation instructions and be aware of where the default python app directory is. For example, on windows, you can specify   the default install directory to be C:\python
  
2. For convenience, make sure that your python application is in your PATH environment variable. This will make it easy to invoke python from the command line.  
  
3. Make sure you have PIP installed. If you are using python 3+ it should already be installed. If you need to install, go to https://pip.pypa.io/en/stable/installing/  for directions. To verify your installation, you can run the command: pip install -U pip from the command line. (This will perform an update of pip, if needed)

4. Install Flask. This is why you need pip. Run the command: pip install Flask. More detailed instructions are found here: http://flask.pocoo.org/docs/0.10/installation/

5. Download the files blogserver.py and blog.db to the default directory of your python installation. For example, if you installed python to C:\python, please put the files in that directory.

6. Download the two html files form_submit.html, and form_action.html and place them in the /templates subdir of your python folder. If /templates does not exist, go ahead and make that directory. For example, you would place the files in C:\python\templates\ 


To Run:
1. Invoke python script from command line: type: 'python blogserver.py'. The script will start a small webserver that will run on your computer on port 5000 

2. Open a browser and navigate to http://localhost:5000/. This will display a form for you to make entries into the blog.

3. To display the contents of the blog, navigate to http://localhost:5000/posts


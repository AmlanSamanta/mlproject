### End to end Machine Learning project


## Steps

1. Create a public repo in Github (to share the work with world) with a name, say, mlproject, without
specifying any other details or chossing options. It is succesfully done, you will be able to view some commands like below:

…or create a new repository on the command line
echo "# mlproject" >> README.md
git init
git add README.md
git commit -m "first commit"
git status
git branch -M main
git remote add origin https://github.com/AmlanSamanta/mlproject.git
git remote -v
git push -u origin main (If you are a first time user of Git in your cxomputer's command line, run these first and then go for pushing changes: git config --global user.name "<Your name>"; git config --global user.email "<Your email>")

…or push an existing repository from the command line
git remote add origin https://github.com/AmlanSamanta/mlproject.git
git branch -M main
git push -u origin main

2. Create a directory with the same name in your computer and open a command line in that to type <code .>
(Ensure you have already installed Anaconda and VSCode in your computer)
3. Create a virtual environment with this command: <conda create -p venv python==3.10 -y>
After successfull installation activate the same with it: <conda activate venv/>
4. Now follow the steps shown in Step 1 under "create a new repository on the command line" section.
5. create a .gitignore file with Python template and commit the changes to the newly created repository. Also do <git pull> to sync the changes from remote to local.

## Development of project structure: It can be automated by leverging <template.py> 

6. Create 2 more files:
   -- setup.py: for building the entire application as package 
   -- requirements.txt: for efficient installation of project dependencies
7. Write code in setup.py and create a directory inside our project with name 'src', also create a file with name '__init__.py' inside 'src' to identify it as a package. Whatever project components we will be developing, would reside inside this directory.
8. Add '-e .' in requirements.txt to trigger the execution of <setup.py> file at the time of installing requirements from command line and also to build the application as package. Accordingly do adjustments in the <setup.py> code.
9. Now open terminal and run <pip install -r requirements.txt>. Once the process is done successfully, you should be able to see mlProject.egg-info folder inside your project. It means your project is built successfully as a python package which can be release into Pypi portal.
10. Create below mentioned directories and files inside <src>:
    - Components: under which all the project modules will reside
    - Pipeline: under which all pipeline modules will be 
    - <exception.py>: custom exception handler
    - <logger.py>: custom logger
    - <utils.py>: common useful functions to be accessed across entire project
11. Create a folder <notebooks> outside <src> where all Jupyter notebooks will stay.

name = "sgtk"

version = "dev"

build_command = "python {root}/build.py {install}"

private_build_requires = ["python"]

def commands():
    global env
    
    env.PYTHONPATH.append("{root}/python")
import pandas as pd
import hazelbean as hb
import os, subprocess, sys

from global_invest.crop_provision import crop_provision_initialization
from global_invest.livestock_provision import livestock_provision_initialization
from global_invest.renewable_energy_provision import renewable_energy_provision_initialization

def render_all(p):
    print("Rendering all GEP results.")

    # Set the quarto path to wherever the current script is running. This means that the environment used needs to have quarto, which may not be true on e.g. codespaces.
    os.environ['QUARTO_PYTHON'] = sys.executable
    
    # Get the  list of current services run
    services_run = list(p.results.keys())
    
    # Get the last (presumably most recent, but this is hackish) service run
    service_label = services_run[-1]
    
    # Imply from the service name the file_path for the results_qmd
    module_root = hb.get_projectflow_module_root()
    

    results_qmd_path = os.path.join(module_root, service_label, f'{service_label}_results.qmd')    
    results_qmd_project_path = os.path.join(p.cur_dir, f'{service_label}_results.qmd')
    hb.create_directories(results_qmd_project_path)  # Ensure the directory exists   
    
    # Copy it to the project dir for cmd line processing (but will be removed again later because it makes confusion when people try to edit it and then rerun the script which won't of course update the results.)
    hb.path_copy(results_qmd_path, results_qmd_project_path)
    
    # Set the Current Directory to an environment-level variable that can be used by quarto.
    os.environ['PROJECTFLOW_ROOT'] = p.project_dir
    
    quarto_command = f"quarto render {results_qmd_project_path}"
    hb.log(f"Running quarto command: {quarto_command}")     

    """Run quarto with debug information"""
    # Set environment for more verbose output
    env = os.environ.copy()
    env['QUARTO_LOG_LEVEL'] = 'DEBUG'
    
    cmd = ['quarto', 'render', results_qmd_project_path, '--verbose']
    
    # print(f"Running command: {' '.join(results_qmd_project_path)}")
    print(f"Working directory: {os.getcwd()}")
    print(f"File exists: {os.path.exists(results_qmd_project_path)}")
    
    
    
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Combine stderr into stdout
        text=True,
        bufsize=1,  # Line buffering
        universal_newlines=True
    )
    
    # Read line by line as they come
    while True:
        line = process.stdout.readline()
        if not line and process.poll() is not None:
            break
        if line:
            print(line.rstrip())
            sys.stdout.flush()  # Force immediate display
    # remove results_qmd_project_path
    hb.path_remove(results_qmd_project_path)
        
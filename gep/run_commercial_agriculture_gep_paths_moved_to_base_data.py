import os
import pandas as pd
import hazelbean as hb

from global_invest.commercial_agriculture import commercial_agriculture_tasks
import gep_initialize_project


if __name__ == '__main__':

    # Create a ProjectFlow Object to organize directories and enable parallel processing.
    p = hb.ProjectFlow()

    # Assign project-level attributes to the p object (such as in p.base_data_dir = ... below)
    # including where the project_dir and base_data are located.
    # The project_name is used to name the project directory below. If the directory exists, each task will not recreate
    # files that already exist. 
    p.user_dir = os.path.expanduser('~')        
    p.extra_dirs = ['Files', 'gep', 'projects']
    p.project_name = 'gep_commercial_agriculture'  # This is the name of the project directory.
    # p.project_name = p.project_name + '_' + hb.pretty_time() # If don't you want to recreate everything each time, comment out this line.
    
    # Based on the paths above, set the project_dir. All files will be created in this directory.
    p.project_dir = os.path.join(p.user_dir, os.sep.join(p.extra_dirs), p.project_name)
    p.set_project_dir(p.project_dir) 

    gep_initialize_project.build_gep_commercial_agriculture_task_tree(p)

    # Set the base data dir. The model will check here to see if it has everything it needs to run.
    # If anything is missing, it will download it. You can use the same base_data dir across multiple projects.
    # Additionally, if you're clever, you can move files generated in your tasks to the right base_data_dir
    # directory so that they are available for future projects and avoids redundant processing.
    # The final directory has to be named base_data to match the naming convention on the google cloud bucket.
    # p.base_data_dir = os.path.join(p.user_dir, 'files', 'base_data')
    p.base_data_dir = "G:/Shared drives/NatCapTEEMs/Files/base_data"

    # For speed, we will load the countries vector just once, in the project initialization.
    p.countries_csv_path = p.get_path('cartographic', 'ee', 'ee_r264_correspondence.csv')
    p.countries_vector_path = p.get_path('cartographic', 'ee', 'ee_r264_correspondence.gpkg')
    gep_initialize_project.initialize_paths(p)
    


    # ProjectFlow downloads all files automatically via the p.get_path() function. If you want it to download from a different 
    # bucket than default, provide the name and credentials here. Otherwise uses default public data 'gtap_invest_seals_2023_04_21'.
    p.data_credentials_path = None
    p.input_bucket_name = None
    
    # All results will be stored here by each child task.
    p.results = {}

    hb.log('Created ProjectFlow object at ' + p.project_dir + '\n    from script ' + p.calling_script + '\n    with base_data set at ' + p.base_data_dir)
    
    p.execute()
    
    result = 'Done!'


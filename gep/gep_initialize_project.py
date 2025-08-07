import pandas as pd
import hazelbean as hb

from global_invest.crop_provision import crop_provision_initialization
from global_invest.livestock_provision import livestock_provision_initialization
from global_invest.renewable_energy_provision import renewable_energy_provision_initialization

from gep import gep_tasks

def initialize_paths(p):
    p.df_countries = pd.read_csv(p.df_countries_csv_path)  
    p.gdf_countries = p.gdf_countries_vector_path 
    p.gdf_countries_simplified = p.gdf_countries_vector_simplified_path 
    
def build_gep_render_individual_task_tree(p):
    
    p = crop_provision_initialization.build_gep_service_task_tree(p)
    p = livestock_provision_initialization.build_gep_service_task_tree(p)
    p = renewable_energy_provision_initialization.build_gep_service_task_tree(p)
    
def build_gep_task_tree(p):
    
    p = crop_provision_initialization.build_gep_service_calculation_task_tree(p)
    p = livestock_provision_initialization.build_gep_service_calculation_task_tree(p)
    p = renewable_energy_provision_initialization.build_gep_service_calculation_task_tree(p)
    
    p.add_task(gep_tasks.render_all)
    
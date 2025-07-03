import pandas as pd
import hazelbean as hb

import global_invest
from global_invest.commercial_agriculture import commercial_agriculture_tasks

def initialize_paths(p):
    # p.ee_r264_gdf = hb.read_vector(p.countries_vector_path)
    p.ee_r264_df = pd.read_csv(p.countries_csv_path)
    
    
def build_gep_commercial_agriculture_task_tree(p):
    
    p = commercial_agriculture_tasks.build_gep_task_tree(p)
    

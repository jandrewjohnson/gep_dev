import global_invest
from global_invest.commercial_agriculture import commercial_agriculture_tasks

def build_gep_commercial_agriculture_task_tree(p):
    
    p = commercial_agriculture_tasks.build_gep_task_tree(p)
    

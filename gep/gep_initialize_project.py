import global_invest
from global_invest.pollination import pollination_tasks

def build_default_task_tree(p):
    p.pollination_task  = p.add_task(pollination_tasks.pollination_gep)
    
    
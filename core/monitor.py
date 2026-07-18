import psutil

def get_system_usage() -> tuple[float, float, float]:
    """
    Retrieves the current system resource utilization.
    
    Returns:
        tuple: (cpu_percentage, ram_percentage, disk_percentage)
    """
    try:
      
        cpu_usage = psutil.cpu_percent(interval=0.5)
        
   
        ram_info = psutil.virtual_memory()
        ram_usage = ram_info.percent
        
      
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        
        return cpu_usage, ram_usage, disk_usage
        
    except Exception:
        
        return 0.0, 0.0, 0.0
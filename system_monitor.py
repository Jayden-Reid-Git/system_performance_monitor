import psutil
import time

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)
    
def get_memory_usage():
    """Returns the current memory usage percentage."""
    memory_info = psutil.virtual_memory()
    return memory_info.percent
  
def get_disk_usage():
    """Returns the disk usage percentage for the C: drive."""
    disk_info = psutil.disk_usage("C:\\")
    return disk_info.percent
   
def get_top_processes():
    """Returns the top 5 processes consuming the most CPU."""
    processes = [(p.info["name"], p.info["cpu_percent"]) for p in psutil.process_iter(attrs=["name", "cpu_percent"])]
    processes.sort(key=lambda x: x[1], reverse=True)
    return processes[:5]
   
def log_performance():
    """Logs system performance data every 5 seconds."""
    with open("perfomance_log.txt", "a") as log_file:
        while True:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            disk_usage = get_disk_usage()
            top_processes = get_top_processes()
            
            log_entry = f"CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}%\n"
            log_entry += "Top Processes:\n" + "\n" .join([f"{p[0]}: {p[1]}%" for p in top_processes]) + "\n\n"
            
            print(log_entry)
            log_file.write(log_entry)
            time.sleep(5) # Log data every 5 seconds
            
if __name__ == "__main__":
    log_performance()

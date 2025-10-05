# Lightweight health monitor using psutil (optional)
try:
    import psutil
except Exception:
    psutil = None

def sample_system():
    if not psutil:
        return {}
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'virtual_memory': psutil.virtual_memory()._asdict(),
        'disk_usage': psutil.disk_usage('/')._asdict()
    }

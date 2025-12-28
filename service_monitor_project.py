class ServiceMonitor:
    def __init__(self, name, status, load):
        self.name = name
        self.status = status
        self.load = load

    def status_icon(self):
        if self.status.lower() == "online":
            return "✅"
        else:
            return "❌"

    def severity(self):
        if self.load >= 85:
            return "CRITICAL"
        elif self.load >= 70:
            return "WARNING"
        else:
            return "NORMAL"

    def is_overloaded(self):
        return self.load >= 75

    def summary(self):
        return f"{self.name} {self.status_icon()} | Load: {self.load} | {self.severity()}"


services = [
    ServiceMonitor("Auth", "online", 45),
    ServiceMonitor("Billing", "offline", 82),
    ServiceMonitor("Search", "online", 90),
    ServiceMonitor("Payments", "online", 30),
    ServiceMonitor("Cache", "offline", 25),
    ServiceMonitor("API", "online", 78)
]

total_services = 0
offline_services = 0
overloaded_services = 0
total_load = 0

for service in services:
    print(service.summary())

    total_services += 1
    total_load += service.load

    if service.status.lower() == "offline":
        offline_services += 1

    if service.is_overloaded():
        overloaded_services += 1

average_load = total_load / total_services

print("\n=== SYSTEM REPORT ===")
print(f"Total services: {total_services}")
print(f"Offline services: {offline_services}")
print(f"Overloaded services: {overloaded_services}")
print(f"Average load: {average_load}")

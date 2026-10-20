username = input("Enter username: ")

if username == "root":
    app_name = input("Enter the app name: ")

    if app_name == "grafana":
        port = 3000
        config_file = "/etc/grafana.conf"
    elif app_name == "prometheus":
        port = 9090
        config_file = "/etc/prometheus.yml"
    elif app_name == "webauth":
        port = 5001
        config_file = "/etc/web2.0/auth.cfg"
    else:
        app_name = "demoApp"
        port = 8000
        config_file = "/etc/demo.cfg"

    print(f"App name is: {app_name} running on port: {port} config file: {config_file}")
else:
    print("Access denied. Only root users can log in.")
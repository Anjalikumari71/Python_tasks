'''Write a python program:
->read an app name from <STDIN>
->test - input app name is: grafana - initialize app port num is 3000

    ->say message input app is not matched
    ->default app name is: demoApp running port: 8080

display app name and ru nnning port number.
'''

app_name = input("Enter the app name:")
if(app_name == "grafana"):
    port =3000
else:
    app_name = "demoApp"
    port=8080

print(f"App name is : {app_name} running port: {port}")
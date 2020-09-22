**This is a template framework to show how to run test using Selenoid**

Before running test please install Selenoid
Use the following commands:
'''
$ curl -s https://aerokube.com/cm/bash | bash
$ ./cm selenoid start --vnc
'''
(--vnc - this key is needed to connect to a browser in docker via vnc)

To check the status use:
curl http://localhost:4444/status

To run test using Selenoid, please specify the following settings
Go http://localhost:8080/#/capabilities/ and pick the Python for instance.
See the example of settings:
    capabilities = {
        "browserName": "firefox",
        "version": "79.0",
        "enableVNC": True,
        "enableVideo": False,
        "platform": "LINUX"
    }
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )

The Selenoid UI can be started using following:
$ ./cm selenoid-ui start

Finally, it should looks like that:
$ docker ps
CONTAINER ID  IMAGE                        COMMAND                 CREATED     STATUS              PORTS                   NAMES
78e1c32fe108  aerokube/selenoid-ui:1.10.0  "/selenoid-ui --sele…"  1 hour ago  Up 1 hour (healthy) 0.0.0.0:8080->8080/tcp  selenoid-ui
1fa9d850b722  aerokube/selenoid:1.10.0     "/usr/bin/selenoid -…"  1 hour ago  Up 1 hour           0.0.0.0:4444->4444/tcp  selenoid

Go to http://localhost:8080/ to see the Selenoid UI dashboard
For having an ability to watch for the running test don't forget to specify "enableVNC": True for capabilities settings

Just before starting a test via command line(pytest) or via IDE go for Selenoid UI dashboard and click on newly
created session link to move to the certain section that display running browser and log messages.

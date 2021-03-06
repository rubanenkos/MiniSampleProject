# This is a template framework to show how to run test using Selenoid


Before running test please install Selenoid using the following commands:
```
$ curl -s https://aerokube.com/cm/bash | bash
$ ./cm selenoid start --vnc
```
*(--vnc - this key is needed to connect to a browser in docker via vnc)*

Then check the the status of Selenoid:
curl http://localhost:4444/status


To run test using Selenoid, please specify the following settings
Go http://localhost:8080/#/capabilities/ and pick the Python for instance.
See the example of settings:
```
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
```

There is the UI dashboard for Selenoid that can be started using the following:
```
$ ./cm selenoid-ui start
```

Finally, it should looks like that:
```
$ docker ps
CONTAINER ID  IMAGE                        COMMAND                 CREATED     STATUS     PORTS                   NAMES
78e1c32fe108  aerokube/selenoid-ui:1.10.0  "/selenoid-ui --sele…"  1 hour ago  Up 1 hour  0.0.0.0:8080->8080/tcp  selenoid-ui
1fa9d850b722  aerokube/selenoid:1.10.0     "/usr/bin/selenoid -…"  1 hour ago  Up 1 hour  0.0.0.0:4444->4444/tcp  selenoid
```

Go to http://localhost:8080/ to see the Selenoid UI dashboard

*Don't forget to specify "enableVNC": True for capabilities settings for having an ability to watch for the running test process*


After starting a test (via the command line (pytest) or via IDE) please go for the Selenoid UI dashboard and click on the newly created 
session link to move to the certain section that displays the running browser and log messages.

P/S Useful article https://4te.me/post/selenium-docker/

[![tor-logo](https://user-images.githubusercontent.com/46316908/134797723-e3b5c0fc-c6d8-49a6-b685-f3d869edf141.png)](https://torproject.org/)

# What is TorWebsite?

A container to host website on Tor hidden service with .onion address. Tor is free software and an open network that helps you defend against traffic analysis, enabling anonymous communication. ".onion" is a special-use top level domain name designating a "hidden service" on the Dark Web, reachable via the Tor network/accessed via the Tor browser.

### Container Image: [View on DockerHub](https://hub.docker.com/r/sandeshy/torwebsite)

# How to use this image

★ **Run container:**

```sh
docker container run -it --name <container_name> sandeshy/torwebsite:latest
```

![container-start-image](https://user-images.githubusercontent.com/46316908/134805153-b13d1602-64f0-4d53-a187-de5c2bc22c2d.png)

> Note: To exit from running container without stopping press ctrl+p+q.

★ **Check your .onion addresss**

```sh
torhost
```

![torhost-cmd-image](https://user-images.githubusercontent.com/46316908/134805221-e11067e8-ec7e-4fc0-bbde-fe99389bac10.png)

★ **Open the address in [tor browser](https://www.torproject.org/download/):**

![tor-browser-image](https://user-images.githubusercontent.com/46316908/134805825-b6b669e0-7880-40ee-9025-6e4c675f6f10.png)

★ **Attach volume, overrides default HTML template:**

```sh
docker container run -it --name <container_name> \
       -v </some/path/on/hostOS>:/var/www/hidden_service \
       sandeshy/torwebsite:latest
```

### Configs:

\* Tor config - /etc/tor/torrc</br> \* Nginx config - /etc/nginx/http.d/nginx.conf</br>

### Logs:

/var/log/nginx

## Gotcha/Q&A

**Will I get new .onion address each time?**</br>
Onion address is generated for each new container, if you are using the same container it won't change ever.

**Are any ports exposed?**</br>
No, tor is running inside container which connects to Network using Virtual Ethernet.

**How much time it takes for website to get live?**</br>
5-8 seconds with normal Internet Speed. If your connectivity is weak, try waiting for few mins till Tor picks some relay as introduction point and adds new entry in Distributed Hash Table (DHT). More info [here](https://tor.stackexchange.com/questions/672/how-do-onion-addresses-exactly-work/674#674).

**Underlying services ?**

```
rc-service tor status
rc-service nginx status
```

## Disclaimer

TorWebsite is created to make hosting website on Tor easy and it's not responsible for any misuse or illegal purposes.

Feel free to discuss any issue or new feature at [GitHub Discussions](https://github.com/3xploitGuy/torwebsite/discussions).

## License

TorWebsite is under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

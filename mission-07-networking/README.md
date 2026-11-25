# Mission 7 — How computers communicate

## 1. Task / objective
Explain common network concepts, check connectivity and DNS lookup behavior, and describe how a browser communicates with a website.

## 2. Work completed
### Network concepts
| Concept | Explanation | Example |
|---|---|---|
| LAN | A network covering a relatively small area. | Home or school network. |
| MAN | A network spanning a city or large campus area. | A city-wide institutional network. |
| WAN | A network covering large geographic areas and connecting smaller networks. | The Internet. |
| DNS | A distributed naming system that looks up records such as addresses for domain names. | A browser looks up the address records for a site. |
| Router | A device that forwards packets between networks. | A home router connects a local network to an internet provider. |
| Protocol | Agreed rules and message formats used for communication. | HTTPS uses HTTP over a secure transport. |
| Packet switching | Data is divided into packets that can be forwarded across shared networks. | IP packets carry pieces of a request or response. |
| Client/server | A client requests a service; a server responds to that request. | A browser requests a web page from a web server. |

### Network observations
Commands on macOS and Linux systems:

```bash
ping -c 1 github.com
nslookup github.com
```

`ping` sends a small connectivity probe and reports whether a response arrives. A reply is evidence that the tested host responded at that moment. 
`nslookup` asks DNS for records associated with a name.

| Check | Observation to record |
|---|---|
| Connectivity test | 1 packet transmitted, 1 packet received. |
| DNS lookup | DNS lookup for github.com. gave Address: 4.187.247.160 |

### What happens when you open a website?
1. The browser (the client) parses the URL and determines the destination host and requested resource.
2. If it does not already have a usable DNS answer cached, it asks DNS to resolve the host name.
3. The computer sends packets through its local network and router toward the destination network.
4. The client establishes a transport connection (commonly TCP, or QUIC) and, for HTTPS, negotiates secure TLS as applicable.
5. The browser sends an HTTP request using the protocol's defined message format.
6. The server processes the request and returns an HTTP response containing a status and page data.
7. The browser interprets the response and displays the page; additional resources may trigger further requests.

## 3. Commands / tools used
| Command or tool | Purpose |
|---|---|
| `ping` | Probe whether a host responds to a small network test. |
| `nslookup` | Query DNS records for a domain name. |
| Web browser | Observe the client side of a website request. |

Use only the tools you actually ran and report actual outcomes.

## 4. My understanding
Networking moves data between devices using layered protocols. DNS helps a client find an address for a human-readable name; routers forward packets toward other networks; and client/server protocols describe how requests and responses are exchanged. Connectivity tests have limits, so a failed ping is not a complete diagnosis.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- This README — concept table and example website-request sequence.
- A screenshot of connectivity and DNS checks in [evidence/](evidence/).

## 8. Commit details
- Commit message: `mission-07: Explain networking concepts and website communication`


# Computer network and internet
## Basic Terminologies of Computer Networks

### Network
- Interconnection of a set of devices capable of communicating

### IP Address (Internet Protocol)
#### Theory
- The identify of the devices.
- Devices can identify another devices by using IPv4 or IPv6 ( as shipper)
#### IP dynamic
- Auto alternating IP addresses by DHCP servers.
- ISP matching for each time customers connect.
- Cause Ip is really rarely so that this helps alot.
#### IP Static
- Web or Mail addresses, so that when many customers connect its become stable and can not be distracted.
- Add another routers.
- Can connect which far devices.
- Transfer port for permanent devices.
- Sharing the printers through the camera IP
### Mac Address
#### Theory
- Media Access Control.
- Unique, 12 digits from hexadecimal.
- Contain number and alphanumeric characters.
- 2 pack.
- First 6 digits talk about the manufacturer.
- Second 6 digits talk about the physical address (Hardware address).
#### Distinguishing From IP
- Cannot be alternative
- Use to detect the device in lieu of detect the location of the device as IP do.
- Ip: the address of the house, deine the address of the device.
- Mac: the name of the house owner, use in each step from the first device to the end through many MAC addresses.

### Nodes:
#### Hub: 
- Can be use to connect many different devices and share the same proccesing data (Frame).
- Use the same LAN network.
- Something mistake takeplace make the network conflict (cause hub can't know which is the right port to connect)
- Half duplex connection. (1 direction)
- Activate in a physical layer.
- Units: bits or electronic signals
- No data filtering.
- Not secure and Wasting bandwidth
#### Switch:
- Function same as hub, but it know which port to connect so that data can transfer more exactly, and rarely make the network conflict.
- Full duplex connection. (2 direction)
- Activate in data conection layer.
- Units: packets or frames.
- With data filtering.
#### Router:
- Transfer the data from this network to the others.
- Data to router it will checking the IP if not in its network it will connect to the others.
- Router is created by a switch and a hub.
#### Modem:
- Bring the internet into your house and bussiness.
- Establishes and maintains a dedicated connection to your internet server provider.
- Computer read digital signal while signals out on the internet is analog, so that modem can be used to demonulate the analog signal and also monulate the digital signal.
- Router connects the divices to the modem, so that they can transfer data to the internet.
- Modem is sometime integration together like the wifi...
#### Repeater 
- Regenerates a weak or corrupted signal over the same network,
- Extending its transmission length.  
- Amplify the signal.
- Regenerate the signal.
- Maintaining the original signal strength. 
- A repeater is a 2-port device.
### Topology
#### Star topology:
- Divices connect dirrectly to the switchs.
- 1 stop uneffected to the system. 
- Switch stop go down the system.
#### Ring Topology:
- Each devices connected to the others.
- Sent the data around the ring.
- Old rarely use today.
- Single break all go down.
#### Bus Topology:
- Old like ring and rarely use.
- The wires connected to the devices and 2 terminaters.
#### Mesh Topology:
- All  devices connected, so that one fail others still connect.(Internet is the application of this topology)
#### Infrastructure:
- Wireless and wire devices connected.
#### Ad hoc topology:
- Just wireless devices connected.
#### Wireless mesh topology:
- The combine of infrastructure and mesh.
- Use router to connect the main router to wifi transfer to the other rooms. 
### DNS
- Resolution the IP address to a name that similar for human(facebook and 174.82.112)
### Firewall
- Access control list
- Distract the ip


## Types of Enterprise Computer Networks
### LAN (Local Area Network)
- Covers a small area.
- Little devices
### WAN (Wide Area Network)
- Large area, large geographic area, such as a city, country, or even the entire world
- WANs are used to connect LANs together and are typically used for long-distance communication.
### Cloud Networks: 
- A Wide Area Network (WAN) they can be hosted on public or private cloud service providers.
- Available if there is a demand.
- Consist of Virtual Routers, Firewalls, etc.

## Types of Computer Network Architecture:
### Client-Server Architecture:
- Nodes can be Servers or Clients.
- The server node can manage the Client Node Behaviour.
### Peer-to-Peer Architecture:
- Not any concept of a Central Server. 
- Each device is free for working as either client or server.
## OSI Model (Open Systems Interconnection):
- It is a reference model that specifies standards for communications protocols and also the functionalities of each layer. The OSI has been developed by the International Organization For Standardization and it is 7 layer architecture. Each layer of OSI has different functions and each layer has to follow different protocols. The 7 layers are as follows: 
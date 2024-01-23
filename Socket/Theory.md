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
### Theory:
- A reference model that specifies standards for communications protocols and also the functionalities of each layer. 
- Developed by the International Organization For Standardization 
- 7 layer architecture.
- Each layer has different functions 
- Each layer has to follow different protocols. 
- Separate and independence
- Each layer cannot be effected if any other be alternative.
- Can separate and cancel went uncrucial.
- Guaranteed to connect with other network.
### [Layers](https://youtube.com/watch?v=8H0USHO8g-g):
#### Physical Layer:
- Bottom-most layer.
- Consists of networks components (power plugs, connectors, receivers, cable types, etc.) 
- Converts data to electrical, radio or optical pulses bit data form.
- Through the cab or radio.
#### Data link Layer:
##### Frame Synchronization: 
- Data is divided into frames for transmission. 
- The Data Link Layer adds a header to each frame to define the start and end of the frame.

##### Physical Addressing: 
- If frames are to be distributed to different systems on the network, the Data Link Layer adds a header to the frame to define the physical address of the sender or receiver of the frame.

##### Flow Control: 
- If the rate at which data is taken by the receiver is less than the rate produced in the sender, the Data Link Layer imposes a flow control mechanism to prevent overwhelming the receiver.

##### Error Control:
- The Data Link Layer adds reliability to the Physical Layer by adding mechanisms to detect and retransmit damaged or lost frames. It also prevents duplication of frames using an error control mechanism.

##### Access Control:
- When two or more devices are connected to the same link, data link layer protocols are necessary to determine which device has control over the link at any given time.

#### Network Layer:
- The network layer is responsible for routing packets between networks.
- It determines the best path to send data based on network conditions, such as available bandwidth and latency. 
- The network layer also handles IP addressing, which allows devices on different networks to communicate with each other.

#### Transport Layer:
- The transport layer is responsible for ensuring that data is delivered reliably and in the correct order. 
- It provides end-to-end communication between two applications, ensuring that data is delivered without errors and in a timely manner. 
- The transport layer also handles connection establishment, flow control, and error detection/correction.
  
#### Session Layer:
- The session layer is responsible for managing the creation, maintenance, and termination of sessions between two applications. 
- This includes establishing a connection, managing the flow of data, and ensuring that the session is closed properly when it is no longer needed.
  
#### Presentation Layer:
- The presentation layer is responsible for converting data into a format that can be understood by the application it is being sent to. 
- This includes encoding data into a format that can be sent over a network, such as ASCII or binary, and decoding data into a format that can be used by an application.

#### Application Layer:
- The application layer is responsible for providing the services that end users want or need. 
- Examples of application layer services include email, web browsing, and FTP. 
- The application layer is also responsible for interpreting user requests and sending them to the appropriate service or device.T
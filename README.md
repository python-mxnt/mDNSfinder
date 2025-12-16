# mDNSfinder

mDNSfinder is a simple Python script that waits for a device on your local network to become reachable using its hostname and mDNS domain (e.g., `.local`) and prints its IP address once online. It's perfect for finding devices like Raspberry Pi or other computers that support mDNS.

## Features

- Continuously checks if a device is online using its hostname and mDNS domain.
- Prints the device's IP address once it is reachable.
- Cross-platform ping support (Windows, Linux, macOS).
- Easy to use and lightweight.

## Requirements

- Python 3.x
- Devices on the same local network supporting mDNS.
- Optional: Bonjour or Avahi for `.local` domains on Windows/Linux if needed.

## Usage

1. Clone the repository:

```
git clone https://github.com/python-mxnt/mDNSfinder.git
cd mDNSfinder
```

2. Run the script:

```
python mDNSfinder.py
```

3. Enter the hostname and mDNS domain when prompted:

```
Enter the hostname (e.g., 'pi5'): pi5
Enter the mDNS domain (e.g., '.local'): .local
```

4. The script will wait until the device is reachable and then display:

```
Computer is online!
Hostname : pi5.local
IP       : 192.168.1.42
```

## How It Works

- The script builds the full hostname by combining the user input hostname and mDNS domain.
- It continuously tries to resolve the hostname to an IP address.
- Once an IP is found, it sends a single ping to check if the device is online.
- The loop continues every 2 seconds until the device responds.

## License

This project is open-source and available under the MIT License.

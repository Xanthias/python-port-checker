# Python Port Checker

**Version 1.0 | Python | Cybersecurity | Networking**

A beginner-friendly TCP port checker built with Python. This project was developed as a hands-on introduction to networking fundamentals, socket programming, and ethical cybersecurity testing.

## About the Project

Python Port Checker is a simple cybersecurity tool that attempts to establish a TCP connection to a specified port on the local computer.

The program uses Python's built-in `socket` library to determine whether a TCP connection can be established.

This project is part of my journey learning Python programming, networking, and cybersecurity tool development.

## Features

- TCP port connectivity checking
- IPv4 networking support
- Configurable target port
- One-second connection timeout
- Open/closed connection status displayed in the terminal
- Lightweight and beginner-friendly
- No external Python libraries required

## Technologies Used

- **Python 3** — Programming language
- **Socket Library** — TCP network communication
- **TCP/IP** — Networking protocol
- **Visual Studio Code** — Development environment

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/python-port-checker.git
```

Replace `YOUR_USERNAME` with your GitHub username.

**2. Navigate to the project directory**

```bash
cd python-port-checker
```

**3. Run the program**

```bash
python port_checker.py
```

No additional dependencies are required.

## Configuration

The program currently uses the IPv4 loopback address to test services running on the local computer.

```python
target_ip = "127.0.0.1"
target_port = 8765
```

- `127.0.0.1` is the localhost loopback address.
- `8765` is the TCP port being checked.

The port number can be modified directly in the Python script.

## Example Output

When the connection succeeds:

```text
Port 8765 is open
```

When the connection fails:

```text
Port 8765 is closed
```

**Note:** The current version reports unsuccessful connections as closed. A failed connection does not always mean a port is closed; network restrictions and timeouts can also affect results.

## Testing

The program was tested using Python's built-in HTTP server.

**Step 1 — Start a local server**

Open a terminal and execute:

```bash
python -m http.server 8765 --bind 127.0.0.1
```

**Step 2 — Run the port checker**

Open a second terminal and execute:

```bash
python port_checker.py
```

Expected output:

```text
Port 8765 is open
```

**Step 3 — Stop the server**

Return to the server terminal and press `Ctrl + C`.

Run the port checker again.

Expected output:

```text
Port 8765 is closed
```

Both tests were successfully completed during development.

## What I Learned

This project helped me gain hands-on experience with:

- IPv4 addressing and localhost
- TCP ports and network services
- Python socket programming
- Establishing TCP connections
- Handling connection results
- Connection timeouts
- Conditional statements
- Basic network troubleshooting
- Testing Python networking tools

## Current Limitations

Version 1.0 is intentionally designed as a simple starter project.

- Checks one port at a time
- Requires manual port configuration
- Does not perform automated port scanning
- Does not identify running services
- Does not include comprehensive exception handling
- Does not distinguish all network error conditions

## Responsible Use

This project was created for educational purposes and authorized cybersecurity testing.

The default configuration uses the localhost loopback address (`127.0.0.1`).

Only test devices and networks that you own or have explicit permission to assess.

## Version History

### v1.0 — Initial Release

- Implemented TCP socket creation
- Added IPv4 loopback connectivity testing
- Added configurable TCP port
- Implemented one-second socket timeout
- Added connection status reporting
- Added proper socket closure
- Verified successful and unsuccessful local TCP connections

## License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

## Author

Created as part of my hands-on learning journey in Python programming and cybersecurity.

This project represents my first step toward developing my own cybersecurity tools.

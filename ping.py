import os
import subprocess
import re

# Function to validate an IP address
def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

# Function to ping a host
def ping(host):
    return subprocess.call(["ping", host])

# Main loop
def main():
    while True:
        try:
            host = input("Enter the IP address to ping (or type 'exit' to quit): ")

            if host == "exit":
                print("Exiting...")
                break

            if not is_valid_ip(host):
                print("Invalid IP address. Please enter a valid IP address.\n")
                continue

            print(f"\nPinging {host}...\n")

            try:
                if ping(host) == 0:
                    print(f"{host} is reachable.")
                else:
                    print(f"{host} is unreachable.")
            except KeyboardInterrupt:
                print("\nPing interrupted by user. Resuming...\n")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Resuming...\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Resuming...\n")

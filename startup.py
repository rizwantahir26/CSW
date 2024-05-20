from csw import Authentication, CLI, Config, Interface, VLAN
import getpass

def main():
    # Initialize components
    auth = Authentication()
    config = Config()
    interface = Interface()
    vlan = VLAN()
    cli = CLI(config, interface, vlan)

    # Authenticate the user
    print("Cisco Packet Tracer Simulation")
    print("Please authenticate to access the CLI.")
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')

    if auth.authenticate(username, password):
        print("Authentication successful.\n")
        cli.start()
    else:
        print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()

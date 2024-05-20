class Switch:
    def __init__(self, hostname="Switch"):
        self.hostname = hostname
        self.interfaces = {}
        self.vlans = {}
        self.running_config = ""

    def set_hostname(self, hostname):
        self.hostname = hostname

    def add_interface(self, name, interface):
        self.interfaces[name] = interface

    def get_interface(self, name):
        return self.interfaces.get(name)

    def add_vlan(self, vlan_id, vlan):
        self.vlans[vlan_id] = vlan

    def get_vlan(self, vlan_id):
        return self.vlans.get(vlan_id)

    def show_running_config(self):
        config = f"hostname {self.hostname}\n"
        for iface_name, iface in self.interfaces.items():
            config += iface.get_config()
        for vlan_id, vlan in self.vlans.items():
            config += vlan.get_config()
        return config

    def __str__(self):
        return self.show_running_config()


class Interface:
    def __init__(self, name):
        self.name = name
        self.ip_address = None
        self.status = "administratively down"
        self.protocol = "down"

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def set_status(self, status):
        self.status = status

    def set_protocol(self, protocol):
        self.protocol = protocol

    def get_config(self):
        config = f"interface {self.name}\n"
        if self.ip_address:
            config += f" ip address {self.ip_address}\n"
        config += f" {self.status}\n"
        config += f" {self.protocol}\n"
        return config


class VLAN:
    def __init__(self, vlan_id, name):
        self.vlan_id = vlan_id
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_config(self):
        return f"vlan {self.vlan_id}\n name {self.name}\n"


# Example usage
if __name__ == "__main__":
    # Create a switch
    switch = Switch(hostname="SimulatedSwitch")

    # Add interfaces
    interface1 = Interface(name="FastEthernet0/1")
    interface1.set_ip_address("192.168.1.1")
    interface1.set_status("up")
    interface1.set_protocol("up")
    switch.add_interface(name="FastEthernet0/1", interface=interface1)

    interface2 = Interface(name="FastEthernet0/2")
    switch.add_interface(name="FastEthernet0/2", interface=interface2)

    # Add VLANs
    vlan10 = VLAN(vlan_id=10, name="VLAN0010")
    switch.add_vlan(vlan_id=10, vlan=vlan10)

    vlan20 = VLAN(vlan_id=20, name="VLAN0020")
    switch.add_vlan(vlan_id=20, vlan=vlan20)

    # Show running config
    print(switch)

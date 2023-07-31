#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, AzurermBackend
from imports.azurerm import (
    provider,
    resource_group,
    virtual_desktop_workspace,
    virtual_desktop_host_pool,
    virtual_desktop_application_group,
    network_interface,
    windows_virtual_machine,
    virtual_machine_extension,
)


class ItsVirtualDesktopStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Initialize the Azure provider
        provider.AzurermProvider(self, "azure", features={})

        # Create resource group for the Azure Virtual Desktop resources
        avd_resource_group = resource_group.ResourceGroup(
            self,
            "azure-virtual-desktop",
            name="azure-virtual-desktop",
            location="westus2",
        )

        # Create a virtual network interface for virtual machine
        avd_vm_nic = network_interface.NetworkInterface(
            self,
            "avd-vm-nic-id",
            name="avd-nic",
            location="westus2",
            resource_group_name=avd_resource_group.name,
            ip_configuration=[
                {
                    "name": "avd-ip-config",
                    "subnetId": avd_virtual_subnet.id,
                    "privateIpAddressAllocation": "Dynamic",  # why no snake case here my guy?
                }
            ],
        )

        # Loop through vm_count and create a windows virtual machine
        avd_windows_vm = windows_virtual_machine.WindowsVirtualMachine(
            self,
            "windows-vm",
            name=f"azure-virtual-desktop-vm",
            computer_name="mason-avd",
            location="westus2",
            resource_group_name=avd_resource_group.name,
            size="Standard_D2s_v3",
            os_disk={
                "storage_account_type": "StandardSSD_LRS",
                "disk_size_gb": 128,
                "caching": "ReadWrite",
            },
            network_interface_ids=[avd_vm_nic.id],
            source_image_reference={
                "publisher": "MicrosoftWindowsDesktop",
                "offer": "windows-11",
                "sku": "win11-21h2-pro",
                "version": "22000.2176.230707",
            },
            admin_username="Tom",
            admin_password="Bombadil!",  # I know this is bad, this is a proof of concept
        )

        # Create an Azure Virtual Desktop Workspace
        avd_workspace = virtual_desktop_workspace.VirtualDesktopWorkspace(
            self,
            "workspace",
            name="avd-workspace",
            location="westus2",
            resource_group_name=avd_resource_group.name,
        )

        # Create an Azure Virtual Desktop Host Pool
        avd_host_pool = virtual_desktop_host_pool.VirtualDesktopHostPool(
            self,
            "avd-host-pool",
            name="avd-host-pool",
            location="westus2",
            resource_group_name=avd_resource_group.name,
            friendly_name="Virtual Desktop Host",
            type="Personal",
            load_balancer_type="Persistent",
            start_vm_on_connect=True,
            validate_environment=True,
        )

        # Create an Azure Virtual Desktop Application Group
        avd_application_group = (
            virtual_desktop_application_group.VirtualDesktopApplicationGroup(
                self,
                "application-group",
                name="avd-application-group",
                type="Desktop",
                default_desktop_display_name="azure-vd",
                location="westus2",
                resource_group_name=avd_resource_group.name,
                host_pool_id=avd_host_pool.id,
                friendly_name="AVD Application Group",
            )
        )


app = App()
stack = ItsVirtualDesktopStack(app, "its_azure_vd")
AzurermBackend(
    stack,
    resource_group_name="",
    storage_account_name="",
    container_name="",
    key="",
)

app.synth()

# TODO
# Need to completely refactor AVD referencing existing networking stack
# Fix the AzurermBackend

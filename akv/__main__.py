import pulumi
from pulumi import ResourceOptions
from pulumi_azure.core import ResourceGroup
from pulumi_azure import keyvault

tenant = <tenant here>

resource_group = ResourceGroup("acl-rg", name="acl-rg", location="westus")

trusted_networkds = <ip addresses here>

acls = {"bypass": "AzureServices", "defaultAction": "Deny", "ipRules": trusted_networkds }

vault = keyvault.KeyVault("akv", opts=None, access_policies=None, enabled_for_deployment=None, 
                        enabled_for_disk_encryption=None, enabled_for_template_deployment=None, 
                        location="westus", name="acl-akv", network_acls=acls, resource_group_name=resource_group.name, 
                        sku=None, sku_name="standard", tags=None, tenant_id=tenant, __props__=None, 
                        __name__=None, __opts__=None)

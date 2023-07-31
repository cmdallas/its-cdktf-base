# Introduction 
A base package which defines all of our Terraform CDK constructs for infrastructure as code in Azure.  Each directory will contain

# Getting Started
### 1.	Prerequisites
-   [Python 3](https://www.python.org/downloads/)
-   [Pipenv](https://pipenv.pypa.io/en/latest/installation/#installing-pipenv)
-   [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
-   [cdktf-cli](https://developer.hashicorp.com/terraform/cdktf/cli-reference/cli-configuration)

### 2.	CDKTF references
- [Terraform - Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Github - CDKTF Azurerm Provider](https://github.com/cdktf/cdktf-provider-azurerm)

### 3. Customer Account Setup
Customer account bootstrapping is done with the following shell scripts for now:
-   `/bin/bootstrap_customer_account.sh`
-   `/bin/bootstrap_customer_account_service_principal.sh`

This bootstrap only needs to be done once. It creates the necessary Azure resources for Terraform CDK to operate:

-   A storage account to store the Terraform state file (.tfstate) which serves as the source of truth for deployed resources
-   A storage container where the .tfstate file will be saved
-   A storage account access key for Terraform to access the state file
-   A service principal that Terraform CDK can use to authenticate and manage resources in the Azure account

Completing this bootstrap gives Terraform CDK the permissions and state storage it requires to deploy and manage infrastructure in the Azure subscription. Refer to the [wiki](https://dev.azure.com/itsc-dev/its_cdktf_base/_wiki/wikis/its_cdktf_base.wiki/3/Development-and-Operations-(DevOps)-Philosophy-Practice#) for details on performing this one-time setup process.


# Build, Test, Synthesize & Deploy
- Testing resource synthesis and deployment is done using the [cdktf-cli](https://developer.hashicorp.com/terraform/cdktf/cli-reference/commands)
- You can run `cat help` inside this package to learn more
- You can also run `cdktf -help` for further guidance

# Contribute
TODO: Explain how other users and developers can contribute to make your code better.

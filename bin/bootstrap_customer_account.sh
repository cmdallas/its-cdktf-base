#!/bin/bash

customer="<customer_abbreviation>"
region="westus2"
subscription_id="<subscriptionid>"

resource_group_name="tfstate-$customer"
storage_account_name="tfstate$customer"
container_name="tfstate-$customer"
service_principal_name="its-cdktf-sp"


# Create resource group
az group create --name "$resource_group_name" --location "$region"

# Create storage account
az storage account create --resource-group "$resource_group_name" --name "$storage_account_name" --sku Standard_LRS --location "$region" --encryption-services blob

# Create blob container
az storage container create --name "$container_name" --account-name "$storage_account_name" --public-access off

# Create cdktf service principal and capture the output in a variable
sp_output=$(az ad sp create-for-rbac --name "$service_principal_name" --role Contributor --scopes "/subscriptions/$subscription_id")

# Extract the secret key from the output
secret_key=$(echo "$sp_output" | jq -r .password)

# Create key vault for service principal secret
az keyvault create --name "$service_principal_name" --resource-group "$resource_group_name" --location "$region"

# Set the service principal secret in the key vault
az keyvault secret set --vault-name "$service_principal_name" --name "$service_principal_name" --value "$secret_key"

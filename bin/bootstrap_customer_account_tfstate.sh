#!/bin/bash

CUSTOMER=<customer_acronym>
REGION=westus2

RESOURCE_GROUP_NAME=tfstate-$CUSTOMER
STORAGE_ACCOUNT_NAME=tfstate$CUSTOMER
CONTAINER_NAME=tfstate-$CUSTOMER


# Create resource group
az group create --name $RESOURCE_GROUP_NAME --location $REGION

# Create storage account
az storage account create --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --location $REGION --encryption-services blob

# Create blob container
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME --public-access off

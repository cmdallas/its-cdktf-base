#!/bin/bash

# Create a service principal with Contributor permissions to create resources in customer account
# Don't forget to update <subscription_id> with a valid customer subscription id from their tenant
az ad sp create-for-rbac --name its-cdktf-service-principal --role Contributor --scopes /subscriptions/<subscription_id>

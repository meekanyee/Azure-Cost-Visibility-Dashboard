terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}

# Dev resource group
resource "azurerm_resource_group" "dev" {
  name     = var.dev_resource_group_name
  location = var.location

  tags = {
    environment = "dev"
    project     = "cost-dashboard"
    owner       = var.owner
    cost-center = "engineering"
  }
}

# Prod resource group
resource "azurerm_resource_group" "prod" {
  name     = var.prod_resource_group_name
  location = var.location

  tags = {
    environment = "prod"
    project     = "cost-dashboard"
    owner       = var.owner
    cost-center = "engineering"
  }
}

# Dev storage account
resource "azurerm_storage_account" "dev" {
  name                     = var.dev_storage_account_name
  resource_group_name      = azurerm_resource_group.dev.name
  location                 = azurerm_resource_group.dev.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "dev"
    project     = "cost-dashboard"
    owner       = var.owner
    cost-center = "engineering"
  }
}

# Prod storage account
resource "azurerm_storage_account" "prod" {
  name                     = var.prod_storage_account_name
  resource_group_name      = azurerm_resource_group.prod.name
  location                 = azurerm_resource_group.prod.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "prod"
    project     = "cost-dashboard"
    owner       = var.owner
    cost-center = "engineering"
  }
}
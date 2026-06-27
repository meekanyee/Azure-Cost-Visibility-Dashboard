variable "location" {
  description = "Azure region for all resources"
  type        = string
  default     = "East US"
}

variable "owner" {
  description = "Owner tag applied to all resources"
  type        = string
}

variable "dev_resource_group_name" {
  description = "Name of the dev resource group"
  type        = string
  default     = "rg-cost-dashboard-dev"
}

variable "prod_resource_group_name" {
  description = "Name of the prod resource group"
  type        = string
  default     = "rg-cost-dashboard-prod"
}

variable "dev_storage_account_name" {
  description = "Name of the dev storage account (must be globally unique, lowercase, 3-24 chars)"
  type        = string
}

variable "prod_storage_account_name" {
  description = "Name of the prod storage account (must be globally unique, lowercase, 3-24 chars)"
  type        = string
}
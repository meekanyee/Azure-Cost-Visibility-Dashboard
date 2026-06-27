output "dev_resource_group_name" {
  description = "Name of the dev resource group"
  value       = azurerm_resource_group.dev.name
}

output "prod_resource_group_name" {
  description = "Name of the prod resource group"
  value       = azurerm_resource_group.prod.name
}

output "dev_storage_account_name" {
  description = "Name of the dev storage account"
  value       = azurerm_storage_account.dev.name
}

output "prod_storage_account_name" {
  description = "Name of the prod storage account"
  value       = azurerm_storage_account.prod.name
}

output "dev_storage_account_id" {
  description = "Resource ID of the dev storage account"
  value       = azurerm_storage_account.dev.id
}

output "prod_storage_account_id" {
  description = "Resource ID of the prod storage account"
  value       = azurerm_storage_account.prod.id
}
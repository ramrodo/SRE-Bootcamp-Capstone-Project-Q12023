variable "app_name" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "health_check_path" {
  type = string
}

variable "security_group_id" {
  type = string
}

variable "subnets" {
  default = "{}"
}

variable "bucket_logs" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "app_name" {
  type = string
}

variable "tags" {
  type        = map(any)
  default     = {}
  description = "A set of tags to attach to the created resources"
}

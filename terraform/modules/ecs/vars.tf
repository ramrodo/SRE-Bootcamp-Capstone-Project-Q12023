variable "tags" {
  type        = map(any)
  default     = {}
  description = "A set of tags to attach to the created resources"
}

variable "app_name" {
  type = string
}

variable "ecr_repository" {
  type = string
}

variable "ecr_image_tag" {
  type = string
}

variable "network_mode" {
  type    = string
  default = "awsvpc"
}

variable "requires_compatibilities" {
  type    = string
  default = "FARGATE"
}

variable "taskcpuunit" {
  type    = number
  default = 1024
}

variable "taskmemoryM" {
  type    = number
  default = 3072
}

variable "awslogs_region" {
  type    = string
  default = "us-west-2"
}

variable "awslogs_stream_prefix" {
  type = string
}

variable "container_port" {
  type = number
}

variable "host_port" {
  type = number
}

variable "protocol" {
  type = string
}

variable "desired_count" {
  type    = number
  default = 1
}

variable "launch_type" {
  type    = string
  default = "FARGATE"
}

variable "subnets" {
  default = "{}"
}

variable "vpc_id" {
  type = string
}

variable "target_group_arn" {
  type = string
}

variable "security_group_id" {
  type = string
}

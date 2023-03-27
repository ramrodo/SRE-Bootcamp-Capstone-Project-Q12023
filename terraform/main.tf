locals {
  account_id  = data.aws_caller_identity.current.account_id
  region      = "us-west-2"
  env         = "dev"
  app_name    = "capstoneAPItf"

  default_tags = {
    env         = local.env
  }

  ecs_tags = merge(local.default_tags, {
    createdby = "rodomar@outlook.com"
    }
  )

  ecr_repository = "capstone-api"
  ecr_image_tag  = "deliver-final"

  service_port          = 80
  protocol              = "HTTP"
  subnets               = ["subnet-34c72d4c", "subnet-fa4156b1", "subnet-0d4f8a50", "subnet-be295595"]
  vpc_id                = "vpc-b272ebca"
}

module "ecs" {
  source         = "./modules/ecs"
  app_name       = local.app_name
  tags           = local.ecs_tags
  ecr_repository = local.ecr_repository
  ecr_image_tag  = local.ecr_image_tag

  awslogs_stream_prefix = "aws-ecs-${local.app_name}"
  container_port        = local.service_port
  host_port             = local.service_port
  protocol              = local.protocol
  subnets               = local.subnets
  vpc_id                = local.vpc_id
}

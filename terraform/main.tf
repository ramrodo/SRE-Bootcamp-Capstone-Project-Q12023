locals {
  account_id = data.aws_caller_identity.current.account_id
  region     = "us-west-2"
  env        = "dev"
  app_name   = "capstoneAPItf"

  default_tags = {
    env = local.env
  }

  tags = merge(local.default_tags, {
    created_by = "rodomar@outlook.com"
    }
  )

  ecr_repository = "capstone-api"
  ecr_image_tag  = "latest" # Update this "-v" key & value. From workflow where I'm building the Docker

  service_port = 80
  protocol     = "http"
  subnets      = ["subnet-34c72d4c", "subnet-fa4156b1", "subnet-0d4f8a50", "subnet-be295595"]
  bucket_logs  = "capstone-api"
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "${local.app_name}-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["${local.region}a", "${local.region}b"]
  public_subnets  = ["10.0.1.0/24", "10.0.3.0/24"]
  private_subnets = ["10.0.2.0/24", "10.0.4.0/24"]

  enable_dns_hostnames = true
  enable_dns_support   = true

  # Default security group - ingress/egress rules cleared to deny all
  manage_default_security_group  = false
  default_security_group_ingress = [{}]
  default_security_group_egress  = [{}]
}

module "sg" {
  source = "./modules/sg"

  vpc_id   = module.vpc.vpc_id
  app_name = local.app_name
  tags     = local.tags

  depends_on = [
    module.vpc
  ]
}

module "alb" {
  source = "./modules/alb"

  vpc_id   = module.vpc.vpc_id
  app_name = local.app_name

  bucket_logs = local.bucket_logs

  # Load Balancer Config
  health_check_path = "/"
  security_group_id = module.sg.security_group_id
  subnets           = local.subnets

  depends_on = [
    module.sg,
    module.vpc
  ]
}

module "ecs" {
  source = "./modules/ecs"

  app_name       = local.app_name
  tags           = local.tags
  ecr_repository = local.ecr_repository
  ecr_image_tag  = local.ecr_image_tag

  awslogs_stream_prefix = "aws-ecs-${local.app_name}"
  container_port        = local.service_port
  host_port             = local.service_port
  protocol              = local.protocol
  subnets               = local.subnets
  vpc_id                = module.vpc.vpc_id
  target_group_arn      = module.alb.target_group_arn

  security_group_id = module.sg.security_group_id

  depends_on = [
    module.sg,
    module.alb,
    module.vpc
  ]
}

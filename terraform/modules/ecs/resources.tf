resource "aws_ecs_cluster" "ecs_cluster" {
  name = "${var.app_name}-ECSCluster"
  tags = var.tags
}

resource "aws_cloudwatch_log_group" "ecs_container_cloudwatch_loggroup" {
  name              = "${var.app_name}-ECS-CW-loggroup"
  retention_in_days = 30
  tags              = var.tags
}

data "aws_ecr_repository" "ecr_repository" {
  name = var.ecr_repository
}

resource "aws_ecs_task_definition" "ecs_task_definition" {
  family                   = "${var.app_name}-ECSTask"
  task_role_arn            = aws_iam_role.task_role.arn
  execution_role_arn       = aws_iam_role.exe_role.arn
  network_mode             = var.network_mode
  requires_compatibilities = [var.requires_compatibilities]
  cpu                      = var.taskcpuunit
  memory                   = var.taskmemoryM

  container_definitions = templatefile("${path.module}/container_definitions.tftpl", {
    awslogs_group         = jsonencode(aws_cloudwatch_log_group.ecs_container_cloudwatch_loggroup.name)
    awslogs_region        = jsonencode(var.awslogs_region)
    awslogs_stream_prefix = jsonencode(var.awslogs_stream_prefix)
    image                 = format("%s:%s", data.aws_ecr_repository.ecr_repository.repository_url, var.ecr_image_tag)
    app_name              = jsonencode(var.app_name)
    container_port        = jsonencode(var.container_port)
    host_port             = jsonencode(var.host_port)
    protocol              = jsonencode(var.protocol)
  })

  tags = var.tags
}

resource "aws_security_group" "ecs_sg" {
  vpc_id = var.vpc_id

  ingress {
    description     = "https whitelisted tcp access"
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
  }

  egress {
    description = "total outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
  tags = var.tags
}

resource "aws_ecs_service" "ecs_service" {
  name            = var.app_name
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.ecs_task_definition.arn
  desired_count   = var.desired_count
  launch_type     = var.launch_type

  network_configuration {
    security_groups  = [aws_security_group.ecs_sg.id]
    subnets          = var.subnets
    assign_public_ip = false
  }

  tags = var.tags
}

# Define the IAM role for task and exe

data "aws_iam_policy_document" "exe_role" {
  source_policy_documents = [file("${path.module}/ecs_exe_role.json")]
}

data "aws_iam_policy_document" "task_role" {
  source_policy_documents = [file("${path.module}/ecs_task_role.json")]
}

resource "aws_iam_role_policy" "exe_policy" {
  name = "${var.app_name}-exe-policy"
  role = aws_iam_role.exe_role.id

  policy = data.aws_iam_policy_document.exe_role.json
}

resource "aws_iam_role_policy" "task_policy" {
  name = "${var.app_name}-task-policy"
  role = aws_iam_role.task_role.id

  policy = data.aws_iam_policy_document.task_role.json
}

resource "aws_iam_role" "exe_role" {
  name = "${var.app_name}-exe-role"
  path = "/"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

  tags = var.tags
}

resource "aws_iam_role" "task_role" {
  name = "${var.app_name}-task-role"
  path = "/"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

  tags = var.tags
}

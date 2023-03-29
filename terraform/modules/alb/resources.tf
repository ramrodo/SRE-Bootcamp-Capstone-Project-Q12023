resource "aws_lb_target_group" "target_group" {
  name     = "${var.app_name}-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = var.vpc_id

  load_balancing_algorithm_type = "round_robin"
  slow_start                    = 30 # 30 seconds
  target_type                   = "ip"
  ip_address_type               = "ipv4"

  health_check {
    enabled             = true
    healthy_threshold   = 2
    interval            = 30 # 30 seconds
    matcher             = 200
    path                = var.health_check_path
    port                = "traffic-port"
    timeout             = 15 # 15 seconds
    unhealthy_threshold = 3
  }
}

resource "aws_lb" "load_balancer" {
  name               = "${var.app_name}-load-balancer"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [var.security_group_id]
  subnets            = var.subnets

  enable_deletion_protection = false

  enable_http2 = true

  access_logs {
    bucket  = var.bucket_logs
    prefix  = "test-alb"
    enabled = true
  }
}

resource "aws_lb_listener" "albTargetListener" {
  load_balancer_arn = aws_lb.load_balancer.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn
  }
}

# outputs
output "target_group_arn" {
  value = aws_lb_target_group.target_group.arn
}

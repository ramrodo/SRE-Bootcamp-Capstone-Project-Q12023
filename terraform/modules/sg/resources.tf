resource "aws_security_group" "security_group" {
  name        = var.app_name
  description = "Allow HTTP inbound and outbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow http incoming ipv4"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  ingress {
    description = "Allow RDS DB"
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"
    ]
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

# outputs
output "security_group_id" {
  value = aws_security_group.security_group.id
}

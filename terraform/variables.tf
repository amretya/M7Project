variable "project_id" {
  description = "The ID of the project in which to create the resources."
  type        = string
  default     = "m7projectemotion"
}

variable "region" {
  description = "The region in which to create the resources."
  type        = string
  default     = "asia-southeast1"
}

variable "service_name" {
  description = "The name of the Cloud Run service."
  type        = string
  default     = "m7projectemotion"
}

variable "image_url" {
  description = "The URL of the Docker image to deploy."
  type        = string
  default     = "asia-southeast1-docker.pkg.dev/m7projectemotion/cloud-run-source-deploy/cloud-run-source-deploy:latest"
}

variable "cpu" {
  description = "The number of CPUs to allocate to the Cloud Run service."
  type        = string
  default     = "2"
}

variable "memory" {
  description = "The amount of memory to allocate to the Cloud Run service."
  type        = string
  default     = "2Gi"
}

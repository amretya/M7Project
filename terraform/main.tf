resource "google_cloud_run_service" "default" {
  name     = var.service_name
  location = var.region

  template {
    spec {
      containers {
        image = var.image_url

        resources {
          limits = {
            memory = var.memory
            cpu    = var.cpu
          }
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

}

resource "google_cloud_run_service_iam_member" "noauth" {
  service   = google_cloud_run_service.default.name
  location  = google_cloud_run_service.default.location
  role      = "roles/run.invoker"
  member    = "allUsers"
}

output "cloud_run_url" {
  value = google_cloud_run_service.default.status[0].url
}

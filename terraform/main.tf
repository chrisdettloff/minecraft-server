resource "google_service_account" "default" {
  account_id = "minecraft-server-default"
  display_name = "minecraft-server-default"
}

resource "google_compute_instance" "name" {
  name = "minecraft-server"
  machine_type = "n2-standard-4"
  zone = "us-central1-a"
  

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  network_interface {
    network = "default"
  }
}
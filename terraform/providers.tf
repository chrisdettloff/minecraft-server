terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.16.0"
    }
  }

  backend "gcs" {
    bucket = "tf-state"
    prefix = "minecraft-server"
  }
}

provider "google" {
  project     = "minecraft-server-352615"
  region      = "us-central1"
}
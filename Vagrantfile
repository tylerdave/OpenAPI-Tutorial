Vagrant.configure("2") do |config|
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "tylerdave/openapi-tutorial"
  config.vm.hostname = "openapi-tutorial"
  config.vm.define "openapi-tutorial" do |tutorial|
  end
  config.vm.provider :virtualbox do |vb|
      vb.name = "openapi-tutorial"
  end
  config.ssh.keep_alive = true
  config.ssh.username = "ubuntu"
  config.vm.synced_folder ".", "/home/ubuntu/tutorial-repo"
  config.vm.network "forwarded_port", guest: 8080, host: 8080  # connexion API
  config.vm.network "forwarded_port", guest: 8000, host: 8000  # swagger-editor

  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
end

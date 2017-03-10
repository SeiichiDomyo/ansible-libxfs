# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "bento/centos-7.1"
    centos7.vm.network "private_network", ip: "192.168.33.51"
    centos7.vm.provision :shell, :path => "bootstrap-centos7.sh"  
    centos7.vm.provision "ansible" do |ansible|
      ansible.playbook = "tasks/centos7.yml"
      ansible.inventory_path = "hosts"
      ansible.limit = 'centos7'
    end 
  end

  config.vm.define "centos6" do |centos6|
    centos6.vm.box = "bento/centos-6.7"
    centos6.vm.network "private_network", ip: "192.168.33.52"
    centos6.vm.provision :shell, :path => "bootstrap-centos6.sh"  
    centos6.vm.provision "ansible" do |ansible|
      ansible.playbook = "tasks/centos6.yml"
      ansible.inventory_path = "hosts"
      ansible.limit = 'centos6'
    end 
  end

  config.vm.define "centos5" do |centos5|
    centos5.vm.box = "bento/centos-5.11"
    centos5.vm.network "private_network", ip: "192.168.33.53"
    centos5.vm.provision :shell, :path => "bootstrap-centos5.sh"  
    centos5.vm.provision "ansible" do |ansible|
      ansible.playbook = "tasks/centos5.yml"
      ansible.inventory_path = "hosts"
      ansible.limit = 'centos5'
    end 
  end

end

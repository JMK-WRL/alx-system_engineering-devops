# Puppet manifest to install Flask with a specific version

package { 'python3-pip':
  ensure => 'installed',  # Ensure pip3 is installed
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',  # Specify the path to find pip3
  require => Package['python3-pip'],  # Ensure python3-pip is installed first
}

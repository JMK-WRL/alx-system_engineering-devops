# Puppet manifest to kill a process named 'killmenow'

exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',  # Specify the path to find pkill
}

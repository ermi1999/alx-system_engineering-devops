# updates a file limit in nginx
exec { 'limit':
  command => 'sudo sed -i "/^ULIMIT=\\\"/ c\\ULIMIT=\\\"-n 2000\\\"" /etc/default/nginx',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}
